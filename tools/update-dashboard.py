"""Render the current status using the dashboard's established components. No dependencies."""
import json
from html import escape as e
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'status.json').read_text(encoding='utf-8'))
source = (root / 'index.html').read_text(encoding='utf-8')
header = source.split('<main id="top">')[0]
import re
header = re.sub(r'Updated \d+ \w+ 2026', 'Updated ' + data['updated'], header)
header = header.replace('Five applications, one programme: delivered scope, verified evidence, planning and open decisions.', 'Six workstreams: verified local progress, evidence and open decisions.')
start = '''<main id="top">
<section class="hero"><div class="wrap"><h1>Six workstreams.<br><span>Progress and the decisions ahead.</span></h1>
<p class="lead">Local technical completion and business acceptance are tracked separately. Updated 16 November 2026; no new go-live dates are assumed.</p>
<div class="chips"><span class="chip">6 workstreams · 7 repositories</span><span class="chip">Verification 13-16 November 2026 recorded</span><span class="chip chip-warn">SAP / Bluebird decision: technician dashboard</span></div>
<div class="hero-actions"><a class="btn btn-primary" href="#board">Review project status</a><a class="btn btn-ghost" href="#planning">Open decisions</a></div></div></section>
<section id="board" class="section"><div class="wrap"><header class="section-head"><h2>The programme in 30 seconds</h2><p class="section-sub">Select a project for delivered scope, evidence and job stoppers. These source changes are not a production deployment.</p></header>
<div class="board-wrap"><table class="board"><thead><tr><th scope="col">Project</th><th scope="col">Current state</th><th scope="col">Next step</th></tr></thead><tbody>'''
rows = ''.join(f'<tr><th scope="row"><a href="#p-{e(p["id"])}">{e(p["name"])}</a></th><td>{e(p["state"])}</td><td>{e(p["next"])}</td></tr>' for p in data['projects'])
middle = '''</tbody></table></div></div></section>
<section id="overview" class="section section-alt"><div class="wrap"><header class="section-head"><h2>What completion means</h2><p class="section-sub">A passing build verifies software. HR and Finance validate business rules; IT confirms deployment, access and operations. Historical October plans remain historical and are not renewed as commitments.</p></header></div></section>
<section id="projects" class="section"><div class="wrap"><header class="section-head"><h2>Project detail and job stoppers</h2></header>'''
details = []
for p in data['projects']:
    image = f'<figure class="figure"><img src="assets/img/2026-11-13/{e(p["image"])}" alt="{e(p["name"])}: isolated local verification screenshot" loading="lazy"><figcaption>Local verification, 13-16 November 2026 · demo data</figcaption></figure>' if p['image'] else ''
    details.append(f'''<details class="detail card" id="p-{e(p['id'])}"><summary class="detail-summary"><span class="dot" aria-hidden="true"></span><span class="summary-name">{e(p['name'])}</span><span class="badge badge-progress">{e(p['state'])}</span><span class="summary-more">Full detail</span></summary>
<div class="detail-grid"><div class="detail-main"><h3>Delivered</h3><p>{e(p['delivered'])}</p><h3>Verification</h3><p>{e(p['evidence'])}</p>{image}</div><aside class="detail-side"><h3>Job stoppers</h3><p>{e(p['stoppers'])}</p><h3>Next step</h3><p>{e(p['next'])}</p></aside></div></details>''')
end = '''</div></section><section id="planning" class="section section-alt"><div class="wrap"><header class="section-head"><h2>Decisions needed to proceed</h2></header>
<ul class="stoppers"><li><strong>HR:</strong> absence rules, balances, employee data and overtime workflow acceptance.</li><li><strong>Finance / SAP:</strong> Faucon definitions, reporting periods and approved project information.</li><li><strong>PM / Production / IT:</strong> assess SAP fit or Bluebird for the Mubea technician dashboard and agree process ownership. Anna's 1–2 day Bluebird estimate is not a committed delivery date.</li><li><strong>Inventory owner:</strong> validate spare-parts/MRP stock, locations and hardware workflows.</li><li><strong>IT / application owners:</strong> hosting, HTTPS, corporate identity, backups, monitoring, notification sender and scheduling.</li></ul></div></section>
<section id="evidence" class="section"><div class="wrap"><header class="section-head"><h2>Verification evidence</h2><p class="section-sub">Results are listed per project because the suites cover different runtimes and scopes. PostgreSQL concurrency tests and production acceptance are not implied by local SQLite checks.</p></header><p>The screenshots use isolated demo accounts. Existing live services and owner databases were not replaced. The 30 October progress report remains a historical record.</p></div></section></main>
<footer class="footer"><div class="wrap footer-inner"><div class="footer-titles"><strong>Mubea Digital — programme progress</strong><p>Updated 16 November 2026 · next review to be agreed</p></div><div class="footer-contact"><strong>Yassir AMRANI</strong><p>Mubea Suspension Components Morocco SARL</p></div></div></footer>
<script src="assets/app.js"></script></body></html>'''
(root / 'index.html').write_text(header + start + rows + middle + ''.join(details) + end, encoding='utf-8')
