# han-planning

שכבת התכנון של חבילת Han: הסקילים שאתה פונה אליהם לפני המימוש. היא מגדירה מה פיצ'ר עושה, מתכננת איך לבנות אותו, מסדרת את הבנייה ברצף, מפרקת אותה לעבודה, ובוחנת תוכניות בלחץ לפני שאתה מתחייב, כל אחד מהם דרך תהליך מבוסס-ראיות שמשגר סוכנים מומחים לעבודה שדורשת שיקול דעת. פנה אליה כשיש לך בעיה לפתור ואתה רוצה תוכנית עמידה וסקורה לפני ששורת קוד אחת נכתבת.

**מצורף.** מותקן יחד עם המטא-פלאגין `han`. תלוי ב-`han-communication` וב-`han-core`.

**איך מתחילים:** הסקילים משתרשרים. הגדר עם [`/plan-a-feature`](docs/skills/plan-a-feature.md), תכנן את הבנייה עם [`/plan-implementation`](docs/skills/plan-implementation.md), סדר אותה ברצף עם [`/plan-a-phased-build`](docs/skills/plan-a-phased-build.md), ופרק אותה לעבודה עם [`/plan-work-items`](docs/skills/plan-work-items.md); בחן כל תוכנית בלחץ בכל שלב בדרך עם [`/iterative-plan-review`](docs/skills/iterative-plan-review.md).

## סקילים

- [`/plan-a-feature`](docs/skills/plan-a-feature.md) — בונה מפרט פיצ'ר מאפס דרך ראיון מבוסס-ראיות שעובר על עץ העיצוב ומשגר סוקרים מומחים.
- [`/plan-implementation`](docs/skills/plan-implementation.md) — הופך מפרט פיצ'ר לתוכנית מימוש דרך שיחת צוות מונחית.
- [`/plan-a-phased-build`](docs/skills/plan-a-phased-build.md) — מפצל גוף הקשר לרצף ממוספר של שלבי בנייה בפרוסות אנכיות, כשכל אחד מהם ניתן להדגמה עצמאית מול אדם אמיתי וכל אחד נבנה על קודמו.
- [`/plan-work-items`](docs/skills/plan-work-items.md) — מחלק תוכנית מימוש מהימנה לפריטי עבודה אטומיים שאפשר לתפוס באופן עצמאי, בקובץ פריטי עבודה אחד.
- [`/iterative-plan-review`](docs/skills/iterative-plan-review.md) — בוחן בלחץ תוכנית שכבר נכתבה, דרך מספר מעברי סקירה מעוגנים בבסיס הקוד.

## סוכנים

- [`discussion-facilitator`](docs/agents/discussion-facilitator.md) — מבקר דיון תכנון תוך כדי התרחשותו: מריץ את סבב הדוברים, מדרג כל טענה מול ראיות, ומתעד על מה הצוות עדיין לא ענה.

הסקילים שלו משגרים גם סוכנים משותפים שיושבים ב-`han-core` (ובמקרה של readability-editor, ב-`han-communication`).

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין (או התקן את `han` כדי לקבל אותו כחלק מהחבילה המצורפת):

```
/plugin marketplace add testdouble/han
/plugin install han-planning@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
