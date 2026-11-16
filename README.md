# Mubea Digital - Programme Progress Dashboard

Six workstreams across seven repositories: Portal, MubeAbsent, Overtime, MSCM Faucon, Workshop Tool Tracking and spare-parts/MRP (including the older spare-parts reference repository). Updated 16 November 2026.

Corrected scope: Anna's SAP/Bluebird feedback concerns the Mubea technician dashboard (Workshop Tool Tracking). Spare-parts/MRP has separate inventory and operational validation.

Current delivered scope, verification and job stoppers live in `status.json`. Run `python tools/update-dashboard.py` after editing it; the generated `index.html` uses the existing static stylesheet and disclosure behavior. Screenshots use isolated demo data. October plans and past CI results are not renewed as current commitments. Source changes do not establish a production release.

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

- Edit `status.json`, then run `python tools/update-dashboard.py` from this repository.
- Update screenshots and their provenance under `assets/img/2026-11-13/` (the verification-batch directory; captures span 13-16 November).
- Keep local checks, production deployment and business acceptance distinct. Do not invent dates or infer budgets/HR policies.
- `assets/styles.css` and `assets/app.js` retain the established design and disclosure/print behavior.
- Publishing is manual: the CLI-linked Vercel project has no Git deployment integration. A Git push does not publish this site. No publication was performed for this update.
