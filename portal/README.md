# EAI Standard Portal

The portal is an informative, static browser view of repository sources. It does not add or change normative definitions, rules, cases or evidence. The Python build generates one version index; the browser uses that index and the actual published JSON schemas. No separate database or external JavaScript service is used.

The site root is the interactive portal. Existing schema URLs are unchanged. `schema-index.html` retains a plain list for clients without JavaScript. The version selector uses the exact commit pins in `schema-snapshots.json`. A verified Git tag is shown only if it resolves to the pinned commit.

## Run locally

Use a full Git checkout and Python 3.12:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/build_schema_site.py
python -m http.server 8000 --directory _site
```

Open http://localhost:8000/. The navigation can be switched between English and Dutch; the English normative text remains authoritative. The dictionary uses its own bilingual entries.

## Checks

```sh
python -m pip install playwright==1.65.2
python -m playwright install chromium
python scripts/test_portal.py
```

The browser check exercises desktop and mobile layouts, search, navigation, filters, schema inspection, version comparison, language and theme. Screenshots are emitted in `portal-screenshots/` and uploaded by the publication workflow.

On `main`, the publication workflow verifies the site first, then publishes immutable candidate Git tags and pre-releases from the pin map, then rebuilds with the tags present and deploys. A failed check blocks that pipeline; PR runs have no write access to tags or Pages.
