# han-documentation

שכבת התיעוד של חבילת Han: הסקילים שאתה פונה אליהם כדי לכתוב מה הצוות בנה ומה הוא החליט. היא מתעדת פיצ'רים ומערכות, מתעדת החלטות ארכיטקטוניות ולוכדת נהלים תפעוליים, כל אחד מהם דרך תהליך מבוסס-ראיות שמסרב לכתוב תיעוד ספקולטיבי. פנה אליה כשקיים משהו אמיתי שהצוות צריך שיהיה כתוב.

**מצורף.** מותקן יחד עם המטא-פלאגין `han`. תלוי ב-`han-communication` וב-`han-core`.

**איך מתחילים:** תעד פיצ'ר או מערכת עם [`/project-documentation`](docs/skills/project-documentation.md), תעד החלטה עם [`/architectural-decision-record`](docs/skills/architectural-decision-record.md), ולכוד נוהל תפעולי עם [`/runbook`](docs/skills/runbook.md).

## סקילים

- [`/project-documentation`](docs/skills/project-documentation.md) — יוצר ומתחזק תיעוד לפיצ'רים, מערכות ורכיבים.
- [`/architectural-decision-record`](docs/skills/architectural-decision-record.md) — יוצר, מחלץ או ממיר רשומות החלטה ארכיטקטונית.
- [`/runbook`](docs/skills/runbook.md) — יוצר או מעדכן runbook לתרחיש תפעולי אחד, עם תבנית שמתחילה מהסימפטום ובדיקת YAGNI מקדימה שדורשת ראיות אמיתיות לפני הכתיבה.

הסקילים שלו משגרים סוכנים משותפים שיושבים ב-`han-core` (ובמקרה של readability-editor, ב-`han-communication`).

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין (או התקן את `han` כדי לקבל אותו כחלק מהחבילה המצורפת):

```
/plugin marketplace add testdouble/han
/plugin install han-documentation@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
