# han-github

שכבת ה-GitHub של חבילת Han: הסקילים שמדברים עם GitHub דרך ה-CLI‏ `gh`. היא מפרסמת סקירת קוד על pull request, כותבת תיאור PR מתוך השינויים בענף, ומפרסמת קובץ פריטי עבודה כ-issues ב-GitHub. פנה אליה כשאתה רוצה שהפלט של Han ינחת ב-GitHub במקום להישאר מקומי.

**מצורף.** מותקן יחד עם המטא-פלאגין `han`. תלוי ב-`han-communication`, ב-`han-core` וב-`han-coding` (הסקיל post-code-review-to-pr עוטף את code-review של han-coding). דורש את ה-CLI‏ `gh`.

## סקילים

- [`/post-code-review-to-pr`](docs/skills/post-code-review-to-pr.md) — מריץ `/code-review` מול PR ב-GitHub ומפרסם את הסקירה כתגובות, אחרי בדיקת בהירות על גוף הסקירה שנוסח.
- [`/update-pr-description`](docs/skills/update-pr-description.md) — מייצר תיאור PR מתוך השינויים בענף הנוכחי, בהתאם לתבנית ה-PR של הריפו כשקיימת כזו.
- [`/work-items-to-issues`](docs/skills/work-items-to-issues.md) — מפרסם כל פריט בקובץ פריטי עבודה של `/plan-work-items` כ-issue ב-GitHub בריפו היעד שלו, עם קישור לחוסמים שבתוך אותו ריפו.

הסקילים שלו משגרים סוכנים משותפים שיושבים ב-`han-core` (ובמקרה של readability-editor, ב-`han-communication`).

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין (או התקן את `han` כדי לקבל אותו כחלק מהחבילה המצורפת):

```
/plugin marketplace add testdouble/han
/plugin install han-github@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
