#!/usr/bin/env python3
"""בודק שכל קישור עם עוגן (#) במשטחים המתורגמים מתפענח לכותרת אמיתית.

תרגום כותרת לעברית משנה את ה-slug שגיטהאב מייצר ממנה, ולכן שובר כל קישור
שמצביע לכותרת הזו, כולל קישורים מקבצים שלא נגעת בהם. הבדיקה הזו תופסת את זה.

ההיקף הוא בדיוק מה שמתורגם לפי docs/translation-glossary.md: README-ים,
docs/ בשורש, ו-{plugin}/docs/. תבניות תחת skills/ לא נכללות, כי הקישורים
שבהן מצביעים לתוצרים שנוצרים בזמן ריצה ולא לקבצים בריפו.
"""

import re
import sys
from pathlib import Path


def slug(heading):
    """מחשב את מזהה העוגן שגיטהאב מייצר מכותרת."""
    text = re.sub(r"[`*_]", "", heading).strip().lower()
    text = "".join(c for c in text if c.isalnum() or c in " -_")
    return text.replace(" ", "-")


def headings(path):
    try:
        body = path.read_text(encoding="utf-8")
    except OSError:
        return None
    found, in_fence = set(), False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^#{1,6}\s", line):
            found.add(slug(line.split(None, 1)[1]))
    return found


def in_scope(path):
    parts = path.parts
    if "node_modules" in parts or ".git" in parts:
        return False
    # קובצי markdown בשורש הריפו מקשרים לתוך docs/, אז שינוי כותרת שם שובר אותם.
    if len(parts) == 1:
        return True
    if path.name == "README.md":
        return True
    return "docs" in parts and "plans" not in parts and "research" not in parts


def main():
    broken = 0
    for md in sorted(Path(".").rglob("*.md")):
        if not in_scope(md):
            continue
        for match in re.finditer(r"\]\(([^)\s]*?)#([^)\s]+)\)", md.read_text(encoding="utf-8")):
            target, anchor = match.group(1), match.group(2)
            if target.startswith(("http://", "https://")):
                continue
            # תוצרים שסקיל מייצר בזמן ריצה, לא קבצים בריפו.
            if target.startswith("artifacts/"):
                continue
            available = headings((md.parent / target).resolve() if target else md)
            if available is None:
                print(f"❌ {md}: קובץ היעד לא קיים -> {target}")
                broken += 1
            elif anchor not in available:
                print(f"❌ {md}: עוגן שבור -> {target}#{anchor}")
                broken += 1
    print("✅ כל העוגנים במשטחים המתורגמים מתפענחים" if not broken else f"❌ {broken} עוגנים שבורים")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
