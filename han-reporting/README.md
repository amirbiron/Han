# han-reporting

שכבת הדיווח של חבילת Han: הסקילים שהופכים את העבודה בחזרה למשהו שאפשר לשתף עם בעלי עניין לא-טכניים. היא ממירה מפרט פיצ'ר לסיכום בשפה פשוטה לבעלי עניין, עם דיאגרמות, ואחר כך לדוח מנהלים אחד ב-HTML שעומד בפני עצמו. פנה אליה כשאתה צריך הסכמה או משוב מאנשים שלא יקראו את המפרט.

**מצורף.** מותקן יחד עם המטא-פלאגין `han`. תלוי ב-`han-communication`.

**איך מתחילים:** הסקילים משתרשרים. הרץ [`/stakeholder-summary`](docs/skills/stakeholder-summary.md) כדי לייצר את הסיכום, ואז [`/html-summary`](docs/skills/html-summary.md) כדי להפוך את הסיכום לדוח HTML שאפשר לשתף.

## סקילים

- [`/stakeholder-summary`](docs/skills/stakeholder-summary.md) — הופך מפרט פיצ'ר לסיכום בשפה פשוטה לבעלי עניין, עם דיאגרמות Mermaid לחוויית המשתמש ולזרימת הנתונים, לצורך משוב לפני המימוש.
- [`/html-summary`](docs/skills/html-summary.md) — ממיר `stakeholder-summary.md` לדוח מנהלים אחד ב-HTML שעומד בפני עצמו, עם השורה התחתונה והבקשות בראש; מייצר את הקובץ בלבד, לא מפרסם אותו.

הסקילים שלו שואבים את תקן הקריאוּת המשותף מ-`han-communication` ומשגרים את סוכן ה-readability-editor שלו.

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין (או התקן את `han` כדי לקבל אותו כחלק מהחבילה המצורפת):

```
/plugin marketplace add testdouble/han
/plugin install han-reporting@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
