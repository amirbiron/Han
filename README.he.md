# Han: לְמהנדס המוצר היחיד

[Read this document in English](./README.md)

<img src="images/han-banner.png">

Han היא חבילה של סקילים וסוכני AI למהנדסי מוצר שעובדים לבד (או בצוות קטן). היא מחברת תכנון מבוסס-ראיות, מימוש מונחה-בדיקות, תחזוקה מלאה של תיעוד, סקירת קוד לעומק וניתוח ארכיטקטוני לצוות של מומחים שאפשר לשגר מתוך Claude Code.

## מה הפלאגין הזה עושה

Han הופכת עבודת תכנון, מימוש, סקירה ותיעוד שבדרך כלל דורשת צוות שלם לאוסף של סקילים דטרמיניסטיים שאתה מריץ מתוך Claude Code.

כל סקיל משגר סוכנים מומחים, כמו מנהלי פרויקטים, סוקרים אדוורסריים, חוקרים, אנליסטים ארכיטקטוניים ומומחי בדיקות ואבטחה, שיעשו את העבודה שדורשת שיקול דעת. לאחר מכן הוא מקפל את הממצאים שלהם לתוצר שאפשר לסמוך עליו.

הסקילים תוכננו להתחבר זה לזה. אפשר לתכנן פיצ'ר, אחר כך לתכנן את המימוש שלו, אחר כך לעבור על התוכנית באיטרציות, אחר כך לבנות אותו בגישת test-first, אחר כך לסקור את הקוד שנוצר ואז לכתוב את תיאור ה-PR. הכול דרך סקילים בעלי שם שמעבירים שליטה זה לזה בצורה נקייה.

קרא את [Concepts](./docs/concepts.md) כדי להכיר את מודל הסקילים והסוכנים שעובר כחוט השני בכל הפלאגין.

## למהנדסי מוצר יחידים ולצוותים קטנים

Han נבנתה במכוון עבור מהנדסי מוצר יחידים וצוותים קטנים, ולא עבור צוותים גדולים או ארגונים גדולים. זה לא אומר שהיא לא יכולה לעבוד בצוותים גדולים יותר. קרא למה [המיקוד של Han הוא מהנדסי מוצר יחידים וצוותים קטנים](./docs/why-solo-and-small-teams.md) כדי להבין את המיצוב של Han ומה היא לא מביאה איתה.

## התקנה

### Claude Code

הוסף את ה-marketplace של Test Double ל-Claude Code, ואז התקן את הפלאגין:

```
/plugin marketplace add testdouble/han
/plugin install han@han
```

Han מגיעה כמספר פלאגינים:

| פלאגין               | סוג       | מה הוא מביא                                                                                                                                              |
| -------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`han`**            | הורה      | פלאגין ההורה שמביא את `han-communication`, `han-core`, `han-documentation`, `han-research`, `han-planning`, `han-coding`, `han-github` ו-`han-reporting` |
| `han-communication`  | מצורף     | הפלאגין היסודי שמתחת לכל האחרים: תקן הקריאוּת המשותף ופרופיל קול הכתיבה, יחד עם הסקילים והסוכן שמיישמים אותם                                             |
| `han-core`           | מצורף     | מערך הסוכנים המומחים המשותף, הסקיל project-discovery, מצב העבודה המשותף `/pairing` וקובצי הכללים הקנוניים                                                |
| `han-documentation`  | מצורף     | סקילים לתיעוד: תיעוד פרויקט, רשומות החלטה ארכיטקטונית ו-runbooks                                                                                         |
| `han-research`       | מצורף     | סקילים לעבודת ידע שלפני התכנון: מחקר, ניתוח פערים ומיון issues, יחד עם הסוכן research-analyst                                                            |
| `han-planning`       | מצורף     | סקילים לתכנון שאתה מגיע אליהם לפני המימוש                                                                                                                |
| `han-coding`         | מצורף     | סקילים לכתיבת קוד שאתה מגיע אליהם תוך כדי עבודה בקוד                                                                                                     |
| `han-github`         | מצורף     | סקילים מול GitHub, למשל פרסום סקירת קוד על PR                                                                                                            |
| `han-reporting`      | מצורף     | סקילים לדיווח, למשל סיכום לבעלי עניין                                                                                                                    |
| `han-feedback`       | אופציונלי | סקיל לאיסוף משוב אחרי סשן על ריצות של סקילים ב-Han                                                                                                       |
| `han-atlassian`      | אופציונלי | סקילים לפרסום מסמכים ופריטי עבודה למוצרי Atlassian                                                                                                       |
| `han-linear`         | אופציונלי | סקיל לפרסום פריטי עבודה ל-Linear (דורש שרת MCP של Linear)                                                                                                |
| `han-plugin-builder` | אופציונלי | נושא את ההנחיות והסקילים לבניית סקילים, סוכנים ופלאגינים משלך                                                                                            |

התקנה של `han@han` מושכת את החבילה המצורפת (המטא-פלאגין יחד עם `han-communication`, `han-core`, `han-documentation`, `han-research`, `han-planning`, `han-coding`, `han-github` ו-`han-reporting`), וזו הבחירה הנכונה לרוב האנשים. אם אתה רוצה רק פרוסה אחת מ-Han, התקן שכבה בודדת כמו `han-documentation@han` או `han-coding@han` (כל אחת מביאה איתה את הסוכנים המשותפים של `han-core`), והוסף פלאגינים ספציפיים נוספים לפי הצורך.

לתמונה המלאה ולמדריך מהיר של "איזה מהם אני צריך?", ראה [Choosing a Han plugin](./docs/choosing-a-han-plugin.md).

### Codex

הוסף את הריפו הזה כ-marketplace של Codex:

```
codex plugin marketplace add testdouble/han
```

Codex עדיין לא תומך במטא-פלאגינים כמו `han@han` (ראה openai/codex#23531), והוא לא מפענח תלויות, ולכן התקן את חבילות Han ישירות — החל מ-`han-communication` היסודי, שהחבילות שמייצרות טקסט תלויות בו:

```
codex plugin add han-communication@han
codex plugin add han-core@han
codex plugin add han-documentation@han
codex plugin add han-research@han
codex plugin add han-planning@han
codex plugin add han-coding@han
codex plugin add han-github@han
codex plugin add han-reporting@han
```

התקן את `han-feedback`, `han-atlassian`, `han-linear` או `han-plugin-builder` בנפרד כשאתה רוצה את החבילות האופציונליות האלה. מכיוון ש-Codex לא מפענח תלויות, התקן את `han-communication` לצד `han-atlassian` (הסקילים שמייצרים טקסט ועטופים בתוכו שואבים ממנו את תקן הקריאוּת המשותף).

## תיעוד

- [Concepts](./docs/concepts.md). סקיל מול סוכן, ואיך הם מתחברים. קריאה חד-פעמית לפני השימוש בפלאגין.
- [Plugin index](./docs/choosing-a-han-plugin.md). כל פלאגין עם שורת ריח וקישור ל-README שלו, החבילה המלאה מול שכבה בודדת, התלות של השכבות ב-`han-core` ומדריך מהיר לאיזה מהם להתקין.
- [Quickstart](./docs/quickstart.md). חמישה מסלולים לחמישה מצבים נפוצים. כל מסלול הוא רצף קצר של סקילים.
- [Skills index](./docs/skills/README.md). כל סקיל, לפי סדר אלפביתי, עם שורת ריח וקישור לתיעוד המורחב שלו.
- [Agents index](./docs/agents/README.md). כל סוכן, לפי סדר אלפביתי, עם שורת ריח וקישור לתיעוד המורחב שלו.
- [Workflows](./docs/workflows.md). המפה של אילו סקילים משתרשרים זה לזה, עם דיאגרמות זרימה לשרשראות המסתעפות.
- [Configuration](./docs/configuration.md). קובצי `.han/config.md` האופציונליים, אחד אישי ואחד לכל פרויקט, שקובעים תיקיית פלט בסיסית, גודל swarm ברירת מחדל, פרופיל קול כתיבה וסוכנים נוספים לסקילים של Han.
- [Sizing](./docs/sizing.md). מודל ה-small / medium / large שקובע כמה סוכנים הסקילים המשגרים swarm מפעילים.
- [YAGNI](./docs/yagni.md). כלל ה-"You Aren't Gonna Need It" מבוסס-הראיות שכל סקיל תכנון, סקירה וארכיטקטורה מיישם.
- [Evidence](./docs/evidence.md). מה נחשב ראיה ב-Han, איך לאפיין עד כמה היא חזקה, ומה לעשות כשאין ראיה בכלל.
- [Readability](./docs/readability.md). תקן הפלט המשותף שכל סקיל שפונה לקורא מיישם תוך כדי כתיבה, כך שהתוצר שמיועד לבני אדם פותח בעיקר ונקרא באופן עקבי בין הסקילים.
- [Changelog](./CHANGELOG.md). מה חדש בכל גרסה של הפלאגין.

### מדריכי How-To

- [How-to guides](./docs/how-to/README.md). מתכונים מקצה לקצה לתכנון פיצ'ר, לעדכון תוכנית אחרי שהבנייה כבר התחילה, להאצת ההבנה שלך בקוד לא מוכר, למיון וחקירה של באג, להרצת סקירת קוד אפקטיבית ולמחקר לקראת החלטה. בחר אחד כשאתה רוצה את ההליכה המלאה, ולא רק את המסלול.
- [How to provide feedback on Han](./docs/how-to/provide-feedback.md). שליחת משוב מובנה למתחזקים על ריצה של סקיל או סוכן.
- [Extend Han via dependencies](./docs/how-to/extend-han-with-plugin-dependencies.md). הוספת סקילים משלך מעל Han.
- [Build a plugin that depends on Han](./docs/how-to/build-a-plugin-that-depends-on-han.md). שחרור פלאגין שנשען על הסקילים והסוכנים של Han.

### תרומה ל-Han

- [Contributing](./CONTRIBUTING.md). הוספה או עריכה של סקילים, סוכנים ותיעוד.
- [Create a new skill](./docs/how-to/create-a-new-skill.md). בניית slash command חדש מאפס עם `/skill-builder`.
- [Create a new agent](./docs/how-to/create-a-new-agent.md). בניית סאב-סוכן חדש מאפס עם `/agent-builder`.

## תחזוקה ותמיכה

- **אופק תחזוקה:** מתוחזק ללא הגבלת זמן, במאמץ סביר. ללא SLA.
- **סוג הפרויקט:** פרויקט אישי, עם תמיכה מסוימת של Test Double
- **איך לדווח על תקלות:** דרך GitHub Issues, עם ציפייה למענה במאמץ סביר בתוך שבועיים.

Han היא מוצר קוד פתוח של [Test Double](https://testdouble.com), ומתוחזקת על ידי האנשים הבאים:

- [River Lynn Bailey](https://github.com/mxriverlynn): יוצר ומתחזק ראשי
- [Tamika Nomara](https://github.com/taminomara): תורם ליבה
- [Aaron Frerichs](https://github.com/afrerich): תורם ליבה
- [כל התורמים](https://github.com/testdouble/han/graphs/contributors): שונות, ומוערכים מאוד!

## הודעות משפטיות

Han היא מוצר קוד פתוח של [Test Double, Inc](https://testdouble.com), שפורסם במקור ב-[testdouble/han](https://github.com/testdouble/han). הריפו הזה נושא עותק של הפרויקט הזה, והקרדיט על העבודה המקורית שייך ל-Test Double ולתורמים שמופיעים למעלה.

Copyright 2026 [Test Double, Inc](https://testdouble.com). מופץ תחת [רישיון MIT](./LICENSE).

רישיון MIT מעניק לך את הזכות להשתמש ב-Han, להעתיק אותה, לשנות אותה ולהפיץ אותה מחדש, בתנאי אחד: הודעת זכויות היוצרים והודעת ההרשאה חייבות להישאר בכל עותק או חלק מהותי של התוכנה. בפועל זה אומר להשאיר את [LICENSE](./LICENSE) בריפו ללא שינוי, להשאיר את ההודעה הזו, ואם אתה מפיץ גרסה ששינית, להוסיף שורת זכויות יוצרים משלך לצד זו של Test Double ולא במקומה.
