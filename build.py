"""Builds index.html from projects.py and repos.json (gh repo list --json name,description)."""
import html, json
from projects import FLAGSHIP, GROUPS, LIVE, DESC
repos = {r["name"]: r for r in json.load(open("repos.json"))}
GH = "https://github.com/applycoding/"
def desc(n):
    d = (repos.get(n, {}).get("description") or "").strip()
    return d or DESC.get(n, "")
def lang(n):
    l = repos.get(n, {}).get("primaryLanguage") or {}
    return l.get("name", "") if isinstance(l, dict) else ""
def card(n, d, live=None):
    live = live or LIVE.get(n)
    links = f'<a href="{GH}{n}">Code</a>' + (f' <a class="live" href="{live}">Live demo</a>' if live else "")
    lg = lang(n)
    return (f'<article class="card"><h4>{html.escape(n)}</h4><p>{html.escape(d)}</p>'
            f'<div class="meta">{"<span>"+html.escape(lg)+"</span>" if lg else ""}{links}</div></article>')
flag = "".join(card(n, d, l) for n, d, l in FLAGSHIP)
groups = ""
for g, names in GROUPS.items():
    gid = g.split()[0].lower().strip(",")
    groups += f'<section id="{gid}"><h3>{html.escape(g)} <small>{len(names)}</small></h3><div class="grid">' + "".join(card(n, desc(n)) for n in names) + "</div></section>"
nav = "".join(f'<a href="#{g.split()[0].lower().strip(",")}">{html.escape(g)}</a>' for g in GROUPS)
page = open("template.html").read().replace("{{FLAGSHIP}}", flag).replace("{{GROUPS}}", groups).replace("{{NAV}}", nav)
open("index.html", "w").write(page)
print("built index.html with", sum(len(v) for v in GROUPS.values()) + len(FLAGSHIP), "projects")
