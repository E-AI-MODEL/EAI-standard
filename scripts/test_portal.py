"""Exercise the built static portal in a real Chromium browser."""
import functools
import json
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright, expect
from build_schema_site import ROOT

SITE = ROOT / "_site"
SHOTS = ROOT / "portal-screenshots"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def assert_no_overflow(page, context):
    size = page.evaluate("({body: document.documentElement.scrollWidth, viewport: innerWidth})")
    assert size["body"] <= size["viewport"] + 1, f"Horizontal page overflow: {context}: {size}"


def snapshot(page, name):
    page.screenshot(path=str(SHOTS / (name + ".png")), full_page=True, animations="disabled")


def main():
    assert (SITE / "portal-data.json").is_file()
    SHOTS.mkdir(exist_ok=True)
    data = json.loads((SITE / "portal-data.json").read_text(encoding="utf-8"))
    assert data["current"] in data["versions"]
    for version in data["versions"].values():
        assert version["version"] in data["versions"]
        assert version["rules"] and version["schemas"]
        for schema in version["schemas"]:
            assert (SITE / schema["url"]).is_file(), schema["url"]
        assert (SITE / "releases" / version["version"] / "LICENSE").is_file()
    server = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(SITE)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://127.0.0.1:{server.server_port}/"
    errors = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 1000}, color_scheme="light")
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(url)
            expect(page.locator("#main h1")).to_have_text("EAI Standard")
            expect(page.locator(".stat").first).to_be_visible()
            assert_no_overflow(page, "desktop overview")
            snapshot(page, "desktop-overview")
            page.locator("#search").fill("EAI-R034")
            expect(page.locator("#results .search-result").first).to_contain_text("EAI-R034")
            page.locator("#search").press("Enter")
            expect(page.locator("#rule-detail")).to_contain_text("EAI-R034")
            page.locator("#nav a[href='#concepts']").click()
            expect(page.locator(".graph-center")).to_be_visible()
            expect(page.locator(".relation-list")).not_to_be_empty()
            assert_no_overflow(page, "desktop concepts")
            snapshot(page, "desktop-concepts")
            page.locator("#nav a[href='#overview']").click()
            page.locator(".position[data-position='education_native']").click()
            expect(page.locator("#position-filter")).to_have_value("education_native")
            assert page.locator(".items .item:visible").count() < data["versions"][data["current"]]["dictionary"].__len__()
            page.locator("#filter-list").fill("nonexistent-test-key")
            expect(page.locator("#list-empty")).to_be_visible()
            page.locator("#filter-list").fill("")
            page.locator("#nav a[href='#schemas']").click()
            expect(page.locator("#schema-id")).to_contain_text("/schemas/case.schema.json")
            expect(page.locator("#schema-body .field-group").first).to_be_visible()
            page.locator("#schema-body summary").filter(has_text="actors").first.click()
            expect(page.locator("#schema-body details[open]").first).to_be_visible()
            assert_no_overflow(page, "desktop schema")
            snapshot(page, "desktop-schema")
            page.locator("[data-schema-mode='json']").click()
            expect(page.locator("#schema-raw")).to_contain_text('"$id"')
            page.locator("[data-schema-mode='fields']").click()
            page.locator("#nav a[href='#evidence']").click()
            expect(page.locator(".source-card").first).to_be_visible()
            page.locator("#nav a[href='#cases']").click()
            expect(page.locator(".case-action").first).to_be_visible()
            page.locator("#nav a[href='#adapters']").click()
            expect(page.locator(".table-wrap tbody tr").first).to_be_visible()
            page.locator("#nav a[href='#versions']").click()
            expect(page.locator("#schema-diff")).to_contain_text("changed values or fields")
            if len(data["versions"]) > 1:
                older = sorted(data["versions"])[0]
                page.locator("#version").select_option(older)
                expect(page.locator("#main h1")).to_have_text("EAI Standard")
                expect(page.locator("#version")).to_have_value(older)
                page.locator("#version").select_option(data["current"])
            page.locator("#language").click()
            expect(page.locator("html")).to_have_attribute("lang", "nl")
            expect(page.locator("#nav")).to_contain_text("Woordenboek")
            page.locator("#theme").click()
            expect(page.locator("html")).to_have_attribute("data-theme", "dark")
            assert_no_overflow(page, "desktop dark")
            snapshot(page, "desktop-dark")
            page.close()

            mobile = browser.new_page(viewport={"width": 393, "height": 852}, device_scale_factor=1,
                                      is_mobile=True, has_touch=True, color_scheme="light")
            mobile.on("pageerror", lambda e: errors.append(str(e)))
            mobile.goto(url)
            expect(mobile.locator("#main h1")).to_have_text("EAI Standard")
            assert_no_overflow(mobile, "mobile overview")
            snapshot(mobile, "mobile-overview")
            mobile.locator("#menu").click()
            expect(mobile.locator("#menu")).to_have_attribute("aria-expanded", "true")
            mobile.locator("#nav a[href='#dictionary']").click()
            expect(mobile.locator("#menu")).to_have_attribute("aria-expanded", "false")
            expect(mobile.locator(".detail .meaning").first).to_be_visible()
            assert_no_overflow(mobile, "mobile dictionary")
            snapshot(mobile, "mobile-dictionary")
            mobile.locator("#menu").click()
            mobile.locator("#nav a[href='#schemas']").click()
            expect(mobile.locator("#schema-id")).to_contain_text("/schemas/case.schema.json")
            assert_no_overflow(mobile, "mobile schema")
            mobile.locator("[data-schema-mode='json']").click()
            expect(mobile.locator("#schema-raw")).to_be_visible()
            assert_no_overflow(mobile, "mobile raw JSON")
            snapshot(mobile, "mobile-schema")
            browser.close()
        assert not errors, errors
        print("Portal browser checks passed: desktop and mobile navigation, search, position filter, schema tree, raw JSON, research, cases, adapters, version comparison, language and theme.")
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
