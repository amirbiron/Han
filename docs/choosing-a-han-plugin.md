# אינדקס הפלאגינים: בחירת פלאגין של Han

_זהו אינדקס הפלאגינים של חבילת Han: כל פלאגין עם שורת ריח וקישור ל-README שלו, ובנוסף החלטת ההתקנה במקום אחד. לקטלוג לפי סקיל ראה את [אינדקס הסקילים](./skills/README.md); לאיך הסקילים משתרשרים ראה [Workflows](./workflows.md)._

_קהל: כל מי שעומד להתקין את Han. זמן קריאה: כשתי דקות. תוצאה: להתקין את הפלאגין הנכון בניסיון הראשון, ולדעת בדיוק מה קיבלת._

> ראה גם: [שורש הריפו](../README.md) · [אינדקס הסקילים](./skills/README.md) · [אינדקס הסוכנים](./agents/README.md) · [Workflows](./workflows.md) · [מושגי יסוד](./concepts.md) · [Quickstart](./quickstart.md)

> **התשובה הקצרה.** התקן את החבילה המצורפת עם `/plugin install han@han`. זה נותן לך את כל מה שהמטא-פלאגין מצרף: סקילי התקשורת, כל הסוכנים, סקילי התיעוד, סקילי המחקר שלפני התכנון, סקילי התכנון, סקילי הקוד, סקילי ה-GitHub וסקילי הדיווח.
>
> בחר פלאגין של שכבה בודדת (כמו `han-documentation` או `han-coding`) רק כשאתה יודע שאתה רוצה בדיוק את הפרוסה הזו; הוא מביא איתו את מערך הסוכנים של `han-core`. אין דרך להתקין שכבה בלי הסוכנים המשותפים, מפני שפלאגיני השכבות תלויים בפלאגין הליבה ומביאים אותו איתם.
>
> חלק מהפלאגינים יושבים מחוץ לחבילה. התקן את `han-feedback` בנפרד כדי לשלוח משוב, את `han-atlassian` כדי לפרסם ל-Confluence או ל-Jira, את `han-linear` כדי לפרסם פריטי עבודה ל-Linear, או את `han-plugin-builder` להנחיות על בניית סקילים, סוכנים ופלאגינים משלך.

יתר הדף מפרט את הפלאגינים, מסביר את התלות האחת שמפתיעה אנשים, ועוזר לך לבחור.

## הפלאגינים

Han מגיעה כמשפחת פלאגינים ב-marketplace אחד. כל רשומה מקשרת ל-README של אותו פלאגין, שהוא הבעלים של התיאור המלא של מה שהוא עושה. המטא-פלאגין `han` הוא עטיפת נוחות שמצרפת את שמונת הראשונים.

- **[`han-communication`](../han-communication/README.md).** הפלאגין היסודי שמתחת לכל האחרים. בעלים של תקן הקריאוּת הקנוני ושל תקן ההסבר לדיבור עם מי שלא הולך לממש את העבודה, יחד עם הסקילים והסוכן שמיישמים אותם ועם סגנונות הפלט `Han Readability` ו-`Han Concise` שמחילים את תקן הקריאוּת על סשן שלם. מצורף; לא תלוי בכלום.
- **[`han-core`](../han-core/README.md).** הבסיס המשותף: מערך הסוכנים המומחים שהפלאגינים האחרים משגרים, הסקיל project-discovery, קובצי הכללים הקנוניים, ומצב העבודה `/pairing` שבונה כל סוג של עבודה בחתיכות שאפשר לסקור. מצורף; לא תלוי בשום פלאגין אחר של Han.
- **[`han-documentation`](../han-documentation/README.md).** שכבת התיעוד: מסמכי פיצ'רים ומערכות, רשומות החלטה ארכיטקטונית, ו-runbooks. מצורף; תלוי ב-`han-communication` וב-`han-core`.
- **[`han-research`](../han-research/README.md).** שכבת עבודת הידע שלפני התכנון: מחקר פתוח, ניתוח פערים ומיון issues, ובנוסף הסוכן research-analyst. מצורף; תלוי ב-`han-communication` וב-`han-core`.
- **[`han-planning`](../han-planning/README.md).** שכבת התכנון: הגדרה, תכנון, סידור ברצף, פירוק ובחינה בלחץ של עבודה לפני המימוש, ובנוסף הסוכן discussion-facilitator. מצורף; תלוי ב-`han-communication` וב-`han-core`.
- **[`han-coding`](../han-coding/README.md).** שכבת הקוד: כתיבה, סקירה, ניתוח, בדיקה, חקירה ותקנון של קוד. מצורף; תלוי ב-`han-communication` וב-`han-core`.
- **[`han-github`](../han-github/README.md).** שכבת ה-GitHub: פרסום סקירות, כתיבת תיאורי PR, ופרסום פריטי עבודה כ-issues דרך ה-CLI‏ `gh`. מצורף; תלוי ב-`han-communication`, ב-`han-core` וב-`han-coding`.
- **[`han-reporting`](../han-reporting/README.md).** שכבת הדיווח: הפיכת מפרט לסיכום בשפה פשוטה לבעלי עניין ולדוח HTML שאפשר לשתף. מצורף; תלוי ב-`han-communication`.
- **[`han-feedback`](../han-feedback/README.md).** שכבת המשוב האופציונלית: משוב מובנה אחרי סשן על סקילי Han שהרצת. אופציונלי; לא תלוי בשום פלאגין אחר של Han.
- **[`han-atlassian`](../han-atlassian/README.md).** שכבת Atlassian האופציונלית: פרסום תוצרים של Han ל-Confluence ויצירת פריטי עבודה ב-Jira. אופציונלי; תלוי ב-`han-communication`, ב-`han-core`, ב-`han-documentation`, ב-`han-planning` וב-`han-coding`; דורש שרת MCP של Atlassian.
- **[`han-linear`](../han-linear/README.md).** שכבת Linear האופציונלית: יצירת issue אחד ב-Linear לכל פרוסת פריט עבודה. אופציונלי; לא תלוי בשום פלאגין אחר של Han; דורש שרת MCP של Linear.
- **[`han-plugin-builder`](../han-plugin-builder/README.md).** שכבת בניית הפלאגינים האופציונלית: הנחיות החיבור ושני בונים מונחי-ראיון לסקילים ולסוכנים חדשים. אופציונלי; לא תלוי בכלום.
- **[`han`](../han/README.md).** המטא-פלאגין בלי רכיבים משלו. הוא מצרף את `han-communication`, `han-core`, `han-documentation`, `han-research`, `han-planning`, `han-coding`, `han-github` ו-`han-reporting`. התקנה שלו היא הדרך לבקש את החבילה המצורפת בפקודה אחת. הוא לא מצרף את `han-feedback`, `han-atlassian`, `han-linear` או `han-plugin-builder`.

## הדבר האחד שמפתיע אנשים

`han-documentation` נושא רק את סקילי התיעוד, `han-research` רק את סקילי המחקר שלפני התכנון, `han-planning` רק את סקילי התכנון, `han-coding` רק את סקילי הקוד, ו-`han-github` רק את סקילי ה-GitHub. אז אולי תצפה שהתקנה של אחד מהם תיתן לך את הפרוסה הזו של Han ותו לא. אף אחד מהם לא עובד ככה.

`han-documentation`, `han-research`, `han-planning`, `han-coding` ו-`han-github` תלויים כולם ב-`han-core`, מפני שהסקילים שלהם משגרים את הסוכנים המומחים המשותפים שיושבים שם, וב-`han-communication`, מפני שהסקילים שלהם מייצרים טקסט ושואבים ממנו את תקן הקריאוּת. כשאתה מתקין פלאגין שמצהיר על תלות, Claude Code מפענח ומתקין את התלות עבורך אוטומטית ואומר לך מה הוא הוסיף. לכן התקנה של כל אחד מהם מתקינה את שניהם לצידו, ואתה מקבל את מערך הסוכנים המשותף, את גילוי הפרויקט, את מצב העבודה pairing ואת תקן הקריאוּת כך או כך. (`han-reporting` הוא היוצא מן הכלל: הוא תלוי ב-`han-communication` בלבד.)

זה אומר ש**כל התקנה של שכבה מגיעה עם הסוכנים המשותפים.** הבחירה האמיתית מסתכמת ב:

- **שכבה בתוספת היסודות** (למשל `han-documentation` או `han-coding`): הסקילים של אותה שכבה, בתוספת מערך הסוכנים המשותף, גילוי הפרויקט ומצב העבודה pairing מ-`han-core`, ותקן הקריאוּת מ-`han-communication`.
- **החבילה המצורפת** (`han`): כל השכבות בבת אחת.

הפלאגינים האופציונליים (`han-feedback`, `han-atlassian`, `han-linear`, `han-plugin-builder`) יושבים מחוץ לבחירה הזו. המטא-פלאגין במכוון לא מצרף אותם, ולכן לא `han` ולא אף שכבה מביאים אותם; התקן כל אחד בנפרד. `han-atlassian` דורש שרת MCP של Atlassian מוגדר ו-`han-linear` שרת MCP של Linear מוגדר.

## איזה מהם אתה צריך?

מצא את השורה שמתאימה לך והרץ את הפקודה שבה. התחל באפשרות המומלצת אלא אם יש לך סיבה שלא.

| המצב שלך                                                                             | להתקין                                                            | פקודה                                    |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ---------------------------------------- |
| אתה רוצה הכול, או שאתה עדיין לא בטוח                                                 | **`han` (התחל כאן)**                                              | `/plugin install han@han`                |
| אתה רוצה לכתוב קוד test-first עם `/tdd`                                              | `han` (החבילה המצורפת כוללת את סקילי הקוד)                        | `/plugin install han@han`                |
| אתה עובד מול GitHub מתוך Claude Code (סקירת PRs, כתיבת תיאורי PR, פרסום פריטי עבודה) | `han` (החבילה המצורפת כוללת את סקילי ה-GitHub)                    | `/plugin install han@han`                |
| אתה רוצה רק את סקילי התיעוד (מסמכי פרויקט, ADRs, runbooks)                           | `han-documentation` (מביא איתו את הסוכנים של `han-core`)          | `/plugin install han-documentation@han`  |
| אתה רוצה רק את סקילי המחקר שלפני התכנון (מחקר, ניתוח פערים, מיון issues)             | `han-research` (מביא איתו את הסוכנים של `han-core`)               | `/plugin install han-research@han`       |
| אתה רוצה את הסוכנים המשותפים, את גילוי הפרויקט ואת מצב העבודה pairing                | `han-core`                                                        | `/plugin install han-core@han`           |
| התקנת שכבה בודדת ועכשיו אתה רוצה את סקילי התכנון                                     | `han-planning` (לצד מה שכבר יש לך)                                | `/plugin install han-planning@han`       |
| התקנת שכבה בודדת ועכשיו אתה רוצה את סקילי הקוד                                       | `han-coding` (לצד מה שכבר יש לך)                                  | `/plugin install han-coding@han`         |
| אתה רוצה לשלוח למתחזקים משוב אחרי סשן על סקילי Han                                   | `han-feedback` (לצד כל מה שכבר יש לך)                             | `/plugin install han-feedback@han`       |
| אתה רוצה לפרסם תיעוד או תוכניות פיצ'ר של Han ל-Confluence, או פריטי עבודה ל-Jira     | `han-atlassian` (לצד כל מה שכבר יש לך; דורש שרת MCP של Atlassian) | `/plugin install han-atlassian@han`      |
| אתה רוצה לפרסם פריטי עבודה של Han ל-Linear                                           | `han-linear` (לצד כל מה שכבר יש לך; דורש שרת MCP של Linear)       | `/plugin install han-linear@han`         |
| אתה בונה סקילים, סוכנים או פלאגינים משלך ורוצה את הנחיות החיבור                      | `han-plugin-builder` (בנפרד, או לצד כל מה שכבר יש לך)             | `/plugin install han-plugin-builder@han` |

החבילה המצורפת `han` היא ברירת המחדל הנכונה כמעט לכולם. שכבה בודדת היא הבחירה המכוונת של מי שיודע שהוא רוצה בדיוק את הפרוסה הזו של Han בתוספת הסוכנים המשותפים.

## התקנה

קודם הוסף את ה-marketplace, ואז התקן את הפלאגין שבחרת:

```
/plugin marketplace add testdouble/han
/plugin install han@han
```

החלף את הפקודה השנייה ב-`han-core@han` אם בחרת ליבה בלבד, או נקוב ישירות בפלאגין שכבה עם `han-documentation@han`, `han-research@han`, `han-planning@han`, `han-coding@han`, `han-github@han`, `han-reporting@han`, `han-feedback@han`, `han-atlassian@han`, `han-linear@han` או `han-plugin-builder@han`. כולם מתפענחים מאותו marketplace.

הוספת ה-marketplace חושפת את הרישום של Test Double ל-Claude Code כך שהוא יוכל לפענח את הפלאגין לפי שם; לכן היא באה קודם. כשההתקנה מסתיימת, Claude Code מפרט מה הוא הוסיף, כולל כל תלות שהוא משך, כדי שתוכל לוודא שקיבלת את מה שציפית.

## להתחיל מהליבה ולהוסיף שכבה מאוחר יותר

הבחירה ב-`han-core` או בשכבה בודדת אינה דלת חד-כיוונית. אם התחלת עם הליבה בלבד ומאוחר יותר החלטת שאתה רוצה את סקילי ה-GitHub, התקן את `han-github` (או את `han`) מעל מה שכבר יש לך. Claude Code מוסיף את השכבה לליבה שכבר התקנת, ויש לך את החבילה המלאה. אתה לא צריך להסיר או להתקין מחדש שום דבר.

## תיעוד קשור

- [שורש הריפו](../README.md). המקום שכולם מתחילים בו, ושבו נמצאות פקודות ההתקנה.
- [אינדקס הסקילים](./skills/README.md). כל סקיל, עם שורת ריח וקישור לתיעוד המורחב שלו.
- [אינדקס הסוכנים](./agents/README.md). כל סוכן שהסקילים משגרים.
- [Workflows](./workflows.md). איך הסקילים משתרשרים בין הפלאגינים.
- [מושגי יסוד](./concepts.md). מודל הסקילים והסוכנים שעובר כחוט השני בכל החבילה.
- [Quickstart](./quickstart.md). חמישה מסלולים לחמישה מצבים נפוצים, אחרי שהתקנת.
- [How to provide feedback on Han](./how-to/provide-feedback.md). מה לעשות אחרי ש-`han-feedback` מותקן.
- [Why solo and small teams?](./why-solo-and-small-teams.md). תשובת ההתאמה הכנה אם אתה עדיין מתלבט אם Han בשבילך.
