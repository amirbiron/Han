# han

`han` הוא המטא-פלאגין של חבילת Han. הוא לא כולל סקילים ולא סוכנים משלו. הוא קיים כדי למשוך את החבילה המצורפת בצעד אחד דרך התלויות שלו, כך שהתקנת `han` היא הדרך לבקש את כל מה שהחבילה מצרפת בבת אחת.

**החבילה המצורפת.** התקנת `han` מביאה את `han-communication`, `han-core`, `han-documentation`, `han-research`, `han-planning`, `han-coding`, `han-github` ו-`han-reporting` דרך התלויות שלו. היא לא מצרפת את הפלאגינים האופציונליים (`han-feedback`, `han-atlassian`, `han-linear` ו-`han-plugin-builder`); את כל אחד מהם מתקינים בנפרד.

```
/plugin marketplace add testdouble/han
/plugin install han@han
```

## לאן ממשיכים מכאן

- [אינדקס הפלאגינים](../docs/choosing-a-han-plugin.md). כל פלאגין, מה הוא עושה, ואיזה מהם להתקין.
- [Workflows](../docs/workflows.md). איך הסקילים בפלאגינים המצורפים משתרשרים זה לזה.
- [שורש הריפו](../README.md). דף הנחיתה של חבילת Han והתיאור המלא של מה ש-Han עושה.

## הרחבה של Han

אם אתה רוצה לבנות מעל Han או לשחרר משהו שתלוי בה, קרא את שני מדריכי ההרחבה:

- [Extend Han with plugin dependencies](../docs/how-to/extend-han-with-plugin-dependencies.md). איך Han משתמשת בתלויות בין פלאגינים כדי להרכיב את החבילה שלה עצמה.
- [Build a plugin that depends on Han](../docs/how-to/build-a-plugin-that-depends-on-han.md). איך להצהיר על Han כתלות של פלאגין משלך.
