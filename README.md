# Mubea Digital — Programme Progress Dashboard

A self-contained static website that presents the progress of the four projects:

- **MubeAbsent** — annual-leave workflow, team calendar, administration (production preparation)
- **Mubea Portal** — application catalogue, accounts and roles, production packaging (ready to deploy)
- **Mubea Technicien Dashboard** — tools inventory with barcode labels (in service)
- **Overtime Management System** — overtime workflow, approvals, assignments, CSV hand-off (Phase 1 verified; administration console, account management and password change delivered)

Contents: overview KPIs, per-project status with application screenshots, verified evidence,
provisional planning (Gantt snapshots), the open decisions on the critical path and the tooling
requests.

No build step, no dependencies — plain HTML/CSS/JS.

## Preview locally

```powershell
cd mubea-program-dashboard
python -m http.server 8080
# then open http://localhost:8080
```

## Publish on Vercel

Any of these options works; all of them produce a public URL you can send by email.

### Option A — Drag & drop (fastest)

1. Go to <https://vercel.com/new>.
2. Drag the whole `mubea-program-dashboard` folder onto the upload area.
3. Deploy — Vercel serves it as a static site. Copy the public URL.

### Option B — Vercel CLI

```powershell
npx vercel login          # once
cd mubea-program-dashboard
npx vercel --prod
```

### Option C — GitHub import

1. Create a repository containing this folder (files at the repository root).
2. On <https://vercel.com/new>, import the repository.
3. Framework preset: **Other** — leave Build Command and Output Directory empty.
4. Deploy.

### Behind the corporate TLS-inspection proxy

On machines behind the Mubea TLS-inspection proxy, Node (and therefore the
Vercel CLI and `npx`) can fail with `fetch failed` or certificate errors —
Windows trusts the proxy CA, Node only trusts its bundled roots. Export the
corporate roots once and point Node at them in the same terminal as the
deploy command:

```powershell
$pem = "$env:TEMP\mubea-corporate-ca.pem"
Get-ChildItem Cert:\LocalMachine\Root |
  Where-Object { $_.Subject -match 'CN=Mubea-' } |
  ForEach-Object {
    "-----BEGIN CERTIFICATE-----"
    [Convert]::ToBase64String($_.RawData, 'InsertLineBreaks')
    "-----END CERTIFICATE-----"
  } | Set-Content $pem -Encoding ascii
$env:NODE_EXTRA_CA_CERTS = $pem
npx vercel --prod
```

TLS verification stays enabled; only the corporate roots already trusted by
Windows are added for this terminal session.

## Updating the dashboard later

- Content lives in `index.html` (text, statuses, tables).
- The page opens with the "30-second view" board (`#board`): one row per application with
  its state, the next date and what is needed from management. Update it together with the
  matching detail section whenever a status changes.
- Each project detail is a `<details>` panel, collapsed by default; its summary line has to
  make sense on its own. Links to `#p-…` open the panel automatically (`assets/app.js`), and
  printing or "Save as PDF" expands every panel first.
- Styling: `assets/styles.css`; behaviour: `assets/app.js` (lightbox + reveal animation).
- Replace the Gantt snapshots in `assets/img/` (`gantt-mubeabsent.png`, `gantt-portal.png`,
  `gantt-overtime.png`) and update the "Updated …" date in `index.html` when the planning
  changes.
- Publishing is manual: the project is linked to Vercel through the CLI (`.vercel/project.json`),
  not through a Git integration, so pushing to GitHub does not deploy. Run `npx vercel --prod`
  from this folder instead — behind the corporate proxy, set `NODE_EXTRA_CA_CERTS` first as
  described above. `npx vercel git connect` would switch the project to deploy-on-push.
