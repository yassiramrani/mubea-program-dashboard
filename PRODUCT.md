# Product

## Platform and stack

Internal programme-reporting website. Static HTML, CSS and JavaScript, with `status.json` and the dependency-free `tools/update-dashboard.py` generator. There is no application database or sign-in integration in this reporting repository. Preview locally; publishing uses a separate release action.

## Audience and purpose

Yassir, plant management and the HR, Finance, PM, Production and IT stakeholders need a shared view of delivered scope, verification, job stoppers and the next decision for each Mubea software workstream.

## Scope

Six workstreams across seven source repositories: Mubea Portal, MubeAbsent, Overtime, MSCM Faucon / Investment Monitor, Workshop Tool Tracking, and spare-parts/MRP. The older spare-parts prototype is reference material for the MRP domain, not a separate stock system to roll out. The SAP/Bluebird platform decision applies only to spare-parts/MRP; the local implementation in that domain was rejected.

## Evidence and reporting rules

Use recorded build/test results, repository implementation and documented owner decisions. Screenshots identify local demo verification; they are not proof of deployment or business acceptance. Keep checks scoped by runtime and database: local SQLite success must not imply PostgreSQL concurrency acceptance. Do not renew historical targets as current commitments or infer HR entitlements, approved budgets, project progress, target mappings or production release status. No production employee data, credentials, raw databases or private export packages belong in this site.

## Completion and release

Distinguish implemented source, locally verified behavior, deployed behavior and business acceptance. HR confirms policy and employee data; Finance confirms financial meanings and reporting inputs; PM/Production/IT decide the MRP platform and process ownership; IT/application owners confirm hosting, identity, notifications, backups and monitoring. Unknown dates remain uncommitted. A Git push does not publish the CLI-linked reporting site.

## Interface

Preserve the existing `assets/styles.css` design and native project disclosures. The first view shows current status and next decisions; details provide delivered scope, evidence and job stoppers. Desktop/mobile readability and accurate labels take priority over decorative changes.
