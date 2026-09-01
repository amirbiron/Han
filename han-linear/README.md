# han-linear

פלאגין Linear האופציונלי של חבילת Han. הוא מפרסם פריטי עבודה של Han ל-Linear דרך שרת ה-MCP של Linear, ומאתר את המצבים, התוויות, ה-Projects והחברים האמיתיים של הצוות לפני שהוא יוצר משהו. פנה אליו כשהתוכנית שלך כבר פורקה לפריטי עבודה ואתה עוקב אחרי העבודה הזו ב-Linear.

**אופציונלי.** מותקן בנפרד, ולא מצורף למטא-פלאגין `han`. התקן אותו עם `/plugin install han-linear@han`. לא תלוי בשום פלאגין אחר של Han ודורש שרת MCP של Linear מוגדר.

## סקילים

- [`/work-items-to-linear`](docs/skills/work-items-to-linear.md) — יוצר issue אחד ב-Linear לכל פרוסה מתוך קובץ פריטי עבודה של `/plan-work-items`, בצוות יעד אחד, מאתר את מצבי ה-workflow, התוויות, ה-Projects והחברים האמיתיים של הצוות, ומקשר תלויות שבתוך הקובץ כיחסי "blocked by" מקוריים.

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין:

```
/plugin marketplace add testdouble/han
/plugin install han-linear@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
