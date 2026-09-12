# Contributing

Open an issue with a clear problem, expected behaviour and a fictional example. For a guide change, include browser and reproduction steps. For an agent behaviour change, include the configuration version, test ID and a sanitised response summary. Never post live SOPs, personal data, private organisational links, credentials or unapproved agent outputs.

Keep the core agent advisory and portable. Changes to instructions should preserve the six recommendations, effort/capacity distinctions and retained human decisions. Add or update meaningful evaluation scenarios when behaviour changes.

Edit canonical configuration in `agent/`, test scenarios in `tests/scenarios.json`, and browser behaviour in `scripts/guide-ui.js` or `scripts/guide-core.js`. Run:

```sh
python scripts/build-guide.py
python scripts/validate.py
node --test tests/guide.test.cjs
```

Commit the regenerated `docs/index.html` with its sources. Document visible changes in the changelog. Do not silently edit the original reference downloads; they establish provenance. Any new local-tenant claims require explicit supporting evidence and a date.
