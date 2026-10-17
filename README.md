# applycoding.github.io

Portfolio page for Arpan Bom: https://applycoding.github.io

Static HTML, no framework. Project data lives in `projects.py`; `repos.json` is a snapshot of `gh repo list applycoding --json name,description,primaryLanguage`.

```bash
python3 build.py   # regenerates index.html from template.html
```

Headshot: add `assets/headshot.jpg` and swap the `AB` placeholder in `template.html` (see the HTML comment).
