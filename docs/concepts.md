# מושגי יסוד

Han בנויה משני סוגי דברים: **סקילים** ו**סוכנים**. אם תקרא את הדף הזה פעם אחת לפני שאתה בוחר slash command, כל שאר התיעוד יתחיל להתחבר.

> ראה גם: [דף הנחיתה של הפלאגין](../README.md) · [בחירת פלאגין](./choosing-a-han-plugin.md) · [Quickstart](./quickstart.md) · [כל הסקילים](./skills/README.md) · [כל הסוכנים](./agents/README.md)

## TL;DR

- **סקיל** הוא תהליך דטרמיניסטי שאתה בדרך כלל מריץ עם slash command (כמו `/code-review`), אם כי Claude יכול גם להפעיל אותו לבד כשהבקשה שלך תואמת לתיאור של הסקיל. חשוב על זה כתרשים זרימה.
- **סוכן** הוא פרסונה מומחית בעלת שיקול דעת, שסקיל משגר או שאתה משגר (כמו `adversarial-security-analyst`). חשוב על זה כחבר צוות.
- סקילים משגרים סוכנים. הסקיל הולך לפי תרשים הזרימה שלו, שולח את הסוכן לבצע תת-משימה שדורשת שיקול דעת (לחקור באג, לסקור ארכיטקטורה, לבקר תוכנית), ואז מקפל את הממצא בחזרה לתוך הפלט שלו.
- **גודל (Sizing)** קובע כמה סוכנים משוגרים. הסקילים שמתפרשים ל-swarm מסווגים קודם את העבודה כקטנה, בינונית או גדולה, ברירת המחדל היא קטנה, ומשם הם מגדילים את הצוות ואת עומק האיטרציות. ראה [Sizing](./sizing.md) למודל המלא.
- **YAGNI** קובע מה שורד. כל סקיל שמייצר תוצר וכל סוכן שסוקר תוצר מחיל כלל YAGNI מבוסס-ראיות לפני שהוא מתחייב לפריטים: פיצ'רים, שלבי תוכנית, המלצות קוד, ADRs, תקני קוד, runbooks, התראות, אינדקסים, בדיקות והפשטות. פריטים בלי ראיות נדחים (מתועדים להמשך, לא נזרקים בשקט). ראה [YAGNI](./yagni.md).
- **ראיות (Evidence)** קובעות כמה בטוח אתה במה ששרד. אחרי ש-YAGNI העביר פריט, כלל הראיות נוקב במחלקת האמון של הציטוט (בסיס הקוד, רשת, סופק) ומחיל שער אימות-הצלבה על מקורות מהרשת. הוא גם מתייג טענות שאין להן ראיות בשום דרג כמצב דחייה נפרד. ראה [Evidence](./evidence.md).

שלושת אלה הם כל מודל ההחלטה. כל השאר הוא אוצר מילים.

- **קריאוּת (Readability)** היא תקן מסוג אחר, לא מנגנון החלטה רביעי. גודל, YAGNI וראיות מחליטים _מה קורה_ לפריט. קריאוּת שולטת ב*פלט* של הסקילים שהתוצר שלהם הוא טקסט שקורא שאינו הכותב קורא, כך שהפלט הזה פותח בעיקר, משתמש בשפה פשוטה, וחושף פרטים בשכבות. היא מוגבלת לאותם סקילים שפונים לקורא, ולא כמעט-אוניברסלית כמו שלושת המנגנונים. ראה [Readability](./readability.md).

> **שוקל את Han לארגון גדול?** Han נבנתה למהנדסי מוצר יחידים ולצוותים קטנים, לא לצוותים גדולים או לארגונים. קרא את [Why solo and small teams, and not large teams or enterprise?](./why-solo-and-small-teams.md) לתשובה הכנה על ההתאמה לפני שאתה ממשיך.

## סקילים: שכבת התהליך

סקיל הוא רצף צעדים קבוע ש-Claude Code מריץ. הקלדת ה-slash command היא הדרך העיקרית להפעיל אותו, אבל לא היחידה.

- אתה מפעיל אותו: `/code-review`, `/plan-a-feature`, `/investigate`. זה המסלול המכוון והעיקרי.
- Claude עשוי גם להפעיל אותו לבד. תיאורי הסקילים כתובים כך שיתאימו לכוונת המשתמש, ולכן בקשה כמו "אתה יכול לוודא שהקוד הזה תקין?" יכולה להתנתב ל-`/code-review` בלי שתקליד את הפקודה. זה פעיל כברירת מחדל (שדה ה-frontmatter‏ `disable-model-invocation` מוגדר כברירת מחדל ל-`false`); אף סקיל של Han לא מכבה את זה. כך או כך הסקיל מריץ את אותו פרוטוקול.
- הוא הולך לפי פרוטוקול מוגדר. כל מי שמריץ את אותו סקיל מקבל את אותה צורת פלט.
- הוא מתועד בקובץ `SKILL.md` בתוך תיקיית `skills/{name}/` של הפלאגין שלו (`han-documentation/skills/{name}/`, `han-research/skills/{name}/`, `han-planning/skills/{name}/`, `han-coding/skills/{name}/`, `han-github/skills/{name}/`, ותיקיות ה-`skills/{name}/` של יתר הפלאגינים).
- הוא עשוי לשגר סוכן אחד או יותר לצעדים שדורשים שיקול דעת.

**המבחן:** האם היית יכול לצייר את כל הדבר כתרשים זרימה? אם כן, זה סקיל.

## סוכנים: שכבת שיקול הדעת

סוכן הוא חבר צוות מומחה. מודל עם פרסונה, תחום צר ועמדה מוצהרת.

- לסוכן יש שם כמו `adversarial-security-analyst`, `plan-synthesizer` או `junior-developer`.
- סוכן מפעיל שיקול דעת תלוי-הקשר. _האם הממצא הזה באמת בעיה? האם התוכנית מטפלת בסיכון? האם כדאי לשאול מומחה נוסף?_
- סוכן מתועד בקובץ `.md` אחד בתוך תיקיית ה-`agents/` של הפלאגין שלו (`han-core/agents/` עבור המערך המשותף; ה-readability-editor יושב ב-`han-communication/agents/`, ה-research-analyst ב-`han-research/agents/`, וה-discussion-facilitator ב-`han-planning/agents/`).
- אתה יכול לשגר סוכן ישירות עם כלי ה-`Agent`, אבל את רוב הסוכנים משגרים _עבורך_ כשסקיל צריך את הקלט שלהם.

**המבחן:** האם זה דורש חשיבה על הקשר במקום ביצוע של סקריפט? אם כן, זה סוכן.

## איך הם מתחברים

סקיל מריץ את הפרוטוקול שלו, ובצעדים שדורשים שיקול דעת הוא משגר סוכן. הסוכן מחזיר ממצאים; הסקיל מקפל אותם לתוך הפלט הסופי.

```
You → /plan-a-feature → (interview loop, codebase discovery)
                     → dispatches → junior-developer
                                  → plan-synthesizer
                                  → 3-5 specialist agents
                     ← folds findings back in
      ←  feature-specification.md, decision-log.md, team-findings.md
```

כמה צמדים קונקרטיים מתוך הפלאגין:

- **`/plan-a-feature` משגר את `junior-developer` ואת `plan-synthesizer` ובנוסף שלושה עד חמישה מומחים.** המומחים נבחרים לפי מה שהפיצ'ר נוגע בו. פיצ'ר עתיר-נתונים מכניס את `data-engineer`. פיצ'ר עם משטח פרודקשן מכניס את `devops-engineer`. זרימה שהמשתמש רואה מכניסה את `user-experience-designer`.
- **`/code-review` תמיד משגר את `junior-developer` ואת `adversarial-security-analyst`, ובנוסף את יתר המערך באופן מותנה** (`test-engineer`, `edge-case-explorer`, `structural-analyst`, `behavioral-analyst`, `concurrency-analyst`, `data-engineer`, `devops-engineer`, `on-call-engineer`) לפי מה שהקבצים שהשתנו נוגעים בו. המערך גדל עם [הגודל](./sizing.md): שינוי קטן מריץ את המערך המינימלי; שינוי גדול מריץ את כל המערך המותנה. כל סוכן סוקר את שינויי הענף מהעדשה שלו, והסקיל מסווג את הממצאים שלהם לתוך פלט הסקירה.
- **`/architectural-analysis` תמיד משגר שדרה של `structural-analyst`, `behavioral-analyst`, `risk-analyst` ו-`software-architect`, ובנוסף את יתר המערך לפי אותות** (`concurrency-analyst` כשיש פרימיטיבים של מקביליות; `adversarial-security-analyst`, `data-engineer`, `devops-engineer` כשאזור המיקוד נוגע באימות/PII, בחוזי נתונים או במשטח תפעולי; `on-call-engineer` כשקוד המקור של האפליקציה באזור המיקוד מראה אות של חוסן כוננות; `codebase-explorer` לאזורים גדולים ולא מוכרים; `system-architect` בגודל גדול כשקיים תפר בין שירותים או בין הקשרים חסומים). המערך גדל עם [הגודל](./sizing.md): קטן מריץ את השדרה בתוספת מקביליות; גדול מריץ כל מומחה שקיבל אות. אנליסטי הגילוי רצים ראשונים, `risk-analyst` מנקד את הממצאים שלהם, והארכיטקטים מסנתזים. כש-`system-architect` לא משוגר, סוגיות של חצייה בין שירותים ובין הקשרים חסומים עולות כדחויות כדי שתוכל לשגר אותו בנפרד.
- **`/investigate` משגר את `evidence-based-investigator` ובנוסף מומחים מותנים** (`concurrency-analyst`, `behavioral-analyst`, `data-engineer`) לפי הסימפטום, ואחריהם `adversarial-validator` כדי להוכיח שהתיקון המוצע יתקן את הבאג במקום להסתיר אותו.
- **`/gap-analysis` משגר את `gap-analyzer` פעם אחת לניתוח הראשי, ואז פורש swarm של מאמתים ומרחיבים כברירת מחדל.** `adversarial-validator` ו-`junior-developer` (שמריץ סריקה מפורשת מנקודת מבטם של שחקנים שונים: משתמשים אנושיים, קוראי API, סוכני AI וסוגי שחקנים אחרים) נדרשים בכל גודל. `evidence-based-investigator` נדרש כשהמצב הקיים קונקרטי. `plan-synthesizer` נדרש בגודל בינוני וגדול כדי לאחד את סעיף 4 של הדוח. מומחי תחום (`adversarial-security-analyst`, `data-engineer`, `user-experience-designer` ואחרים) מתווספים לפי מה שהפערים נוגעים בו. השב `no swarm` כדי לוותר ולחזור למעבר קל של gap-analyzer בלבד.
- **`/plan-a-phased-build` משגר את `information-architect` פעם אחת בזמן ריצה** מול מתאר שלבי הבנייה כפי שנוצר, כדי לוודא יכולת מציאה, עמידה עצמאית של רשומות השלבים לפי EPPO, והבנה הדרגתית, לפני שהמסמך מוצג לך. הסקיל מחיל ממצאים של דליפת שפה לא-פשוטה כעריכות חובה, וממצאים מבניים כשהם משמרים את החוזה של המסמך.

אתה לא צריך לשנן את הצמדים האלה כדי להריץ סקיל. אתה כן צריך לדעת שהם קיימים. כך, כשהפלט של הסקיל מזכיר "ממצא מ-`plan-synthesizer`" או "האנליסטים הארכיטקטוניים סימנו צימוד", אתה יודע מה זה אומר.

## גודל: ידית השיגור

כל סקיל שמשגר swarm של סוכנים מסווג את העבודה כ**קטנה**, **בינונית** או **גדולה** לפני השיגור, ואז משתמש ברצועה כדי לתחום את גודל הצוות או ה-swarm, את עומק האיטרציות, ואת רצועות החומרה שהסוכנים מסלימים.

- **ברירת המחדל היא קטן.** כל סקיל מודע-גודל מתחיל את הסיווג בקטן ומסלים רק כשאותות קונקרטיים מחייבים זאת.
- **סיווג אוטומטי, עם עקיפה דרך `$size`.** הסקילים קוראים אותות (מספר קבצים, תת-מערכות שנגעו בהן, משטח אבטחה/נתונים/תשתית) ומכריזים על הגודל שנבחר עם הצדקה בשורה אחת. העבר `small`, `medium` או `large` כארגומנט המיקומי הראשון כדי לעקוף (`/code-review medium`, `/plan-a-feature large "describe the feature"`).
- **סקילים מודעי-גודל.** [`/architectural-analysis`](../han-coding/docs/skills/architectural-analysis.md), [`/code-overview`](../han-coding/docs/skills/code-overview.md), [`/code-review`](../han-coding/docs/skills/code-review.md), [`/code-walkthrough`](../han-coding/docs/skills/code-walkthrough.md), [`/design-an-api`](../han-coding/docs/skills/design-an-api.md), [`/gap-analysis`](../han-research/docs/skills/gap-analysis.md), [`/iterative-plan-review`](../han-planning/docs/skills/iterative-plan-review.md), [`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md), [`/plan-implementation`](../han-planning/docs/skills/plan-implementation.md), [`/research`](../han-research/docs/skills/research.md).

קרא את מסמך הייחוס המלא [Sizing](./sizing.md) לרצועות, לתהליך הסיווג האוטומטי ולכללים לכל סקיל.

## YAGNI: שער ההכללה

כל סקיל שמייצר תוצר וכל סוכן שסוקר תוצר מריץ כלל YAGNI מבוסס-ראיות לפני שהוא מתחייב לפריטים. לכלל שני שערים: מבחן ראיות (_האם זה נחוץ עכשיו?_) ומבחן גרסה פשוטה יותר (_האם קיימת גרסה פשוטה יותר באופן מובהק שמספקת את אותן ראיות?_). פריטים בלי ראיות נדחים, ומתועדים תחת סעיף `## Deferred (YAGNI)` בתוצר, עם טריגר _reopen-when_ נקוב. לעולם לא נזרקים בשקט.

YAGNI חל על סקילי התכנון (`/plan-a-feature`, `/plan-implementation`, `/plan-a-phased-build`, `/iterative-plan-review`). הוא חל על סקירה ותקנים (`/code-review` בייעוץ בלבד, `/coding-standard`, `/automated-test-planning`, `/architectural-decision-record`). הוא חל גם על כמה סוכנים (`discussion-facilitator`, `plan-synthesizer`, `junior-developer`, `software-architect`, `system-architect`, `test-engineer`, `edge-case-explorer`, `data-engineer`, `devops-engineer`, `on-call-engineer`).

קרא את מסמך הייחוס המלא [YAGNI](./yagni.md) לשערים, לרשימת הראיות הקבילות, לאנטי-דפוסים הנקובים בשם ולטבלת ההחלה לכל סקיל ולכל סוכן.

## ראיות: שכבת הביטחון

אחרי ש-YAGNI סינן את ההכללה, כלל הראיות מאפיין את איכות הראיות שכל פריט ששרד נשען עליהן. שלושה עקרונות מבססים את הכלל. ראיות קרובות יותר לאירוע או לנתון המקורי נושאות משקל רב יותר מראיות רחוקות יותר (קרבה, שמוחלת כהיוריסטיקה ולא כסולם מדורג). שני מקורות בלתי תלויים עדיפים על מקור אחד (אימות-הצלבה, מוגבל למקורות מהרשת). היעדר ראיות הוא מצב בפני עצמו עם שם ועם תגובה (תיוג היעדר-ראיות). אוצר המילים של מחלקות האמון (בסיס הקוד, רשת, סופק) ושער אימות-ההצלבה נולדו ב-[`/research`](../han-research/docs/skills/research.md), וכיום חולצו לכלל קנוני שכל סקיל וכל סוכן מודעי-ראיות קוראים בזמן ריצה.

ראיות חלות על סקילי המחקר והחקירה (`/research`, `/investigate`, `/gap-analysis`) ועל סקילי התכנון והסקירה (`/plan-a-feature`, `/plan-implementation`, `/iterative-plan-review`). הן חלות גם על סקילי המוסכמות (`/coding-standard`, `/architectural-decision-record`), על הסקילים התפעוליים (`/runbook`), ועל הסוכנים שסוקרים תוצרים (`discussion-facilitator`, `junior-developer`, `evidence-based-investigator`, `gap-analyzer`).

קרא את מסמך הייחוס המלא [Evidence](./evidence.md) לשלושת העקרונות, לאוצר המילים של מחלקות האמון, לשער אימות-ההצלבה, לתגובת היעדר-הראיות ולטבלת ההחלה לכל סקיל ולכל סוכן.

## קריאוּת: תקן הפלט

גודל, YAGNI וראיות מחליטים איך סקיל עובד. קריאוּת מחליטה איך הפלט שלו נקרא. כל סקיל שפונה לקורא (כזה שהתוצר העיקרי שלו הוא טקסט שקורא שאינו הכותב קורא מתחילתו ועד סופו) מחיל כלל קריאוּת משותף אחד תוך כדי הכתיבה. הכלל הזה גורם לתוצר לפתוח בעיקר, לתת לכל פסקה רעיון אחד, להשתמש בכותרות מתארות, לשמור על משפטים קצרים ופעילים, להעדיף מילים נפוצות, ולחשוף פרטים בשכבות.

הכלל מוחל בשלבים, לעולם לא כבלוק הוראות אחד. הכללים המבניים שלו מעצבים את תבנית הפלט של כל סקיל, והקריטריונים המעוגנים בהתנהגות רצים כבדיקה עצמית נפרדת אחרי שהטיוטה קיימת. סקילים שיש להם שלב סינתזה או עריכה משגרים גם את סוכן ה-[`readability-editor`](../han-communication/docs/agents/readability-editor.md) כדי לשכתב את הטיוטה, תוך שמירה על כל עובדה. נאמנות גוברת על קריאוּת: שום עובדה נדרשת לא נזרקת כדי שהטקסט ייקרא פשוט יותר, אלא אם הקורא ביקש פחות ואיבודה לא היה משנה את מה שהוא עושה אחר כך.

קריאוּת חלה על הסקילים שפונים לקורא (`/research`, `/gap-analysis`, `/project-documentation`, `/issue-triage`, `/runbook`, `/architectural-decision-record`, `/code-overview`, `/investigate`, `/code-review`, `/architectural-analysis`, `/stakeholder-summary`, `/html-summary`, `/update-pr-description`, `/plan-a-feature`, `/plan-implementation`, `/plan-a-phased-build`, `/plan-work-items`, `/iterative-plan-review`, `/coding-standard` ו-`/automated-test-planning`). מפרט מובנה, תוכנית, בנייה בשלבים, רשימת פריטי עבודה, תקן קוד או תוכנית בדיקות נחשבים ככאלה כשאדם קורא אותם מתחילתם ועד סופם. סקילים שהפלט שלהם הוא קוד, או תוצר מובנה שרק סקילים במורד הזרם צורכים כקלט מכונה, נמצאים מחוץ להיקף.

קרא את מסמך הייחוס המלא [Readability](./readability.md) לתכונות הנדרשות, להחלה בשלבים, לטבלת ההיקף ולשמירת הנאמנות.

## קונפיגורציה

Han קוראת שני קובצי `.han/config.md` אופציונליים בכל ריצת סקיל: אחד אישי בתיקיית הקונפיגורציה של Claude Code שלך, ואחד של הפרויקט בשורש הפרויקט. כל אחד מהם קובע תיקיית בסיס לתוצרי ה-markdown של הסקילים, גודל swarm ברירת מחדל לסקילים מודעי-הגודל, פרופיל קול כתיבה לסקילי הקריאוּת, וסוכנים נוספים שהסקילים המשגרים ישקלו. הקובץ האישי מספק ברירות מחדל שנוסעות איתך לכל פרויקט, וקובץ הפרויקט עוקף אותן הגדרה-אחר-הגדרה. מי שאין לו אף אחד מהקבצים לא רואה שום שינוי, וקובץ שבור מתדרדר בשקט לברירות המחדל עם הערה בשורה אחת שנוקבת באיזה קובץ מדובר. קרא את מסמך הייחוס המלא [Configuration](./configuration.md) לסכמה, לשרשרת הקדימות ולחוזה ההתדרדרות.

## מתי היית משגר סוכן ישירות?

רוב הזמן לא תעשה זאת. סקיל שקורא לסוכן הוא הזרימה הרגילה.

ייתכן שתשגר סוכן ישירות כאשר:

- שיקול הדעת שאתה רוצה צר יותר מכל סקיל קיים. _"תן לי ביקורת אבטחה על `src/auth/` עם `adversarial-security-analyst`"_. אין צורך ב-`/code-review` מלא.
- אתה רוצה חוות דעת שנייה אחרי שסקיל רץ. שגר את `adversarial-validator` מול התוכנית שסקיל תכנון ייצר.
- אתה מרכיב workflow מותאם שלא מתאים לאף slash command בצורה נקייה.

שיגור ישיר משתמש בכלי ה-`Agent` עם `subagent_type: {plugin}:{agent-name}` (לדוגמה, `han-core:adversarial-security-analyst`, או `han-research:research-analyst`).

## איך Han ארוזה

Han מגיעה כמשפחת פלאגינים ב-marketplace אחד. `han-core` נושא את מערך הסוכנים המומחים המשותף שהפלאגינים האחרים משגרים, את הסקיל project-discovery, את מצב העבודה המשותף `/pairing` ואת קובצי הכללים הקנוניים.

`han-documentation` מוסיף את סקילי התיעוד (`/project-documentation`, `/architectural-decision-record` ו-`/runbook`). `han-research` מוסיף את סקילי עבודת הידע שלפני התכנון (`/research`, `/gap-analysis` ו-`/issue-triage`) ובנוסף את הסוכן research-analyst. `han-planning` מוסיף את סקילי התכנון שאתה פונה אליהם לפני המימוש (`/plan-a-feature`, `/plan-implementation`, `/plan-a-phased-build`, `/plan-work-items` ו-`/iterative-plan-review`). `han-coding` מוסיף את סקילי הקוד שאתה פונה אליהם תוך כדי עבודה בקוד (`/tdd`, `/refactor`, `/design-an-api`, `/code-review`, `/code-overview`, `/code-walkthrough`, `/architectural-analysis`, `/automated-test-planning`, `/manual-test-planning`, `/investigate` ו-`/coding-standard`). `han-github` מוסיף את סקילי ה-GitHub, ו-`han-reporting` מוסיף את סקילי הדיווח. כל אלה חוץ מ-`han-reporting` תלויים ב-`han-core`, ולכן התקנה של כל אחד מהם מביאה איתה את הסוכנים המשותפים; `han-reporting` תלוי רק ב-`han-communication`.

`han` הוא מטא-פלאגין בלי רכיבים משלו. הוא תלוי ב-`han-communication`, ב-`han-core`, ב-`han-documentation`, ב-`han-research`, ב-`han-planning`, ב-`han-coding`, ב-`han-github` וב-`han-reporting`, ולכן התקנה שלו מושכת את החבילה המצורפת.

יתר הפלאגינים אופציונליים. `han-feedback` מוסיף את סקיל המשוב שאחרי הסשן ולא תלוי בשום פלאגין אחר של Han. `han-atlassian` מוסיף את סקילי Confluence ו-Jira; הוא דורש שרת MCP של Atlassian מוגדר, ומכיוון שסקילי העטיפה שלו מריצים סקילים מ-`han-documentation`, מ-`han-planning` ומ-`han-coding`, הוא תלוי בשלושת אלה ובנוסף ב-`han-core`. `han-linear` מוסיף את סקיל work-items-to-Linear, דורש שרת MCP של Linear מוגדר, ולא תלוי בשום פלאגין אחר של Han. המטא-פלאגין `han` לא מושך את אלה, ולכן כל אחד מהם מותקן בנפרד.

`han-plugin-builder` נושא את ההנחיות לבניית סקילים, סוכנים ופלאגינים, ובנוסף את הסקילים מונחי-הראיון `/skill-builder` ו-`/agent-builder`. הוא לא תלוי בכלום וגם הוא אופציונלי.

הבחירה המעשית היא ליבה בלבד, החבילה המצורפת, או החבילה בתוספת הפלאגינים האופציונליים שאתה רוצה. אין התקנה של תכנון-בלבד, קוד-בלבד או GitHub-בלבד. `han-reporting` הוא היוצא מן הכלל: הוא תלוי ב-`han-communication` בלבד, ולכן התקנה שלו לבדו נותנת לך את סקילי הדיווח בלי הסוכנים של `han-core`.

לאיזה מהם להתקין ולתלות שמפתיעה אנשים, קרא את [Choosing a Han plugin](./choosing-a-han-plugin.md).

## מה הפלאגין כולל?

- **הסקילים.** [אינדקס הסקילים](./skills/README.md) מקבץ אותם לפי מטרה (תכנון, בנייה, חקירה ומחקר, סקירה, גילוי, מוסכמות, דיווח, תפעול).
- **הסוכנים.** [אינדקס הסוכנים](./agents/README.md) מקבץ אותם לפי תפקיד (תכנון והנחיה, סוקרים אדוורסריים, חקירה, ארכיטקטורה, בדיקות, פערים ותוכן).

עבור על האינדקסים ברפרוף אחרי שתקרא את הדף הזה. בחר את הסקיל האחד שאתה צריך עכשיו. חזור מאוחר יותר ללמוד את השאר.

## לאן ממשיכים מכאן

- **רוצה להספיק משהו?** ← [Quickstart](./quickstart.md). בוחר סקיל התחלתי לפי מה שאתה מנסה לעשות.
- **רוצה סקיל מסוים?** ← [אינדקס הסקילים](./skills/README.md).
- **רוצה סוכן מסוים?** ← [אינדקס הסוכנים](./agents/README.md).
- **רוצה לדעת איך השיגור גדל?** ← [Sizing](./sizing.md).
- **רוצה לדעת מה שורד סקירה?** ← [YAGNI](./yagni.md).
- **רוצה לדעת כמה לבטוח במה ששרד?** ← [Evidence](./evidence.md).
- **רוצה לדעת איך שומרים על קריאוּת הפלט של סקיל?** ← [Readability](./readability.md).
- **רוצה לכוונן לאן סקילים כותבים ואילו סוכנים הם שוקלים?** ← [Configuration](./configuration.md).
- **כותב סקיל או סוכן משלך?** ← [Contributing](../CONTRIBUTING.md).

## קריאה נוספת

- [`han-plugin-builder/skills/guidance/references/plugin-entity-taxonomy.md`](../han-plugin-builder/skills/guidance/references/plugin-entity-taxonomy.md). הטקסונומיה שהפלאגין הזה הולך לפיה. חלה על כל הפלאגינים בריפו הזה.
- [Claude Code Skills reference](https://code.claude.com/docs/en/skills). איך סקילים מוגדרים ומופעלים ב-Claude Code עצמו.
- [Claude Code Subagents reference](https://code.claude.com/docs/en/sub-agents). איך סוכנים משוגרים מתוך סקילים.
