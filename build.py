#!/usr/bin/env python3
"""Builds the Alarmco Technology Solutions concept site into ./dist.
One responsive build serves both desktop and phone."""
import pathlib, shutil

ROOT = pathlib.Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"
REAL = "https://www.alarmcoinc.com"
PHONE, TEL = "(208) 376-9731", "tel:+12083769731"

CHECK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#D80016" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>'
ARROW = '<span class="arr" aria-hidden="true">&#8594;</span>'
NOW = '<span class="badge now"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>Available now</span>'
SOON = '<span class="badge soon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>Coming soon</span>'

PAGES = [  # (slug, short label, file)
    ("overview", "Overview", "index.html"),
    ("cctv", "Video Surveillance", "video-surveillance.html"),
    ("access", "Card Access", "card-access.html"),
    ("cabling", "Structured Cabling", "structured-cabling.html"),
    ("entrance", "Entrance Control", "entrance-control.html"),
    ("integration", "System Integration", "integration.html"),
    ("monitoring", "24/7 Monitoring", "monitoring.html"),
]

def head(title, desc):
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0b0b0c">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>"""

def header(active):
    return f"""
<div class="concept" role="note"><strong>Concept preview</strong> prepared by Justin Whitton for Alarmco, Inc. Not the official Alarmco website &mdash; visit <a href="{REAL}/">alarmcoinc.com</a>.</div>
<div class="util"><div class="wrap">
  <div class="soc">
    <a href="https://www.facebook.com/profile.php?id=100068637940435" aria-label="Alarmco on Facebook"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-1.6 19.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 12 2z"/></svg></a>
    <a href="https://www.youtube.com/user/AlarmCoincorporated" aria-label="Alarmco on YouTube"><svg width="19" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9L15.5 12z"/></svg></a>
  </div>
  <span class="tag">Home to Idaho's only local UL-listed central station</span>
  <a href="{TEL}"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 15.5c-1.2 0-2.4-.2-3.6-.6-.3-.1-.7 0-1 .2l-2.2 2.2a15 15 0 0 1-6.6-6.6l2.2-2.2c.3-.3.4-.7.2-1-.3-1.1-.5-2.3-.5-3.5 0-.6-.4-1-1-1H4c-.6 0-1 .4-1 1 0 9.4 7.6 17 17 17 .6 0 1-.4 1-1v-3.5c0-.6-.4-1-1-1z"/></svg>{PHONE}</a>
</div></div>
<div class="logo-band"><a class="logo" href="index.html" aria-label="Alarmco Technology Solutions home"><img src="assets/img/logo.webp" alt="Alarmco, Inc." width="400" height="55"></a></div>
<div class="navbar"><div class="wrap nb-in">
  <button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg><span>Menu</span></button>
  <nav class="nav" id="nav" aria-label="Main">
    <a href="{REAL}/">Home</a>
    <a href="{REAL}/products-and-services/">Products and Services <span class="car" aria-hidden="true"></span></a>
    <a href="index.html" aria-current="page">Technology Solutions</a>
    <a href="{REAL}/remote-guard-service-rgs/">Remote Guard Service (RGS)</a>
    <a href="{REAL}/about/">About <span class="car" aria-hidden="true"></span></a>
    <a href="{REAL}/blog/">Blog</a>
    <a href="{REAL}/contact/">Contact</a>
    <a href="https://sedonaweb.alarmcoinc.com/login.aspx">Pay Bill</a>
    <a class="nav-cta" href="index.html#assessment">Free Site Assessment</a>
  </nav>
</div></div>
<nav class="subnav" aria-label="Technology Solutions"><div class="wrap">
{''.join(f'<a href="{f}"' + (' aria-current="page"' if s == active else '') + f'>{l}</a>' for s, l, f in PAGES)}
</div></nav>
<main id="main">"""

FOOT = f"""</main>
<footer class="foot">
  <div class="wrap cols">
    <div>
      <div class="tagline">Commitment to Standards &amp; Partnerships</div>
      <div class="big">We Are Your Ultimate Security Partner In Boise, ID And Beyond.</div>
      <p class="muted">Home To Idaho's Only Local Central Station. SBA-certified WOSB / EDWOSB.</p>
    </div>
    <div>
      <h4>Technology Solutions</h4>
      <ul>{''.join(f'<li><a href="{f}">{l}</a></li>' for s, l, f in PAGES[1:])}</ul>
    </div>
    <div>
      <h4>Visit or Call</h4>
      <p class="muted">1675 N Mitchell Street<br>Boise, ID 83704</p>
      <p class="muted" style="margin-top:10px"><a href="{TEL}">{PHONE}</a><br>Fax (208) 376-9632<br>24-hour repair service</p>
    </div>
  </div>
  <div class="bar">&copy; 2026 Alarmco Inc &mdash; All Rights Reserved<small>Concept pages prepared by Justin Whitton. Product names are trademarks of their respective owners.</small></div>
</footer>
<script src="assets/site.js" defer></script>
</body>
</html>"""

def page(slug, title, desc, body):
    return head(title, desc) + header(slug) + body + FOOT

def cta(h, p, btn="Schedule My Assessment"):
    return f"""
<section class="cta"><div class="wrap rv">
  <h2>{h}</h2><p>{p}</p>
  <div class="btns"><a class="btn dark" href="{REAL}/contact/">{btn} {ARROW}</a><a class="btn ghost" href="{TEL}">{PHONE}</a></div>
</div></section>"""

def phero(img, alt, crumb, h1, p, btn):
    return f"""
<section class="phero"><img src="assets/img/{img}" alt="{alt}"><div class="wrap">
  <div class="crumb"><a href="index.html">Technology Solutions</a> &rsaquo; {crumb}</div>
  <h1>{h1}</h1><p>{p}</p>
  <a class="btn" href="{REAL}/contact/">{btn} {ARROW}</a>
</div></section>"""

def plat(name, cat, text, fits, now, fit_label="Where it fits"):
    lis = "".join(f"<li>{f}</li>" for f in fits)
    return f"""<article class="plat{'' if now else ' soon'} rv">
  <div class="top"><h3>{name}</h3>{NOW if now else SOON}</div>
  <div class="cat">{cat}</div><p>{text}</p>
  <div class="fit-h">{fit_label}</div><ul>{lis}</ul>
</article>"""

def checks(items, two=False):
    return f'<ul class="checks{" two" if two else ""}">' + "".join(f"<li>{CHECK}<span>{i}</span></li>" for i in items) + "</ul>"

def tiles(items, cls="g3"):
    return f'<div class="grid {cls}">' + "".join(
        f'<div class="tile rv d{i%4}"><h3>{h}</h3><p>{t}</p></div>' for i, (h, t) in enumerate(items)) + "</div>"

def sec_head(eyebrow, h2, lede=""):
    return f'<div class="sec-head"><div><div class="eyebrow">{eyebrow}</div><h2 class="h2">{h2}</h2></div>' + (f'<p class="lede">{lede}</p>' if lede else "") + "</div>"

# ---------------------------------------------------------------- building plan
def plan_svg(label):
    cams = [  # x, y, angle, id
        (32, 272, 22, "c1"), (566, 392, 205, "c2"), (232, 32, 55, "c3"),
        (566, 32, 135, "c4"), (32, 124, 18, "c5"), (404, 274, 200, "c6")]
    cam = "".join(f"""<g class="cam" data-id="{i}" transform="translate({x} {y}) rotate({a})"><g><path class="fov" d="M0 0L112 -40A119 119 0 0 1 112 40Z"/><animateTransform attributeName="transform" type="rotate" values="-11;11;-11" dur="{7 + n}s" repeatCount="indefinite"/></g><rect x="-6" y="-4" width="12" height="8" rx="2"/><circle class="ring" r="6"/></g>""" for n, (x, y, a, i) in enumerate(cams))
    doors = [
        ("d1", "M270 420V392M330 420V392", "M270 392A28 28 0 0 1 298 420M330 392A28 28 0 0 0 302 420", 346, 406),
        ("d2", "M100 260V222", "M100 222A38 38 0 0 1 138 260", 152, 274),
        ("d3", "M120 76H146", "M146 76A28 28 0 0 1 120 104", 134, 62),
        ("d4", "M420 180H458", "M458 180A40 40 0 0 1 420 220", 406, 232),
        ("d5", "M580 300V380", "", 566, 290)]
    door = "".join(f'<g class="door" data-id="{i}"><path class="leaf{" roll" if i == "d5" else ""}" d="{l}"/>' + (f'<path class="swing" d="{s}"/>' if s else "") + f'<circle class="ring" cx="{x}" cy="{y}" r="6"/><circle class="rdr" cx="{x}" cy="{y}" r="4.5"/></g>' for i, l, s, x, y in doors)
    cab = ["M70 60H232V38", "M232 46H560V38", "M70 60V124H40", "M70 124V272H40", "M110 124H200V274H152",
           "M200 244H406V232", "M300 244V284", "M406 244V270", "M406 252H560V290", "M560 290V386", "M300 318V396H346", "M110 62H134"]
    cabling = "".join(f'<path d="{d}"/>' for d in cab)
    return f"""<svg class="plan" viewBox="0 0 600 440" role="img" aria-label="{label}" data-show="all">
<defs><pattern id="grid-{label[:4]}" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="rgba(255,255,255,.045)" stroke-width="1"/></pattern></defs>
<rect width="600" height="440" fill="url(#grid-{label[:4]})"/>
<g class="lyr base">
  <rect x="20" y="20" width="560" height="400" class="floor"/>
  <path class="wall" d="M270 420H20V20H580V300M580 380V420H330M120 20V76M120 104V110H20M220 110V260M20 260H100M140 260H260M340 260H580M420 20V180M420 220V260"/>
  <g class="rm"><text x="70" y="52" text-anchor="middle">MDF</text><text x="120" y="196" text-anchor="middle">OFFICES</text><text x="320" y="150" text-anchor="middle">OPEN OFFICE</text><text x="500" y="150" text-anchor="middle">WAREHOUSE</text><text x="150" y="348" text-anchor="middle">LOBBY</text><text x="520" y="348" text-anchor="middle">DOCK</text><text x="300" y="436" text-anchor="middle">MAIN ENTRANCE</text></g>
  <rect class="mdf" x="46" y="58" width="48" height="16" rx="2"/>
</g>
<g class="lyr cabling" data-l="cabling">{cabling}</g>
<g class="lyr video" data-l="video">{cam}</g>
<g class="lyr access" data-l="access">{door}</g>
<g class="lyr entrance" data-l="entrance"><g class="ts" data-id="t1"><rect x="258" y="284" width="8" height="34" rx="2"/><rect x="296" y="284" width="8" height="34" rx="2"/><rect x="334" y="284" width="8" height="34" rx="2"/><path class="wing" d="M266 298H279M283 298H296M304 298H317M321 298H334"/><circle class="ring" cx="300" cy="301" r="8"/></g></g>
<g class="lyr integration" data-l="integration">
  <path class="link" d="M346 406C420 380 420 300 404 274"/><path class="link" d="M566 290C590 330 590 360 566 392"/><path class="link" d="M300 290C200 290 80 300 32 272"/><path class="link" d="M406 232C440 150 520 90 566 32"/>
  <g class="uplink" data-id="up"><path d="M70 58V2"/><circle class="ring" cx="70" cy="8" r="6"/><circle class="node" cx="70" cy="8" r="4"/><text x="82" y="12">TO ALARMCO CENTRAL STATION</text></g>
</g>
</svg>"""

# ---------------------------------------------------------------- index
def index():
    solutions = [
        ("01", "video-surveillance.html", "camera.webp", "Network security camera", "Video Surveillance", "Axis and exacqVision today, with i-PRO and Digital Watchdog on the way. Clear evidence, remote viewing, local support."),
        ("02", "card-access.html", "reader.webp", "Fingerprint reader at a door", "Card Access Control", "From one office door to a multi-building campus: cards, phones, PINs and biometrics, with lockdown at the push of a button."),
        ("03", "structured-cabling.html", "construction.webp", "Commercial building under construction", "Structured Cabling", "Category 6/6A copper, fiber backbones and telecom rooms, tested, labeled and documented."),
        ("04", "entrance-control.html", "lock-banner.webp", "Secure entry graphic", "Entrance Control", "Optical turnstiles, speed lanes and security entrances that stop tailgating at the front door."),
        ("05", "integration.html", "console.webp", "Operators at a security console", "Multi-System Integration", "Video, doors, intrusion, fire and intercom working as one system, monitored from Boise."),
        ("06", "monitoring.html", "operator.webp", "Operator watching live camera feeds", "24/7 Monitoring", "Monthly monitoring from Idaho's only local UL-listed central station: alarms, fire, sprinklers and live video."),
    ]
    sol = "".join(f"""<a class="sol rv d{i%3}" href="{h}"><div class="ph"><img src="assets/img/{img}" alt="{alt}" loading="lazy"><span class="num">{n}</span>{SOON if n == '04' else ''}</div>
<div class="bd"><h3>{t}</h3><p>{d}</p><span class="more">Explore {ARROW}</span></div></a>""" for i, (n, h, img, alt, t, d) in enumerate(solutions))
    partners = [("Axis Communications", "Network cameras &amp; door stations", 1), ("exacqVision", "Video management software", 1), ("DMP", "Intrusion &amp; integrated access", 1),
                ("i-PRO", "AI network cameras", 0), ("Digital Watchdog", "Cameras, NVRs &amp; DW Spectrum", 0), ("LenelS2", "Enterprise card access", 0),
                ("Genetec", "Unified security platform", 0), ("Boon Edam", "Turnstiles &amp; security entrances", 0)]
    part = "".join(f'<div class="partner{"" if now else " soon"} rv d{i%4}"><div class="pn">{n}</div><div class="pc">{c}</div>{NOW if now else SOON}</div>' for i, (n, c, now) in enumerate(partners))
    inds = [
        ('<path d="M4 21V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v16"/><path d="M12 8v6M9 11h6M2 21h20"/>', "Healthcare &amp; Clinics", "Patient-area access, pharmacy and med-room control, and camera coverage that respects privacy zones."),
        ('<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c2 2 10 2 12 0v-5M22 9v6"/>', "Schools &amp; Districts", "Lockdown-ready entries, visitor management, and cameras for buildings, buses and parking lots."),
        ('<path d="M2 21V10l6 4V10l6 4V6h4l2 15zM2 21h20"/>', "Manufacturing &amp; Food Processing", "Perimeter and dock cameras, restricted-area access, and cabling for plant-floor networks."),
        ('<path d="M3 21V7l7-4v18M10 9h9a1 1 0 0 1 1 1v11M6 9h1M6 13h1M6 17h1M14 13h2M14 17h2M2 21h20"/>', "Property Management &amp; Multi-Tenant", "Tenant card access, lobby entrance control, and one system across every building you manage."),
        ('<path d="M3 9l9-5 9 5M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 21h18M4 18h16"/>', "Municipal &amp; Public Facilities", "City halls, utilities and public works yards, secured, recorded and monitored locally."),
        ('<path d="M3 9l1.5-5h15L21 9M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0M5 12v9h14v-9M10 21v-5h4v5"/>', "Retail, Banking &amp; Multi-Site", "One login for every location, and video evidence you can find in minutes instead of hours."),
    ]
    ind = "".join(f'<div class="ind rv d{i%3}"><div class="ic"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg></div><div><h3>{h}</h3><p>{t}</p></div></div>' for i, (p, h, t) in enumerate(inds))
    steps = [("Free Site Assessment", "A senior technician walks the facility and documents coverage gaps, aging equipment and code exposure."),
             ("Design &amp; Proposal", "Camera layouts, door schedules and cabling plans, with clear phased pricing."),
             ("Installation", "Installed, programmed and tested by our Boise team, with as-built documentation at turnover."),
             ("Monitoring &amp; Service", "24-hour local monitoring, remote support and service agreements that keep it all working.")]
    stp = "".join(f'<li class="step rv d{i}"><span class="sn">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></li>' for i, (h, t) in enumerate(steps))
    explorer = [
        ("all", "All Systems", "Everything on one plan", "One building, one security picture. Cameras, doors, lanes and cabling, all tied back to a telecom room and monitored from Boise.", "integration.html"),
        ("video", "Video", "Cameras placed for a purpose", "Every camera covers a job: faces at the entry, activity in the lobby, the dock and the warehouse aisles.", "video-surveillance.html"),
        ("access", "Card Access", "Five controlled openings", "Main entrance, offices, server room, warehouse and dock, each with a reader, door contact and electrified hardware.", "card-access.html"),
        ("cabling", "Cabling", "One home run to every device", "Every camera, reader and lane runs back to the MDF on tested, labeled Category 6A.", "structured-cabling.html"),
        ("entrance", "Entrance", "Lanes at the lobby", "Optical lanes between the lobby and the office floor stop tailgating without slowing staff down.", "entrance-control.html"),
        ("integration", "Integration", "Events that trigger responses", "A forced door pulls up the nearest camera. Every alarm reaches Alarmco's central station with video attached.", "integration.html"),
    ]
    tabs = "".join(f'<button type="button" role="tab" class="xt" data-l="{k}" aria-selected="{"true" if k == "all" else "false"}">{lbl}</button>' for k, lbl, *_ in explorer)
    panes = "".join(f'<div class="xp" data-l="{k}"{"" if k == "all" else " hidden"}><div class="eyebrow">{lbl}</div><h3>{h}</h3><p>{t}</p><a class="btn sm dark" href="{href}">See the page {ARROW}</a></div>' for k, lbl, h, t, href in explorer)

    body = f"""
<section class="hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <div class="kicker"><span class="kbar"></span>Commercial Technology Solutions &middot; Boise, Idaho</div>
      <h1 class="hl"><span class="w">Every camera.</span> <span class="w">Every door.</span> <span class="w">Every cable.</span> <span class="w red">One Boise team.</span></h1>
      <p class="hero-p">Video surveillance, card access, structured cabling, entrance control and system integration, designed, installed and monitored by the company that runs Idaho's only local UL-listed 24-hour central station.</p>
      <div class="hero-btns"><a class="btn" href="#assessment">Get a Free Site Assessment {ARROW}</a><a class="btn ghost" href="#explore">Explore the Building</a></div>
      <ul class="hero-proof"><li>Local since 1994</li><li>UL-listed central station</li><li>SBA-certified WOSB</li></ul>
    </div>
    <div class="console" aria-label="Illustrative live site view">
      <div class="con-bar"><span class="live"><i></i>Live site view</span><span class="demo">Illustrative demo</span></div>
      {plan_svg("Animated floor plan showing cameras, card readers, turnstiles and cabling in a commercial building")}
      <ol class="ticker" aria-live="off"></ol>
    </div>
  </div>
  <a class="scroll-cue" href="#stats" aria-label="Scroll to learn more"><span></span></a>
</section>

<section class="stats" id="stats"><div class="wrap grid g4">
  <div class="stat rv"><div class="sv" data-count="1994">1994</div><div class="sl">Serving Boise since</div></div>
  <div class="stat rv d1"><div class="sv">24/7</div><div class="sl">Local UL-listed monitoring</div></div>
  <div class="stat rv d2"><div class="sv" data-count="2003">2003</div><div class="sl">Trusted on government work since</div></div>
  <div class="stat rv d3"><div class="sv">WOSB</div><div class="sl">SBA-certified woman-owned</div></div>
</div></section>

<section class="sec" id="solutions"><div class="wrap">
  {sec_head("What We Design, Install &amp; Support", "Technology Solutions", "Every system is designed around your building, your operations and your budget, then installed and serviced by the same local team.")}
  <div class="sols">{sol}
    <div class="sol offer rv d2" id="assessment">
      <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 4h6v3H9z"/><path d="M8 5.5H6a1 1 0 0 0-1 1V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V6.5a1 1 0 0 0-1-1h-2"/><path d="M8.5 13l2.5 2.5 4.5-5"/></svg>
      <h3>Free On-Site Security Assessment</h3>
      <p>A senior technician walks your facility and documents coverage gaps, aging equipment and code exposure. You keep the written findings whether or not you buy anything.</p>
      <a class="btn dark" href="{REAL}/contact/">Request My Assessment {ARROW}</a>
    </div>
  </div>
</div></section>

<section class="sec dark explore" id="explore"><div class="wrap">
  {sec_head("System Explorer", "See How It Comes Together", "One building, five systems. Pick a system to see where it lives and what it does.")}
  <div class="xgrid">
    <div class="xplan">{plan_svg("Interactive floor plan. Use the system buttons to highlight each system.")}</div>
    <div class="xside">
      <div class="xtabs" role="tablist" aria-label="Systems">{tabs}</div>
      <div class="xpanes">{panes}</div>
    </div>
  </div>
</div></section>

<section class="sec mon"><div class="wrap split">
  <div class="mon-ph rv"><img src="assets/img/operator.webp" alt="Alarmco operator watching live camera feeds" loading="lazy"><span class="mon-live"><i></i>Answered in Boise, 24/7</span></div>
  <div class="copy rv d1">
    <div><div class="eyebrow">Monthly Monitoring</div><h2 class="h2">Watched From Boise, Every Minute of Every Day</h2></div>
    <p class="lede">Installation is day one. Monitoring is every day after. Your alarms, fire and sprinkler signals and cameras report to Idaho's only local UL-listed central station, staffed by people who know the Treasure Valley.</p>
    <ul class="mon-chips">
      <li>Intrusion alarm monitoring {NOW}</li><li>Fire &amp; sprinkler monitoring {NOW}</li>
      <li>Remote Guard Service (live video) {NOW}</li><li>Remote management &amp; alerts {NOW}</li>
      <li>Managed access control {SOON}</li><li>Camera &amp; system health checks {SOON}</li>
    </ul>
    <div><a class="btn" href="monitoring.html">See Monitoring Plans {ARROW}</a></div>
  </div>
</div></section>

<section class="sec soft"><div class="wrap">
  {sec_head("Manufacturer Partners", "Open Platforms, Not Lock-In", "We build on open, standards-based systems, so your cameras, readers and software can be expanded, serviced or reused later instead of ripped out.")}
  <div class="grid g4">{part}</div>
  <p class="note">Lines marked Coming Soon are being added to our line card. Planning a project for next year? Ask us about timing.</p>
</div></section>

<section class="sec"><div class="wrap">
  {sec_head("Built for Local Business", "Who We Work With in the Treasure Valley")}
  <div class="grid g3">{ind}</div>
</div></section>

<section class="sec dark"><div class="wrap">
  {sec_head("How a Project Runs", "From First Walkthrough to 24-Hour Support")}
  <ol class="steps">{stp}</ol>
</div></section>

<section class="sec"><div class="wrap split">
  <img class="rv" src="assets/img/boise.webp" alt="Downtown Boise and the Idaho State Capitol" loading="lazy">
  <div class="copy rv d1">
    <div><div class="eyebrow">Why Alarmco</div><h2 class="h2">Local Since 1994</h2></div>
    {checks(["Serving Boise businesses since January 1994", "Home to Idaho's only local UL-listed 24-hour central station", "SBA-certified Woman-Owned Small Business (WOSB / EDWOSB)", "Trusted on government projects since 2003", "Fire alarm and security under one roof, so door release and egress are coordinated by one team", "24-hour repair service and annual inspections"])}
  </div>
</div></section>
{cta("Find Out What Your Building Actually Needs", "Book a free on-site assessment. We will show you what is working, what is not, and what it costs to fix.", "Book My Assessment")}"""
    return page("overview", "Technology Solutions | Alarmco, Inc. (Concept)", "Video surveillance, card access, structured cabling, entrance control and integration from Boise's Alarmco. Concept preview.", body)

# ---------------------------------------------------------------- subpages
def cctv():
    body = phero("monitoring.webp", "Operators watching a video wall", "Video Surveillance", "Commercial Camera Systems Built on Open Platforms",
                 "Clear, usable video from the parking lot to the loading dock, recorded on systems you own and supported by a Boise team that answers the phone.", "Request a Camera Assessment") + f"""
<section class="sec"><div class="wrap split">
  <div class="copy rv"><div><div class="eyebrow">Enterprise-Grade</div><h2 class="h2">Video for Every Size of Site</h2></div>
    <p class="lede">Four cameras on a storefront or two hundred across a campus, we design around what you need to see: faces at the entry, plates at the gate, activity on the floor. Every camera is placed for a purpose.</p>
    {checks(["Fixed, PTZ, panoramic and multi-sensor cameras", "Recorders and video management sized to your retention needs", "Secure remote viewing from your phone, tablet or browser", "Upgrades that reuse existing cabling and cameras where it makes sense"])}
  </div>
  <img class="rv d1" src="assets/img/floorplan.webp" alt="Floor plan with camera placements reviewed on a tablet" loading="lazy">
</div></section>
<section class="sec soft"><div class="wrap">
  {sec_head("Camera &amp; Recording Platforms", "The Right Platform for the Job", "We recommend the platform that fits your site and budget. Here is where each one shines.")}
  <div class="grid g2">
    {plat("Axis Communications", "Network cameras, audio &amp; door stations", "The network-camera pioneer, and a name found on many commercial and public-sector specifications. Built for image quality in hard light and long service life.", ["Parking lots, entries and perimeters where detail matters", "Sites that want cameras, speakers and intercoms on one network", "Projects written to an engineer's specification"], True)}
    {plat("exacqVision", "Video management software &amp; recorders", "Johnson Controls' video management platform. Records cameras from many manufacturers and scales from a single recorder to multiple sites under one login.", ["Businesses mixing new cameras with ones they already own", "Multi-location owners who want every site in one view", "Sites tying video to access control events"], True)}
    {plat("i-PRO", "AI network cameras", "Formerly Panasonic's security business. Cameras that run AI analytics on the camera itself, so you can search for a person or vehicle by attributes instead of scrubbing hours of video.", ["Large sites where fast investigations save real time", "Rugged outdoor and industrial locations", "Government-funded projects with NDAA requirements"], False)}
    {plat("Digital Watchdog", "MEGApix cameras, Blackjack NVRs &amp; DW Spectrum", "A complete camera, recorder and software line with DW Spectrum IPVMS for web and mobile viewing. Strong value for small and mid-size businesses.", ["Retail, restaurants, offices and small warehouses", "Owners replacing an aging analog DVR system", "Budget-conscious projects that still need professional results"], False)}
  </div>
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("Every Project Includes", "Designed, Installed and Supported Locally")}
  {tiles([("Camera Placement Design", "Field-of-view and pixel-density planning so every camera can identify, not just detect."), ("Storage &amp; Retention Sizing", "Recorders sized for the days of video your insurance, policy or regulator requires."), ("Network &amp; Cyber Hardening", "PoE switching, isolated camera networks, and firmware and passwords managed properly."), ("Mobile &amp; Remote Viewing", "Live and recorded video on your phone, with user rights set by role."), ("Training at Turnover", "Your staff learn to search, export and share clips before we leave the site."), ("Service Agreements", "Health monitoring, preventive maintenance and 24-hour repair service.")])}
</div></section>
<section class="phero band"><img src="assets/img/operator.webp" alt=""><div class="wrap">
  <div class="eyebrow">Take It Further</div><h2 class="h2">Pair Your Cameras With Remote Guard Service</h2>
  <p>Turn recorded video into live protection. Our operators watch your cameras in real time and respond before a break-in becomes a loss.</p>
  <a class="btn" href="monitoring.html">See Monitoring Plans {ARROW}</a>
</div></section>
{cta("Not Sure What Your Cameras Are Missing?", "Our free site assessment shows exactly where your coverage falls short, and what it takes to fix it.")}"""
    return page("cctv", "Video Surveillance | Alarmco, Inc. (Concept)", "Commercial camera systems from Alarmco in Boise: Axis, exacqVision, i-PRO and Digital Watchdog.", body)

def door_svg():
    return """<svg class="door-dia rv" viewBox="0 0 640 480" role="img" aria-label="Diagram of a card-access door: reader, exit sensor, door contact, electrified lock, controller, power supply, server and fire alarm interface">
<rect width="640" height="480" fill="#f4f4f4"/>
<path d="M20 440h600" stroke="#8a8a8a" stroke-width="2"/>
<rect x="180" y="100" width="160" height="340" fill="none" stroke="#0a0a0a" stroke-width="3"/>
<rect x="190" y="110" width="140" height="330" stroke="#0a0a0a" stroke-width="1.5" fill="#fff"/>
<path d="M300 292h24" stroke="#0a0a0a" stroke-width="4" stroke-linecap="round"/>
<rect x="364" y="252" width="26" height="46" rx="3" stroke="#0a0a0a" stroke-width="2" fill="#fff"/><path d="M371 266h12M371 274h12" stroke="#0a0a0a" stroke-width="1.5"/>
<rect x="236" y="68" width="48" height="18" rx="4" stroke="#0a0a0a" stroke-width="2" fill="#fff"/>
<rect x="296" y="96" width="22" height="10" stroke="#0a0a0a" stroke-width="2" fill="#fff"/>
<rect x="331" y="276" width="10" height="34" fill="#D80016"/>
<g fill="#fff" stroke="#0a0a0a" stroke-width="2"><rect x="470" y="150" width="140" height="80"/><rect x="470" y="250" width="140" height="64"/><rect x="470" y="22" width="140" height="56"/></g>
<rect x="470" y="340" width="140" height="64" fill="#fff" stroke="#D80016" stroke-width="2.5"/>
<g fill="none" stroke="#8a8a8a" stroke-width="1.75" stroke-dasharray="5 5" class="flowd"><path d="M390 270h40v-80h40"/><path d="M284 77h146v96h40"/><path d="M318 101h100v84h52"/><path d="M341 304h97v-94h32"/><path d="M540 230v20"/></g>
<path d="M540 150V78" stroke="#0a0a0a" stroke-width="2.5"/>
<path d="M470 372h-24v-150h24" fill="none" stroke="#D80016" stroke-width="2" stroke-dasharray="5 5"/>
<g font-family="Inter,Helvetica,Arial,sans-serif" text-anchor="middle" fill="#0a0a0a">
<text x="540" y="186" font-size="14" font-weight="700">Access controller</text><text x="540" y="206" font-size="12" fill="#555">in telecom room</text>
<text x="540" y="278" font-size="14" font-weight="700">Power supply</text><text x="540" y="298" font-size="12" fill="#555">with battery backup</text>
<text x="540" y="46" font-size="14" font-weight="700">Server / cloud</text><text x="540" y="64" font-size="12" fill="#555">management software</text>
<text x="540" y="368" font-size="14" font-weight="700" fill="#D80016">Fire alarm panel</text><text x="540" y="388" font-size="12" fill="#555">release on alarm</text>
<text x="260" y="466" font-size="12" fill="#555">Secure side</text></g>
<g font-family="Inter,Helvetica,Arial,sans-serif" font-size="12" font-weight="800" text-anchor="middle" fill="#fff">
<circle cx="404" cy="244" r="12" fill="#D80016"/><text x="404" y="248">1</text><circle cx="222" cy="62" r="12" fill="#D80016"/><text x="222" y="66">2</text>
<circle cx="307" cy="126" r="12" fill="#D80016"/><text x="307" y="130">3</text><circle cx="310" cy="330" r="12" fill="#D80016"/><text x="310" y="334">4</text>
<circle cx="456" cy="150" r="12" fill="#0a0a0a"/><text x="456" y="154">5</text><circle cx="456" cy="250" r="12" fill="#0a0a0a"/><text x="456" y="254">6</text>
<circle cx="456" cy="22" r="12" fill="#0a0a0a"/><text x="456" y="26">7</text><circle cx="624" cy="340" r="12" fill="#D80016"/><text x="624" y="344">8</text></g>
</svg>"""

def access():
    legend = [("1", "r", "Reader.", "Card, phone, PIN or biometric. OSDP secure readers encrypt the wiring back to the controller."),
              ("2", "r", "Request-to-exit sensor.", "Lets people leave freely without triggering a forced-door alarm."),
              ("3", "r", "Door position switch.", "Reports doors forced open or propped open."),
              ("4", "r", "Electrified hardware.", "Strike, maglock or electrified lever, fail-safe or fail-secure as code requires."),
              ("5", "k", "Controller.", "Makes the grant or deny decision, even if the network is down."),
              ("6", "k", "Power supply.", "Supervised, with battery backup for the locks and readers."),
              ("7", "k", "Management software.", "Badges, schedules, reports and lockdown, on-site or hosted."),
              ("8", "r", "Fire alarm interface.", "Releases locks on the egress path. Because we also design fire alarm systems, one team coordinates it.")]
    leg = "".join(f'<li><span class="ln {c}">{n}</span><div><strong>{h}</strong> {t}</div></li>' for n, c, h, t in legend)
    body = phero("lock-banner.webp", "Abstract security graphic with a padlock", "Card Access Control", "Card Access Control That Grows With Your Building",
                 "Know who went where and when. Add or revoke a badge in seconds, lock down the building from your phone, and stop re-keying every time a key walks out the door.", "Request an Access Assessment") + f"""
<section class="sec"><div class="wrap split rev">
  <div class="copy rv"><div><div class="eyebrow">One Door to an Entire Campus</div><h2 class="h2">Control, Record and Respond</h2></div>
    <p class="lede">We design access control around how your people actually move through the building: employees, contractors, visitors and after-hours staff. Schedules and alarms are programmed before handover, and every door event is recorded.</p>
    {checks(["Photo ID badging", "Mobile credentials", "One-button lockdown", "24-hour local monitoring", "Elevator floor control", "Video tied to every door event"], True)}
  </div>
  <img class="rv d1" src="assets/img/reader.webp" alt="Person using a fingerprint reader at a door" loading="lazy">
</div></section>
<section class="sec soft"><div class="wrap">
  {sec_head("Access Control Platforms", "Sized to Your Doors, Ready to Grow", "From an integrated panel for a small office to an enterprise platform for a multi-building campus.")}
  <div class="grid g2">
    {plat("LenelS2", "OnGuard &bull; NetBox &bull; BlueDiamond mobile", "One of the most widely specified enterprise access platforms in hospitals, universities and government buildings. Now part of Honeywell.", ["OnGuard for campuses and high-security enterprise sites", "NetBox browser-based control for mid-size buildings", "BlueDiamond mobile credentials on employees' phones"], False)}
    {plat("DMP", "Integrated intrusion &amp; access control", "Card access built into the same panel as your burglar alarm, so one badge can disarm the system and open the door. Managed from the Virtual Keypad app.", ["Offices, clinics and shops with a handful of doors", "Businesses already monitored by our central station", "Owners who want one app for alarm and doors"], True)}
    {plat("Axis Door Solutions", "Network door controllers &amp; IP intercoms", "Door controllers and video door stations on the same network as your Axis cameras. See and speak with a visitor before you let them in.", ["Front entries and receiving doors that need a video intercom", "Sites standardizing on one camera and door vendor", "Remote gates and outbuildings on the network"], True)}
    {plat("Genetec Synergis", "Access control inside Security Center", "Access control that lives in the same software as your video, so doors, cameras and alarms share one map, one alarm list and one login.", ["Airports, utilities and public agencies", "Sites running a security operations desk", "Owners who want video and doors fully unified"], False)}
  </div>
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("What Goes Into a Secured Door", "Anatomy of an Access-Controlled Opening")}
  <div class="anat">{door_svg()}<ol class="legend rv d1">{leg}</ol></div>
</div></section>
<section class="sec dark"><div class="wrap">
  {sec_head("Credential Options", "However Your People Want to Get In")}
  {tiles([("Proximity &amp; Smart Cards", "Keep existing cards during an upgrade, or move to encrypted smart cards."), ("Mobile Credentials", "Badges on employees' phones, issued and revoked remotely."), ("Keypad &amp; PIN", "Simple entry for gates and shared spaces, or as a second factor."), ("Biometrics", "Fingerprint or face readers for pharmacies, server rooms and evidence storage."), ("Photo ID Badging", "Design and print ID badges from the same system that grants access."), ("Visitor Management", "Temporary credentials that expire automatically at the end of the visit.")])}
</div></section>
{cta("Still Re-Keying Every Time Someone Leaves?", "We will walk your doors and show you what card access would cost, door by door.")}"""
    return page("access", "Card Access Control | Alarmco, Inc. (Concept)", "Card access control from Alarmco in Boise: DMP, Axis, LenelS2 and Genetec Synergis.", body)

def cabling():
    body = phero("construction.webp", "Aerial view of a commercial building under construction", "Structured Cabling", "Structured Cabling for New Construction, Tenant Improvements and Upgrades",
                 "The network your cameras, doors, phones and Wi-Fi depend on, installed cleanly, tested end to end and documented so the next person can find every cable.", "Request a Cabling Quote") + f"""
<section class="sec"><div class="wrap split">
  <div class="copy rv"><div><div class="eyebrow">The Foundation</div><h2 class="h2">Infrastructure Done Once, Done Right</h2></div>
    <p class="lede">Most security problems we are called about start in the cabling: unlabeled runs, overloaded PoE switches, cable laid on ceiling tiles. We install the physical layer the way we install life-safety systems, to published standards, and hand you test results and drawings at the end.</p>
    <p class="lede">For general contractors, that means one low-voltage partner for data, security and fire alarm on the same schedule.</p>
  </div>
  <div class="rack rv d1" aria-hidden="true"><svg viewBox="0 0 400 300" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <rect x="110" y="20" width="180" height="260" stroke="#fff" stroke-width="2.5"/><path d="M122 20v260M278 20v260" stroke="#6a6a70" stroke-width="1.5"/>
  <rect x="130" y="40" width="140" height="26" stroke="#fff" stroke-width="1.5"/><g fill="#EA1026" class="blink"><circle cx="146" cy="53" r="3"/><circle cx="160" cy="53" r="3"/><circle cx="174" cy="53" r="3"/></g>
  <rect x="130" y="78" width="140" height="26" stroke="#fff" stroke-width="1.5"/><rect x="130" y="126" width="140" height="26" stroke="#fff" stroke-width="1.5"/>
  <g stroke="#EA1026" stroke-width="2.5"><path d="M142 96c0 16 6 22 18 30"/><path d="M170 96c0 14 4 20 12 30"/><path d="M198 96v30"/><path d="M226 96c0 14-4 20-12 30"/><path d="M254 96c0 16-6 22-18 30"/></g>
  <rect x="130" y="170" width="140" height="40" stroke="#fff" stroke-width="1.5"/><rect x="130" y="222" width="140" height="40" stroke="#fff" stroke-width="1.5"/>
  <g fill="#EA1026" class="blink d"><circle cx="252" cy="190" r="4"/><circle cx="252" cy="242" r="4"/></g>
  <path class="flow" d="M290 60c50 0 60 30 90 30M290 88c40 0 50 50 90 50M290 136c30 0 40 60 90 60M20 90c40 0 50-30 90-30" stroke="#EA1026" stroke-width="2"/></svg></div>
</div></section>
<section class="sec soft"><div class="wrap">
  {sec_head("What We Install", "Copper, Fiber and Everything in Between")}
  {tiles([("Category 6 &amp; 6A Copper", "Horizontal cabling for workstations, phones, access points, cameras and readers, rated for today's PoE loads."), ("Fiber Optic Backbone", "Single-mode and multimode fiber between floors and buildings, terminated and tested."), ("Telecom Rooms &amp; Racks", "Racks, cable management, patch panels, ladder rack and grounding, built to be serviced."), ("Testing &amp; Certification", "Every link tested with a certification tester, with results delivered at closeout."), ("Labeling &amp; As-Builts", "Both ends labeled to a consistent scheme and matched to drawings you can hand to IT."), ("Pathways &amp; Firestopping", "J-hooks, sleeves and firestopped penetrations that pass inspection the first time.")])}
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("How It Fits Together", "From the Main Telecom Room to Every Device")}
  <div class="topo rv">
    <div class="tnode mdf"><strong>MDF &middot; main telecom room</strong><span>Service entrance, core switch, servers, recorders</span></div>
    <div class="tlink fiber"><span>Fiber backbone</span></div>
    <div class="tidfs"><div class="tnode"><strong>IDF 1</strong><span>PoE switch &middot; patch panels</span></div><div class="tnode"><strong>IDF 2</strong><span>PoE switch &middot; patch panels</span></div></div>
    <div class="tlink copper"><span>Category 6A copper &middot; 90 m permanent link max</span></div>
    <div class="tdev"><span>IP cameras</span><span>Card readers</span><span>Wireless APs</span><span>Workstations</span><span>VoIP phones</span><span>Video intercoms</span></div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="sec-head"><h2 class="h2">Installed to Published Standards</h2><div class="on-dark" style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;color:#cfcfcf">Manufacturer-backed extended warranty programs {SOON}</div></div>
  <div class="grid g5 stds">
    <div class="tile rv"><h3>ANSI/TIA-568</h3><p>Cabling &amp; components</p></div><div class="tile rv d1"><h3>TIA-569</h3><p>Pathways &amp; spaces</p></div>
    <div class="tile rv d2"><h3>TIA-606</h3><p>Labeling &amp; administration</p></div><div class="tile rv d3"><h3>TIA-607</h3><p>Bonding &amp; grounding</p></div>
    <div class="tile rv d4"><h3>NFPA 70</h3><p>National Electrical Code</p></div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("One Contractor", "Why Use One Contractor for Cabling and Security")}
  <div class="grid g3 why">
    <div class="rv"><h3>PoE Planned With the Devices</h3><p>Switch power budgets are sized for the cameras, readers and heaters actually going on them.</p></div>
    <div class="rv d1"><h3>Fewer Trades on Site</h3><p>One schedule, one point of contact and no finger-pointing between the cabler and the integrator.</p></div>
    <div class="rv d2"><h3>One Set of Drawings</h3><p>Cabling, security and fire alarm documented together for your facilities and IT teams.</p></div>
  </div>
</div></section>
{cta("Building, Moving or Remodeling?", "Send us your drawings. We will price cabling, cameras and access control together.", "Request a Quote")}"""
    return page("cabling", "Structured Cabling | Alarmco, Inc. (Concept)", "Structured cabling from Alarmco in Boise: Cat 6/6A, fiber, telecom rooms, testing and documentation.", body)

TS = {
 "lanes": '<path d="M10 132h220" stroke="#8a8a8a" stroke-width="1.5"/><g stroke="#0a0a0a" stroke-width="2"><rect x="30" y="58" width="40" height="74" rx="5"/><rect x="170" y="58" width="40" height="74" rx="5"/></g><g stroke="#D80016" stroke-width="2" class="wingl"><path d="M70 78h44v26H70"/></g><g stroke="#D80016" stroke-width="2" class="wingr"><path d="M170 78h-44v26h44"/></g>',
 "tripod": '<path d="M10 132h220" stroke="#8a8a8a" stroke-width="1.5"/><rect x="80" y="52" width="56" height="80" rx="5" stroke="#0a0a0a" stroke-width="2"/><g class="spin" stroke="#D80016" stroke-width="3"><path d="M136 76h60M136 76l26-30M136 76l22 32"/></g>',
 "full": '<rect x="50" y="14" width="140" height="124" stroke="#0a0a0a" stroke-width="2"/><path d="M120 14v124" stroke="#0a0a0a" stroke-width="3"/><g stroke="#D80016" stroke-width="2"><path d="M70 34h50M70 54h50M70 74h50M70 94h50M70 114h50"/></g><g stroke="#0a0a0a" stroke-width="2"><path d="M120 44h50M120 64h50M120 84h50M120 104h50M120 124h50"/></g>',
 "revolve": '<g stroke="#0a0a0a" stroke-width="2.5"><path d="M81 36a55 55 0 0 1 78 0M81 114a55 55 0 0 0 78 0"/></g><g class="spin2" stroke="#D80016" stroke-width="2.5"><path d="M81 36l78 78M159 36l-78 78"/></g><circle cx="120" cy="75" r="5" fill="#0a0a0a"/>',
 "vestibule": '<path d="M60 28h120M60 122h120" stroke="#0a0a0a" stroke-width="3"/><g stroke="#0a0a0a" stroke-width="3"><path d="M60 28v30M60 92v30M180 28v30M180 92v30"/></g><g stroke="#D80016" stroke-width="2"><path d="M60 58l24 10M180 92l-24-10"/></g><g fill="#D80016"><circle cx="48" cy="75" r="4"/><circle cx="192" cy="75" r="4"/></g>',
 "ada": '<path d="M10 132h220" stroke="#8a8a8a" stroke-width="1.5"/><rect x="30" y="58" width="40" height="74" rx="5" stroke="#0a0a0a" stroke-width="2"/><rect x="70" y="76" width="130" height="32" stroke="#D80016" stroke-width="2"/><rect x="200" y="58" width="12" height="74" rx="3" stroke="#0a0a0a" stroke-width="2"/>',
}

def entrance():
    types = [("lanes", "Optical Speed Lanes", "Glass-wing lanes that open for authorized users and alarm on tailgating.", "corporate and medical office lobbies"),
             ("tripod", "Waist-High Tripod Turnstiles", "Durable, economical one-at-a-time entry for high-volume staff areas.", "fitness and recreation centers, staff entries"),
             ("full", "Full-Height Turnstiles", "Floor-to-head rotors for unattended perimeter gates. Nobody climbs over.", "plant perimeters, yards and utilities"),
             ("revolve", "Security Revolving Doors", "One person per rotation, with sensors that detect a second occupant.", "data rooms and high-security buildings"),
             ("vestibule", "Interlock Vestibules", "Two doors that never open at the same time, controlled by the access system.", "pharmacies, cash rooms and labs"),
             ("ada", "Accessible Swing Gates", "Wide lanes for wheelchairs, deliveries and strollers, on the same credential.", "every lane bank, per ADA")]
    tcards = "".join(f'<div class="etype rv d{i%3}"><div class="eart"><svg viewBox="0 0 240 150" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{TS[k]}</svg></div><div class="ebd"><h3>{h}</h3><p>{t}</p><p class="best"><strong>Best for:</strong> {b}</p></div></div>' for i, (k, h, t, b) in enumerate(types))
    body = f"""
<section class="phero ehero"><div class="wrap ehero-in">
  <div><div class="crumb"><a href="index.html">Technology Solutions</a> &rsaquo; Entrance Control</div>
  <h1>Turnstiles and Secured Entrances for Lobbies, Plants and Campuses</h1>
  <p>A card reader controls a door. An entrance lane controls the person. Stop tailgating without slowing down the people who belong there.</p>
  <a class="btn" href="{REAL}/contact/">Start the Conversation {ARROW}</a></div>
  <svg class="lanes-art" viewBox="0 0 460 320" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M10 290h440" stroke="#6a6a70" stroke-width="1.5"/>
  <g stroke="#fff" stroke-width="2.5"><path d="M40 290V150a10 10 0 0 1 10-10h50a10 10 0 0 1 10 10v140"/><path d="M195 290V150a10 10 0 0 1 10-10h50a10 10 0 0 1 10 10v140"/><path d="M350 290V150a10 10 0 0 1 10-10h50a10 10 0 0 1 10 10v140"/></g>
  <g stroke="#EA1026" stroke-width="3" class="wl"><path d="M110 175h38M110 195h38"/></g><g stroke="#EA1026" stroke-width="3" class="wr"><path d="M195 175h-38M195 195h-38"/></g>
  <g stroke="#8a8a8a" stroke-width="2"><path d="M265 175h38M265 195h38M350 175h-38M350 195h-38"/></g>
  <g fill="#EA1026"><circle cx="75" cy="156" r="5"/><circle cx="230" cy="156" r="5"/><circle cx="385" cy="156" r="5"/></g>
  <g class="walker" stroke="#fff" stroke-width="2"><circle cx="152" cy="62" r="16"/><path d="M126 120c3-22 13-32 26-32s23 10 26 32"/></g>
  </svg>
</div></section>
<div class="soonbar"><div class="wrap">{SOON}<span>Entrance control manufacturer partnerships are in progress. Planning a lobby or plant entrance for next year? <a href="{REAL}/contact/">Talk to us now</a> and we will design it with your access control from day one.</span></div></div>
<section class="sec"><div class="wrap split">
  <div class="copy rv"><div><div class="eyebrow">One Credential, One Person</div><h2 class="h2">Stop Tailgating at the Front Door</h2></div>
    <p class="lede">An open door lets in whoever is behind the badge holder. Optical turnstiles and security entrances count each person, sound an alarm on tailgating, and send the video clip to whoever needs to see it.</p>
    <p class="lede">We handle the parts most turnstile projects get wrong: the reader integration, fire alarm release, ADA lanes, and the concrete and power the lanes need before they arrive.</p>
  </div>
  <ol class="seq rv d1"><li><b>01</b>Badge or phone at the lane reader</li><li><b>02</b>Lane opens for exactly one person</li><li><b>03</b>A second person triggers an alarm and a video clip</li></ol>
</div></section>
<section class="sec soft"><div class="wrap">
  {sec_head("Entrance Types", "Matched to Your Traffic and Your Risk")}
  <div class="grid g3">{tcards}</div>
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("Manufacturers We Are Adding", "Proven Entrance Brands")}
  <div class="grid g3">
    <div class="partner soon rv"><div class="pn">Boon Edam</div><div class="pc">Security revolving doors, speed lanes and turnstiles</div>{SOON}</div>
    <div class="partner soon rv d1"><div class="pn">Alvarado</div><div class="pc">Optical, waist-high and full-height turnstiles</div>{SOON}</div>
    <div class="partner soon rv d2"><div class="pn">dormakaba</div><div class="pc">Sensor barriers, swing gates and secured entrances</div>{SOON}</div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  {sec_head("Integration", "Tied Into the Systems You Already Have")}
  <div class="grid g4 why on-dark">
    <div class="rv"><h3>Reader in the Lane</h3><p>The same badges and phones that open your doors open the lanes.</p></div>
    <div class="rv d1"><h3>Video on Every Alarm</h3><p>Tailgating and forced-passage events bookmark the camera clip.</p></div>
    <div class="rv d2"><h3>Fire Alarm Release</h3><p>Lanes open for free egress on alarm, coordinated with the fire system.</p></div>
    <div class="rv d3"><h3>Visitor Passes</h3><p>Temporary credentials that work for one visit, then expire.</p></div>
  </div>
</div></section>
{cta("Planning a Lobby or Plant Entrance?", "Bring us in early. Lanes need power, data and floor prep long before they ship.", "Start the Conversation")}"""
    return page("entrance", "Entrance Control &amp; Turnstiles | Alarmco, Inc. (Concept)", "Optical turnstiles, speed lanes and secured entrances from Alarmco in Boise.", body)

def integration():
    nodes = [(580, 90, "Video surveillance", "Axis &#8226; exacqVision"), (856, 148, "Card access", "DMP &#8226; Axis &#8226; LenelS2 *"), (1004, 297, "Intrusion detection", "DMP panels"),
             (952, 465, "Fire alarm interface", "Door release &#8226; recall"), (433, 575, "Mobile &amp; remote", "Phone, tablet, browser"), (208, 465, "Elevator control", "Floor-by-floor access"),
             (156, 297, "Entrance control *", "Turnstiles &amp; lanes"), (304, 148, "Intercom &amp; visitors", "IP video door stations")]
    lines = "".join(f'<path class="spoke" d="M580 340L{x} {y}"/>' for x, y, *_ in nodes) + '<path class="spoke cs" d="M580 340L727 575"/>'
    boxes = "".join(f'<g class="node"><rect x="{x-105}" y="{y-32}" width="210" height="64"/><text x="{x}" y="{y-4}" class="nt">{t}</text><text x="{x}" y="{y+16}" class="ns">{s}</text></g>' for x, y, t, s in nodes)
    scen = [("A door is forced open", "Pops up the nearest camera, bookmarks the clip, and notifies our central station with video attached."),
            ("The fire alarm activates", "Releases egress doors and lanes, recalls elevators, keeps cameras recording, and dispatches from Boise."),
            ("The last person arms the building", "Switches readers to after-hours rules and turns on exterior camera analytics for the night."),
            ("Someone presses lockdown", "Locks every controlled door, alerts staff on their phones, and shows responders the live cameras."),
            ("Someone tailgates at a lane", "Raises a lane alarm and saves the clip showing who badged in and who followed."),
            ("You manage several locations", "Gives you one login and one alarm list for every site, with badges that work wherever you allow them.")]
    sc = "".join(f'<div class="scen rv d{i%3}"><div class="when">When</div><h3>{h}</h3><div class="then">The system</div><p>{t}</p></div>' for i, (h, t) in enumerate(scen))
    plats = [("exacqVision", "Video with access control events", 1), ("Axis", "Cameras, audio, intercom and door control on one network", 1), ("DMP", "Intrusion and access on one panel, monitored by us", 1), ("Genetec", "Security Center unifies video, access and more", 0), ("LenelS2", "Enterprise access with deep video integrations", 0)]
    pl = "".join(f'<div class="partner dk{"" if n else " soon"} rv d{i%4}"><div class="pn">{a}</div><div class="pc">{b}</div>{NOW if n else SOON}</div>' for i, (a, b, n) in enumerate(plats))
    body = phero("console.webp", "Operators at a multi-screen security console", "Multi-System Integration", "One Building. One Security Picture.",
                 "Cameras, doors, alarms, fire, intercoms and entrances working together, so an event on one system gets the right response from all of them.", "Talk to an Integration Specialist") + f"""
<section class="sec"><div class="wrap center rv">
  <div class="eyebrow">The Problem We Solve</div>
  <h2 class="h2" style="max-width:900px;margin:0 auto">Most Buildings Run Five Security Systems That Never Talk to Each Other</h2>
  <p class="lede">Different installers, different apps, different passwords. When something happens, someone has to check each one by hand. We connect them so the systems do that work for you, and so our central station sees the whole picture when it matters.</p>
</div></section>
<section class="sec soft"><div class="wrap">
  {sec_head("System Map", "Everything Connected, Monitored Locally")}
  <div class="map rv"><svg viewBox="0 0 1160 680" role="img" aria-label="System map: unified security platform connected to video, card access, intrusion, fire alarm interface, Alarmco central station, mobile, elevator control, entrance control and intercom">
    {lines}
    <circle cx="580" cy="340" r="118" fill="#0b0b0c"/><circle class="orbit" cx="580" cy="340" r="130" fill="none" stroke="#D80016" stroke-width="2" stroke-dasharray="6 8"/>
    <text x="580" y="322" class="ct">Unified</text><text x="580" y="348" class="ct">security platform</text><text x="580" y="376" class="cs2">one login &#8226; one alarm list</text><text x="580" y="394" class="cs2">one map of the building</text>
    {boxes}
    <g class="node red"><rect x="622" y="543" width="210" height="64"/><text x="727" y="571" class="nt">Alarmco central station</text><text x="727" y="591" class="ns">UL-listed &#8226; 24/7 &#8226; Boise</text></g>
  </svg></div>
  <p class="note">* Coming soon. Unified platform shown as Genetec Security Center (coming soon); exacqVision with integrated access control is available today.</p>
  <div class="map-m">
    <div class="mm-core">Unified security platform<small>one login &#8226; one alarm list &#8226; one map</small></div>
    <div class="mm-grid">{''.join(f'<div><strong>{t}</strong><small>{s}</small></div>' for x, y, t, s in nodes)}</div>
    <div class="mm-cs">Alarmco central station<small>UL-listed &#8226; 24/7 &#8226; Boise</small></div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("What Integration Looks Like", "When This Happens, the System Does This")}
  <div class="grid g3">{sc}</div>
</div></section>
<section class="sec dark"><div class="wrap">
  {sec_head("Integration Platforms", "Built on Systems That Play Well Together", "Open platforms with published integrations, so your system is not tied to a single installer.")}
  <div class="grid g5 on-dark">{pl}</div>
</div></section>
{cta("Tired of Juggling Security Apps?", "We will map what you have today and show you how to bring it together, often without replacing it.", "Map My Systems")}"""
    return page("integration", "Multi-System Integration | Alarmco, Inc. (Concept)", "Video, access, intrusion, fire and intercom integrated and monitored from Boise by Alarmco.", body)

def monitoring():
    flow = [("Your building", "Alarm panel, fire panel, sprinkler switches and cameras"),
            ("Signal paths", "Phone line, AES radio, internet, cellular and GSM"),
            ("Boise central station", "UL-listed, local, staffed 24 hours a day"),
            ("Verify", "Video check and your call list, so real events get fast action"),
            ("Respond", "Police or fire dispatched, your people notified, event logged")]
    fl = "".join(f'<li class="rv d{i%5}"><span class="fn">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></li>' for i, (h, t) in enumerate(flow))
    plans = [
        ("Intrusion Alarm Monitoring", "Burglar alarm, panic and hold-up signals answered around the clock.", ["24/7 UL-listed central station in Boise", "Multiple communication paths so one cut line does not blind the system", "Open/close and event reports", "Call list and passcode management"], True),
        ("Fire &amp; Sprinkler Monitoring", "Alarm, supervisory and trouble signals from your fire alarm and sprinkler system.", ["Fire department dispatch on alarm", "Sprinkler valve and flow supervision", "Helps you keep code-required monitoring in place", "Pairs with our annual inspections"], True),
        ("Remote Guard Service (RGS)", "Live video monitoring as a cost-effective alternative to on-site guards.", ["Operators watch your cameras in real time", "Respond before a break-in becomes a loss", "Round-the-clock or after-hours coverage", "Works with the cameras we install"], True),
        ("Remote Management &amp; Alerts", "Full control of your security system from anywhere, at any time.", ["Real-time alerts to your phone", "Arm, disarm and check status remotely", "Comprehensive activity reporting", "Changes handled by our local team"], True),
        ("Managed Access Control", "We host and administer your card access so you do not need an in-house admin.", ["Add or remove badges on request", "Schedule and holiday changes", "Monthly who-went-where audit reports", "Lockdown support from the central station"], False),
        ("Camera &amp; System Health Checks", "We watch your equipment, not just your building.", ["Offline camera and recorder alerts", "Storage and recording failure detection", "Controller and panel trouble tracking", "A technician scheduled before you notice"], False),
    ]
    pl = "".join(plat(n, "Monthly plan &middot; ask for pricing", d, f, now, "Includes") for n, d, f, now in plans)
    body = phero("operator.webp", "Operator watching live camera feeds at a monitoring desk", "24/7 Monitoring", "24/7 Monitoring From Boise, Not a Call Center Three States Away",
                 "When your alarm goes off at 2 a.m., the person who answers is in Boise. Monthly monitoring for alarms, fire and sprinkler systems and live video, from Idaho's only local UL-listed central station.", "Get a Monitoring Quote") + f"""
<section class="stats"><div class="wrap grid g4">
  <div class="stat rv"><div class="sv">24/7</div><div class="sl">Staffed every hour of the year</div></div>
  <div class="stat rv d1"><div class="sv">UL</div><div class="sl">Listed central station</div></div>
  <div class="stat rv d2"><div class="sv">5</div><div class="sl">Signal paths supported</div></div>
  <div class="stat rv d3"><div class="sv" data-count="1994">1994</div><div class="sl">Monitoring Idaho since</div></div>
</div></section>
<section class="sec"><div class="wrap split">
  <div class="copy rv"><div><div class="eyebrow">Why Local Matters</div><h2 class="h2">The Difference Between a Response and a Ticket Number</h2></div>
    <p class="lede">Many monitoring providers answer signals from call centers outside Idaho. Ours are answered in Boise by operators who know the roads, the police and fire agencies, and your building.</p>
    {checks(["Idaho's only local UL-listed 24-hour central station", "Operators who know Treasure Valley agencies and addresses", "One company for installation, service and monitoring", "The same local team handles your system changes and repairs", "In many cases, existing panels can be switched over without replacing equipment"])}
  </div>
  <img class="rv d1" src="assets/img/ops-wall.webp" alt="Operators monitoring a wall of live screens" loading="lazy">
</div></section>
<section class="sec dark"><div class="wrap">
  {sec_head("How a Signal Is Handled", "From Your Building to a Response in Seconds")}
  <ol class="sflow">{fl}</ol>
  <div class="paths rv"><span class="pl">Signal paths we receive</span><span>POTS phone lines</span><span>AES radio</span><span>Internet</span><span>Cellular</span><span>GSM</span></div>
</div></section>
<section class="sec soft"><div class="wrap">
  {sec_head("Monthly Plans", "Monitoring Built Around Your Building", "Pick what you need, bundle what makes sense. Every plan is answered in Boise.")}
  <div class="grid g3 plans">{pl}</div>
  <p class="note">Plans marked Coming Soon are being added. Monthly pricing depends on the systems monitored; ask us for a quote.</p>
</div></section>
<section class="sec"><div class="wrap">
  {sec_head("Install + Monitor", "One Contract, One Call")}
  <div class="grid g3 why">
    <div class="rv"><h3>Designed to Be Monitored</h3><p>Cameras, doors and panels are programmed for monitoring from day one, not bolted on later.</p></div>
    <div class="rv d1"><h3>Fewer False Dispatches</h3><p>Video verification and a clean call list mean real events get the fastest possible response.</p></div>
    <div class="rv d2"><h3>Service Built In</h3><p>When the central station sees a trouble signal, the same company that installed it sends the technician.</p></div>
  </div>
</div></section>
{cta("Already Have a System? Let Boise Watch It.", "Tell us what you have. We will tell you what it takes to put it on local, UL-listed monitoring.", "Get a Monitoring Quote")}"""
    return page("monitoring", "24/7 Monitoring | Alarmco, Inc. (Concept)", "Monthly alarm, fire, sprinkler and video monitoring from Idaho's only local UL-listed central station in Boise.", body)

def build():
    if DIST.exists(): shutil.rmtree(DIST)
    shutil.copytree(SRC, DIST)
    for fn, html in [("index.html", index()), ("video-surveillance.html", cctv()), ("card-access.html", access()),
                     ("structured-cabling.html", cabling()), ("entrance-control.html", entrance()), ("integration.html", integration()), ("monitoring.html", monitoring())]:
        (DIST / fn).write_text(html, encoding="utf-8")
    (DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    (DIST / "_headers").write_text("/*\n  X-Robots-Tag: noindex, nofollow\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    print("built", sorted(p.name for p in DIST.iterdir()))

if __name__ == "__main__":
    build()
