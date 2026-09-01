# han-atlassian

פלאגין Atlassian האופציונלי של חבילת Han. הוא מפרסם תוצרים של Han ל-Confluence ויוצר פריטי עבודה ב-Jira דרך שרת ה-MCP של Atlassian, ועוטף את סקילי התיעוד, התכנון והקוד של הליבה כך שהפלט שלהם ינחת ב-Atlassian אחרי שסקרת אותו. פנה אליו כשהמסמכים והכרטיסים של הצוות שלך חיים ב-Confluence וב-Jira.

**אופציונלי.** מותקן בנפרד, ולא מצורף למטא-פלאגין `han`. התקן אותו עם `/plugin install han-atlassian@han`. תלוי ב-`han-communication`, ב-`han-core`, ב-`han-documentation`, ב-`han-planning` וב-`han-coding` (סקילי העטיפה שלו מריצים סקילים מכל אחד מהם), ודורש שרת MCP של Atlassian מוגדר.

## סקילים

- [`/markdown-to-confluence`](docs/skills/markdown-to-confluence.md) — מפרסם קובץ Markdown מקומי אחד למיקום ב-Confluence שהמשתמש מציין, ויוצר דף חדש או מעדכן דף קיים; ברירת המחדל היא טיוטה לא מפורסמת.
- [`/project-documentation-to-confluence`](docs/skills/project-documentation-to-confluence.md) — מריץ `/project-documentation` כדי לכתוב תיעוד פיצ'ר, מציג אותו לסקירה, ואז מפרסם אותו למיקום ב-Confluence שהמשתמש מציין, אחרי אישור.
- [`/investigate-to-confluence`](docs/skills/investigate-to-confluence.md) — מריץ `/investigate` כדי לאתר את שורש הבאג (בלי לשנות קוד), מציג את הדוח לסקירה, ואז מפרסם אותו כדף Confluence אחד אחרי אישור.
- [`/code-overview-to-confluence`](docs/skills/code-overview-to-confluence.md) — מריץ `/code-overview` כדי לייצר סקירת-על בחשיפה הדרגתית (בלי לשנות קוד), מציג אותה לסקירה, ואז מפרסם אותה כדף Confluence אחד אחרי אישור.
- [`/plan-a-feature-to-confluence`](docs/skills/plan-a-feature-to-confluence.md) — מריץ `/plan-a-feature` כדי לבנות מפרט פיצ'ר, מציג אותו לסקירה, ואז מפרסם את המפרט ואת התוצרים הנלווים אליו כעץ דפים ב-Confluence אחרי אישור.
- [`/work-items-to-jira`](docs/skills/work-items-to-jira.md) — יוצר כרטיס Jira אחד לכל פרוסה מתוך קובץ פריטי עבודה של `/plan-work-items`, בפרויקט יעד אחד; האח של `/work-items-to-issues` בצד של Jira.

הסקילים שלו משגרים סוכנים משותפים שיושבים ב-`han-core` (ובמקרה של readability-editor, ב-`han-communication`).

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין:

```
/plugin marketplace add testdouble/han
/plugin install han-atlassian@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
