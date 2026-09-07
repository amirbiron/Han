#!/usr/bin/env python3
"""מייצר את docs/translation-status.md: מפה של מה תורגם לעברית ומה עוד לא.

הקובץ הזה הוא הדרך למצוא במהירות מסמך מתורגם בלי לפתוח תיקייה אחרי תיקייה,
והוא נוצר מהקוד ולא נכתב ביד, כדי שלא יתיישן ברגע שקובץ נוסף מתורגם.

ההיקף זהה לזה של check-translation-anchors.py, שממנו הוא מיובא, כדי שתהיה
הגדרה אחת בלבד למה נחשב משטח מתורגם.

  python3 scripts/translation-status.py           מייצר מחדש את הקובץ
  python3 scripts/translation-status.py --check   נכשל אם הקובץ לא מעודכן
"""

import importlib.util
import re
import sys
from pathlib import Path

HEBREW = re.compile(r"[֐-׿]")
OUTPUT = Path("docs/translation-status.md")

_spec = importlib.util.spec_from_file_location(
    "anchors", Path(__file__).parent / "check-translation-anchors.py"
)
_anchors = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_anchors)
in_scope = _anchors.in_scope


def prose_blocks(body):
    """פסקאות הפרוזה של הקובץ, בלי מה שלא אמור להיות מתורגם.

    כותרות ציטוט נושאות שם ספר באנגלית, שורות URL הן כתובת, ובלוקים מגודרים הם
    קוד. שלושתם נשארים באנגלית גם בקובץ מתורגם לגמרי, ולכן ספירתם הייתה מדרגת
    קובץ גמור כחלקי.
    """
    blocks, current, in_fence = [], [], False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not line.strip():
            if current:
                blocks.append("\n".join(current))
                current = []
            continue
        if re.match(r"^#{1,6}\s", line) or line.startswith("URL:"):
            continue
        current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


def hebrew_share(path):
    """אחוז פסקאות הפרוזה שכתובות בעברית, ומספר הפסקאות שנספרו.

    קוד בשורה, כתובות ויעדי קישור מוסרים לפני הספירה: כולם לטיניים בקובץ מתורגם.
    פסקה נספרת כאנגלית רק אם נשארו בה שמונה אותיות לטיניות לפחות, כדי ששורה של
    שם קובץ או של מונח בודד לא תיחשב פרוזה.
    """
    body = path.read_text(encoding="utf-8")
    hebrew = english = 0
    for block in prose_blocks(body):
        text = re.sub(r"`[^`]*`", "", block)
        text = re.sub(r"https?://\S+", "", text)
        text = re.sub(r"\]\([^)]*\)", "](", text)
        if HEBREW.search(text):
            hebrew += 1
        elif len(re.findall(r"[A-Za-z]", text)) >= 8:
            english += 1
    total = hebrew + english
    return (100 * hebrew / total if total else 100), total


ORDER = {"✅ מתורגם": 0, "🟡 חלקי": 1, "⬜ לא תורגם": 2}


def state(share):
    if share >= 95:
        return "✅ מתורגם"
    if share >= 5:
        return "🟡 חלקי"
    return "⬜ לא תורגם"


def area(path):
    parts = path.parts
    if len(parts) == 1:
        return "שורש הריפו"
    return parts[0]


def render():
    rows = []
    for md in sorted(Path(".").rglob("*.md")):
        if not in_scope(md) or md == OUTPUT:
            continue
        share, blocks = hebrew_share(md)
        rows.append((md, state(share), round(share), blocks))

    done = sum(1 for r in rows if r[1].startswith("✅"))
    partial = sum(1 for r in rows if r[1].startswith("🟡"))
    lines = [
        "# מפת התרגום",
        "",
        "איזה מסמך בריפו כבר קיים בעברית ואיזה עוד לא. הקובץ הזה נוצר על ידי",
        "`scripts/translation-status.py` ולא נכתב ביד, אז הוא תמיד משקף את מה שבדיסק.",
        "הרץ `python3 scripts/translation-status.py` אחרי שתרגמת קובץ, כדי לעדכן אותו.",
        "",
        f"**{done} מתוך {len(rows)} מסמכים מתורגמים**, {partial} חלקיים, "
        f"{len(rows) - done - partial} עוד לא התחילו.",
        "",
        "ההיקף הוא המשטחים שפונים לקורא אנושי: README-ים, `docs/` בשורש, ו-`{plugin}/docs/`.",
        "הגדרות סקילים וסוכנים (`SKILL.md`, `agents/`, `references/`) נשארות באנגלית בכוונה,",
        "מפני שתרגום שלהן משנה את המוצר עצמו ולא את התיעוד שלו.",
        "",
    ]
    for name in sorted({area(r[0]) for r in rows}, key=lambda a: (a != "שורש הריפו", a)):
        group = [r for r in rows if area(r[0]) == name]
        lines += [f"## {name}", ""]
        for path, status, _share, _blocks in sorted(group, key=lambda r: (ORDER[r[1]], r[0])):
            target = Path("..") / path if path.parts[0] != "docs" else Path(*path.parts[1:])
            lines.append(f"- {status} [`{path}`]({target.as_posix()})")
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def main():
    body = render()
    if "--check" in sys.argv:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != body:
            print("❌ docs/translation-status.md לא מעודכן. הרץ scripts/translation-status.py")
            return 1
        print("✅ מפת התרגום מעודכנת")
        return 0
    OUTPUT.write_text(body, encoding="utf-8")
    print(f"✅ נכתב {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
