#!/usr/bin/env python3
"""Generate the docs/ site sources from README.md (the single source of truth).

README.md is split into pages, GitHub alerts become MkDocs admonitions,
<details> blocks become collapsible admonitions and internal #anchors are
rewritten to point at the right page.  Run from the repository root:

    python scripts/build_docs.py && mkdocs build --strict
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"

# page file -> (nav title, difficulty, [H2 heading prefixes to include])
PAGES = [
    ("preparation.md", "Preparation & SD Card", "🟢 Beginner", ["🛠️ Phase 1", "💾 SD Card"]),
    ("setup.md", "Software & ES-DE Setup", "🟢 Beginner", ["🍳 Phase 2", "📂 Phase 3", "🎨 Phase 4"]),
    ("emulators.md", "Emulator Configuration", "🟡 Intermediate", ["⚙️ Phase 5", "🔧 Community Contribution"]),
    ("scraping.md", "ES-DE Advanced & Scraping", "🟡 Intermediate", ["🎨 Phase 6"]),
    ("optimization.md", "Optimization & Profiles", "🟡 – 🟠", ["⚡ Phase 7:", "🚀 Phase 7.5"]),
    ("dark-arts.md", "The Dark Arts (Debloat)", "🔴 Expert", ["🥷 Phase 8", "🧹 Additional"]),
    ("overlays.md", "Removing Touch Overlays", "🟢 Beginner", ["📱 Phase 9"]),
    ("gammaos.md", "GammaOS", "🔴 Expert", ["🚀 Phase 10"]),
    ("games.md", "Must-Play Games", "🟢 Beginner", ["📜 Appendix"]),
    ("about.md", "About, Disclaimer & Credits", "—", ["🤖 About", "⚠️ Disclaimer", "🤝 Community"]),
]

ICONS = {"preparation.md": "🛠️", "setup.md": "🍳", "emulators.md": "⚙️", "scraping.md": "🎨",
         "optimization.md": "⚡", "dark-arts.md": "🥷", "overlays.md": "📱", "gammaos.md": "🚀", "games.md": "📜"}
BLURBS = {
    "preparation.md": "What you need, SD card format and mount, button naming.",
    "setup.md": "Updates, virtual memory, downloads, ROM library and ES-DE folders.",
    "emulators.md": "RetroArch, Dolphin, NetherSX2, PPSSPP, Duckstation, Azahar and more.",
    "scraping.md": "Themes, metadata and artwork scraping for ES-DE.",
    "optimization.md": "Developer tweaks, battery health, fan curve and audio EQ.",
    "dark-arts.md": "Debloat with Shizuku and Termux, Play Services hardening.",
    "overlays.md": "Remove the touch overlays and speed up ES-DE startup.",
    "gammaos.md": "Alternative OS: benefits, risks and how to flash it.",
    "games.md": "Curated must-play games per system with performance tiers.",
}

ALERTS = {"NOTE": "note", "TIP": "tip", "WARNING": "warning", "CAUTION": "danger",
          "IMPORTANT": "info", "SOURCE": "quote"}


def gh_slug(title: str) -> str:
    t = re.sub(r"[^\w\- ]", "", title.lower(), flags=re.UNICODE)
    return t.strip().replace(" ", "-")


def split_sections(lines):
    """Yield (h2_title, [lines]) skipping fenced code when looking for headings."""
    sections, cur, fence = [], None, False
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence
        m = re.match(r"^## (.+)$", ln) if not fence else None
        if m:
            cur = [m.group(1), []]
            sections.append(cur)
        elif cur is not None:
            cur[1].append(ln)
    return sections


LIST_RE = re.compile(r"^\s*([*+-]|\d+\.)\s")


def fix_lists(text):
    """Python-Markdown needs a blank line before a list and 4-space nesting; GitHub does not."""
    out, fence, prev = [], False, ""
    for ln in text.split("\n"):
        body = ln.lstrip()
        if body.startswith("```"):
            fence = not fence
        if not fence and LIST_RE.match(ln):
            indent = len(ln) - len(body)
            if indent and indent % 4:  # normalise 2/3-space nesting to 4
                ln = " " * (4 * ((indent + 1) // 2 if indent < 4 else indent // 4 + 1)) + body
            plain_prev = prev.strip() and not LIST_RE.match(prev) and not prev.startswith((" ", "\t", ">", "|", "!!!", "???"))
            if plain_prev:
                out.append("")
        out.append(ln)
        prev = ln
    return "\n".join(out)


def convert_alerts(lines):
    out, i = [], 0
    while i < len(lines):
        m = re.match(r"^> \[!(\w+)\]\s*$", lines[i])
        if not m:
            out.append(lines[i]); i += 1; continue
        kind = m.group(1)
        title = ' "Source"' if kind == "SOURCE" else ""
        out.append(f"!!! {ALERTS.get(kind, 'note')}{title}")
        i += 1
        body = []
        while i < len(lines) and lines[i].startswith(">"):
            body.append(re.sub(r"^> ?", "", lines[i]))
            i += 1
        for b in fix_lists("\n".join(body)).split("\n"):
            out.append("    " + b if b.strip() else "")
    return out


def convert_details(text):
    def repl(m):
        title = re.sub(r"</?b>", "", m.group(1)).strip()
        body = "\n".join(("    " + l if l.strip() else "") for l in m.group(2).strip("\n").splitlines())
        return f'??? abstract "{title}"\n\n{body}\n'
    return re.sub(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>", repl, text, flags=re.S)


def main():
    lines = (ROOT / "README.md").read_text(encoding="utf-8").splitlines()
    sections = split_sections(lines)
    by_prefix = {}
    for title, body in sections:
        by_prefix[title] = body

    # heading -> page map (all H2-H4 outside fences)
    anchor_page, page_bodies = {}, {}
    for fname, _t, _d, prefixes in PAGES:
        chunks = []
        for pfx in prefixes:
            match = [t for t in by_prefix if t.startswith(pfx)]
            assert len(match) == 1, f"prefix {pfx!r} matched {match}"
            chunks.append((match[0], by_prefix[match[0]]))
        page_bodies[fname] = chunks
        for title, body in chunks:
            slugs = [(title, gh_slug(title))]
            fence = False
            for ln in body:
                if ln.startswith("```"):
                    fence = not fence
                m = re.match(r"^#{3,4} (.+)$", ln) if not fence else None
                if m:
                    slugs.append((m.group(1), gh_slug(m.group(1))))
            for _, s in slugs:
                anchor_page.setdefault(s, fname)

    def fix_links(text):
        def repl(m):
            slug = m.group(1)
            page = anchor_page.get(slug)
            return f"]({page}#{slug})" if page else m.group(0)
        return re.sub(r"\]\(#([^)]+)\)", repl, text)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "docs_src", OUT, dirs_exist_ok=True)

    def add_ids(body_lines):
        res, fence = [], False
        for ln in body_lines:
            if ln.startswith("```"):
                fence = not fence
            m = re.match(r"^(#{3,4}) (.+)$", ln) if not fence else None
            res.append(f"{m.group(1)} {m.group(2)} {{ #{gh_slug(m.group(2))} }}" if m else ln)
        return res

    for fname, title, diff, _p in PAGES:
        parts = []
        for n, (h2, body) in enumerate(page_bodies[fname]):
            level = "#" if n == 0 else "##"
            parts.append(f"{level} {h2} {{ #{gh_slug(h2)} }}\n")
            b = convert_alerts(add_ids(body))
            parts.append("\n".join(b))
        text = "\n".join(parts)
        text = convert_details(text)
        text = text.replace('<div align="center">', '<div style="text-align:center" markdown>')
        text = re.sub(r"\n---\s*\n", "\n\n", text)  # rules between sections are redundant in pages
        text = fix_links(text)
        text = fix_lists(text)
        (OUT / fname).write_text(text.rstrip() + "\n", encoding="utf-8")

    # home page: template + generated cards
    cards = "\n\n".join(
        f"-   **[{ICONS[f]} {t}]({f})**\n\n    ---\n\n    {BLURBS[f]}\n\n    {d}"
        for f, t, d, _ in PAGES if f != "about.md"
    )
    home = (ROOT / "docs_src" / "index.md").read_text(encoding="utf-8").replace("{{CARDS}}", cards)
    (OUT / "index.md").write_text(home, encoding="utf-8")
    print(f"Generated {len(PAGES) + 1} pages in {OUT}")


if __name__ == "__main__":
    main()
