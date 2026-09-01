# han-feedback

פלאגין המשוב האופציונלי של חבילת Han. הוא לוכד תצפיות מובנות על הסקילים והסוכנים של Han שבהם השתמשת זה עתה, כך שהמתחזקים ישמעו מה עבד ומה לא. פנה אליו בסוף סשן כשאתה רוצה לדווח בחזרה איך החבילה עובדת עבורך.

**אופציונלי.** מותקן בנפרד, ולא מצורף למטא-פלאגין `han`. התקן אותו עם `/plugin install han-feedback@han`. לא תלוי בשום פלאגין אחר של Han.

## סקילים

- [`/han-feedback`](docs/skills/han-feedback.md) — לוכד משוב מובנה אחרי סשן על הסקילים והסוכנים של Han שבהם השתמשת, לרוחב כל משפחת הפלאגינים `han-*`, ואופציונלית מפרסם אותו כ-issue ב-GitHub אצל testdouble/han.

## התקנה

הוסף את ה-marketplace ל-Claude Code, ואז התקן את הפלאגין:

```
/plugin marketplace add testdouble/han
/plugin install han-feedback@han
```

---

[אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md) · [שורש הריפו](../README.md) · [Workflows](../docs/workflows.md)
