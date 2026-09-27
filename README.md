# Alarmco Technology Solutions — concept site

Concept pages prepared by Justin Whitton for Alarmco, Inc., live at **https://alarmco.jwhitton.com**.

One responsive build serves desktop and phone. Six pages: the Technology Solutions landing page (animated live site view + interactive system explorer), Video Surveillance, Card Access, Structured Cabling, Entrance Control, and Multi-System Integration.

- `src/` — `assets/site.css`, `assets/site.js`, `assets/img/` (Alarmco's existing site photography and logo)
- `build.py` — generates the pages into `dist/` (`python build.py`, no dependencies)
- Deploys automatically to GitHub Pages on every push to `main` (`.github/workflows/pages.yml`)

Every page is `noindex` and carries a "concept preview" banner so it is never mistaken for the official alarmcoinc.com.
