# Quickstart

בחר את המסלול שמתאים למה שאתה מנסה לעשות עכשיו. כל מסלול הוא רצף קצר של כמה סקילים שמצטרפים לתוצאה שימושית. אתה יכול ללכת לפי מסלול מתחילתו ועד סופו, או לקפוץ ממנו בכל שלב.

> ראה גם: [דף הנחיתה של הפלאגין](../README.md) · [מושגי יסוד](./concepts.md) · [מדריכי How-to](./how-to/README.md) · [סקילים](./skills/README.md) · [סוכנים](./agents/README.md) · [Sizing](./sizing.md) · [YAGNI](./yagni.md)

> **עדיין לא התקנת את Han?** קרא קודם את [Choosing a Han plugin](./choosing-a-han-plugin.md) כדי לבחור בין החבילה המלאה לבין הליבה בלבד, ואז חזור לכאן.

[מדריכי ה-how-to](./how-to/README.md) מכסים לעומק את זרימות העבודה של תכנון, מיון באגים ומחקר, עם פרומפטים ספציפיים, מה לעשות בין שלב לשלב, ולמה לצפות בכל אחד מהם. קרא אחד מהם כשאתה רוצה את המתכון המלא מקצה לקצה למסלול. ה-quickstart מפנה אותך למסלול הנכון; ה-how-to מוליך אותך דרכו.

## באיזה מסלול אתה?

- **[תכנון פיצ'ר חדש](#מסלול-א-תכנון-פיצר-חדש).** יש לך רעיון לפיצ'ר ואתה צריך להבין מה הוא צריך לעשות, איך לבנות אותו, ואז לבנות אותו test-first.
- **[חקירת באג או כשל](#מסלול-ב-חקירת-באג-או-כשל).** משהו שבור או מתנהג מוזר ואתה צריך שורש לבעיה.
- **[מחקר האפשרויות שלך](#מסלול-ה-מחקר-האפשרויות-שלך-לפני-שאתה-מתחייב).** שום דבר לא שבור; יש לך שאלה ואתה רוצה את האפשרויות, את מה שכבר נעשה, והמלצה, לפני שאתה מתחייב.
- **[סקירת קוד או ארכיטקטורה](#מסלול-ג-סקירת-קוד-או-ארכיטקטורה).** אתה רוצה זוג עיניים נוסף על ענף, על PR או על מודול קיים.
- **[הכנת פרויקט לכל השאר](#מסלול-ד-הכנת-פרויקט-לכל-השאר).** אתה רוצה לתעד את הפרויקט שלך, לעגן תקנים, ולתת לכל סקיל אחר הקשר עשיר יותר.

לא בטוח באיזה? התחל בדף [מושגי היסוד](./concepts.md), ואז חזור.

---

## מסלול א: תכנון פיצ'ר חדש

יש לך רעיון לפיצ'ר ואתה רוצה מפרט מעוגן בראיות, ואחריו תוכנית איך לבנות אותו.

ההליכה המלאה, עם פרומפטים, נקודות החלטה, ולמה לצפות בכל שלב, נמצאת ב-**[How to plan a feature, end to end](./how-to/plan-a-feature.md)**. הסקילים בלולאה, לפי הסדר:

[`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md) →
[`/stakeholder-summary`](../han-reporting/docs/skills/stakeholder-summary.md) _(אופציונלי)_ →
[`/plan-a-phased-build`](../han-planning/docs/skills/plan-a-phased-build.md) _(אופציונלי)_ →
[`/plan-implementation`](../han-planning/docs/skills/plan-implementation.md) →
[`/iterative-plan-review`](../han-planning/docs/skills/iterative-plan-review.md) _(אופציונלי)_ →
[`/plan-work-items`](../han-planning/docs/skills/plan-work-items.md) _(אופציונלי)_ → [`/tdd`](../han-coding/docs/skills/tdd.md)
_(כשאתה בונה אותו)_.

**סיימת כאשר:** יש לך `feature-specification.md` ו-`feature-implementation-plan.md` באותה תיקייה, כל אחד עם יומן החלטות מקושר וממצאי סקירה. אם הפיצ'ר היה גדול מספיק כדי לפצל אותו לשלבים, יש לך גם `build-phase-outline.md` שמסדר את העבודה לפרוסות אנכיות שאפשר להדגים. כשאתה בונה אותו, הקוד נוחת התנהגות אחרי התנהגות דרך `/tdd`, כשהבדיקות מובילות.

---

## מסלול ב: חקירת באג או כשל

משהו שבור. אתה רוצה שורש לבעיה, לא ניחוש.

ההליכה המלאה, כולל איך להביא לוגים מפרודקשן ומתי למיין במקום לחקור מיד, נמצאת ב-**[How to triage and investigate a bug](./how-to/triage-and-investigate-a-bug.md)**. הסקילים בלולאה:

[`/issue-triage`](../han-research/docs/skills/issue-triage.md) _(לפי הצורך)_ →
[`/investigate`](../han-coding/docs/skills/investigate.md) →
[`/iterative-plan-review`](../han-planning/docs/skills/iterative-plan-review.md) _(אופציונלי)_.

**סיימת כאשר:** יש לך דוח שנוקב בשורש הבעיה עם ראיות ברמת הקובץ, ותוכנית תיקון ששרדה סקירה אדוורסרית.

---

## מסלול ג: סקירת קוד או ארכיטקטורה

אתה רוצה משוב על משהו שכבר נכתב.

התחל מההיקף שמתאים:

- **ענף או כמה קבצים** ← **[`/code-review`](../han-coding/docs/skills/code-review.md).** תמיד משגר את `junior-developer` ואת `adversarial-security-analyst`. מוסיף באופן מותנה את `test-engineer`, `edge-case-explorer`, `structural-analyst`, `behavioral-analyst`, `concurrency-analyst`, `data-engineer` או `devops-engineer` כשהקבצים שהשתנו מפעילים את התחום שלהם. המערך גדל עם [הגודל](./sizing.md), עם ברירת מחדל קטן. מריץ בדיקות איכות ומייצר סקירה עם ממצאים מסווגים לפי חומרה.
- **PR פתוח ב-GitHub** ← **[`/post-code-review-to-pr`](../han-github/docs/skills/post-code-review-to-pr.md).** כל מה ש-`/code-review` עושה, בתוספת בדיקת בהירות של `junior-developer` מול גוף הסקירה שנוסח, ובתוספת פרסום הסקירה כתגובות על ה-PR.
- **מודול או תת-מערכת שלמה** ← **[`/architectural-analysis`](../han-coding/docs/skills/architectural-analysis.md).** תמיד משגר שדרה של `structural-analyst`, `behavioral-analyst`, `risk-analyst` ו-`software-architect` כדי לבחון צימוד, זרימת נתונים, סיכון והתאמה ל-SOLID. מוסיף באופן מותנה את `concurrency-analyst`, `adversarial-security-analyst`, `data-engineer`, `devops-engineer`, `codebase-explorer` או `system-architect` כשהאותות של אזור המיקוד מחייבים אותם. המערך גדל עם [הגודל](./sizing.md), עם ברירת מחדל קטן. לטופולוגיה בין שירותים כש-`system-architect` לא נכלל אוטומטית, שגר אותו בנפרד.
- **בדיקות שאתה רוצה _לתכנן_, לא לסקור** ← **[`/automated-test-planning`](../han-coding/docs/skills/automated-test-planning.md).** משגר את `test-engineer` ואת `edge-case-explorer`, ובנוסף `concurrency-analyst` או `adversarial-security-analyst` כשהקבצים מחייבים זאת. מייצר תוכנית בדיקות מתועדפת.
- **תוכנית בדיקות שאדם מריץ ידנית** ← **[`/manual-test-planning`](../han-coding/docs/skills/manual-test-planning.md).** מייצר תוכנית בשפה פשוטה של בדיקות בעלות שם עם שלבים ידניים ותוצאות צפויות, שעברה אימות אדוורסרי מול ההקשר שסופק על ידי `adversarial-validator` לפני שהקובץ נכתב.
- **מימוש מול מפרט, PRD או מסמך עיצוב** ← **[`/gap-analysis`](../han-research/docs/skills/gap-analysis.md).** משווה שני תוצרים (מצב קיים מול מצב רצוי) ומייצר דוח בשפה פשוטה שבעלי עניין יכולים לקרוא, מאונדקס לפי מזהי פער יציבים בפורמט `G-NNN`. משגר את `gap-analyzer` לניתוח הראשי, ואז מריץ swarm של מאמתים ומרחיבים כברירת מחדל, כולל הסריקה של `junior-developer` מנקודת מבטם של משתמשים אנושיים, קוראי API, סוכני AI וסוגי שחקנים אחרים. ותר על כך עם `no swarm` למעבר הקל.
- **דוח פערים או PRD שצריך לסדר לבנייה בשלבים** ← **[`/plan-a-phased-build`](../han-planning/docs/skills/plan-a-phased-build.md).** מפצל את תוצר המקור לרצף ממוספר של שלבי בנייה בפרוסות אנכיות. כל שלב הוא תוצר דק מקצה לקצה שאפשר להדגים לאדם אמיתי, וכל אחד נבנה על קודמו. משגר את `information-architect` מול המתאר כפי שנוצר.

**סיימת כאשר:** יש לך תוצר סקירה שאתה סומך עליו, עם ממצאים קשורים לקבצים, לשורות ולרמות חומרה ספציפיות.

---

## מסלול ד: הכנת פרויקט לכל השאר

כל מסלול אחר עובד טוב יותר כשלפלאגין יש הקשר עשיר על הפרויקט שלך. אם יש לך עשר דקות לפני שאתה צריך את הסקיל האמיתי, השקע אותן כאן.

1. **[`/project-discovery`](../han-core/docs/skills/project-discovery.md).** סורק את הריפו וכותב סעיף `## Project Discovery` תמציתי לתוך ה-AGENTS.md או ה-CLAUDE.md שלך (שפות, פריימוורקים, פקודות בנייה, איפה הדברים נמצאים). סקילים אחרים צורכים את זה אוטומטית.
2. **[`/project-documentation`](../han-documentation/docs/skills/project-documentation.md)** _(לפי הצורך)._ תעד פיצ'רים, מערכות ורכיבים. `/code-review` ו-`/architectural-decision-record` קוראים את המסמכים האלה כהקשר.
3. **[`/coding-standard`](../han-coding/docs/skills/coding-standard.md)** _(לפי הצורך)._ עגן מוסכמות קוד, בין אם מדפוסים קיימים ובין אם ממחקר. `/code-review` בודק אותן אוטומטית.
4. **[`/architectural-decision-record`](../han-documentation/docs/skills/architectural-decision-record.md)** _(לפי הצורך)._ תעד החלטות ארכיטקטוניות.
5. **[`.han/config.md`](./configuration.md)** _(לפי הצורך)._ החזק קובץ קונפיגורציה אופציונלי שקובע תיקיית בסיס לפלטי ה-markdown של Han, גודל swarm ברירת מחדל לסקילים מודעי-הגודל, פרופיל קול כתיבה, וסוכנים נוספים שהסקילים המשגרים ישקלו. שים אותו בתיקיית הקונפיגורציה של Claude Code שלך להגדרות שנוסעות איתך לכל מקום, או בשורש הפרויקט עבור אותו פרויקט בלבד.

**סיימת כאשר:** יש לך סעיף `## Project Discovery` ב-AGENTS.md או ב-CLAUDE.md שלך, ואת המסמכים והתקנים שאתה צריך כדי לתת לסקילים אחרים הקשר שימושי.

---

## מסלול ה: מחקר האפשרויות שלך לפני שאתה מתחייב

יש לך שאלה, לא באג ועדיין לא פיצ'ר. אתה רוצה את האפשרויות, את מה שכבר נעשה, והמלצה שאתה יכול לסמוך עליה, לפני שאתה בוחר כיוון.

ההליכה המלאה, כולל איך ללכוד את ההמלצה כ-ADR כך שלצוות יהיה רישום קנוני אחד, נמצאת ב-**[How to research a decision and capture it](./how-to/research-a-decision.md)**. הסקילים בלולאה:

[`/research`](../han-research/docs/skills/research.md) →
[`/architectural-decision-record`](../han-documentation/docs/skills/architectural-decision-record.md) →
[`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md) _(צעד הבא אופציונלי)_.

**סיימת כאשר:** יש לך דוח מחקר שההמלצה שבו שרדה מעבר אדוורסרי, עם כל טענה קשורה למקור שאתה יכול לבדוק בעצמך, וההחלטה מתועדת כ-ADR. אם הבקשה הייתה בעצם באג, מפרט, תקן, השוואת תוצרים או הערכה ארכיטקטונית, `/research` מנתב אותך לסקיל שאחראי על זה במקום.

---

## שילוב מסלולים

אתה יכול להזכיר כמה סקילים בפרומפט אחד ו-Claude מריץ אותם ברצף, ומזין את הפלט של כל אחד לתוך הבא. כמה שעובדים:

- _"תחקור למה משלוחי webhook נכשלים לסירוגין, ואז תיצור תוכנית לתקן את זה ותעבור עליה באיטרציות."_ ←
  [`/investigate`](../han-coding/docs/skills/investigate.md) →
  [`/iterative-plan-review`](../han-planning/docs/skills/iterative-plan-review.md).
- _"תסרוק את הריפו הזה, תתעד את מערכת האימות, ותיצור תקן קוד לאיך שאנחנו מטפלים בטוקנים."_ ←
  [`/project-discovery`](../han-core/docs/skills/project-discovery.md) →
  [`/project-documentation`](../han-documentation/docs/skills/project-documentation.md) →
  [`/coding-standard`](../han-coding/docs/skills/coding-standard.md).
- _"תסקור את הענף שלי, ואז תיצור ADR לכל החלטה ארכיטקטונית ב-diff."_ ←
  [`/code-review`](../han-coding/docs/skills/code-review.md) →
  [`/architectural-decision-record`](../han-documentation/docs/skills/architectural-decision-record.md).
- _"תתכנן את פיצ'ר ה-retry, ואז תתכנן את המימוש, ואז תיצור לו תוכנית בדיקות."_ ←
  [`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md) →
  [`/plan-implementation`](../han-planning/docs/skills/plan-implementation.md) →
  [`/automated-test-planning`](../han-coding/docs/skills/automated-test-planning.md).
- _"תגדיר את זרימת ה-onboarding החדשה, ואז תכתוב סיכום לבעלי עניין שאוכל לשתף עם ההנהלה לפני שנבנה."_ ←
  [`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md) →
  [`/stakeholder-summary`](../han-reporting/docs/skills/stakeholder-summary.md) →
  [`/html-summary`](../han-reporting/docs/skills/html-summary.md) _(אופציונלי, לגרסת HTML עצמאית להעברה)_.
- _"תגדיר את מנוע ההנחות, ואז תבנה אותו test-first."_ ← [`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md)
  → [`/tdd`](../han-coding/docs/skills/tdd.md) → [`/code-review`](../han-coding/docs/skills/code-review.md).
- _"תחקור את האפשרויות שלנו למשימות רקע, ואז תגדיר את זו שאתה ממליץ עליה."_ ←
  [`/research`](../han-research/docs/skills/research.md) → [`/plan-a-feature`](../han-planning/docs/skills/plan-a-feature.md).
- _"תשווה את מימוש האימות למפרט האימות, ואז תתכנן איך לסגור את הפערים, ולסיום תפרק את העבודה הזו ליחידות בגודל משימה."_ ←
  [`/gap-analysis`](../han-research/docs/skills/gap-analysis.md) →
  [`/plan-implementation`](../han-planning/docs/skills/plan-implementation.md) →
  [`/plan-work-items`](../han-planning/docs/skills/plan-work-items.md).
- _"תשווה את מימוש share v1 למפרט share v2, תפצל את הפערים להשקה בשלבים, ואז תתכנן מימוש לשלב הראשון, ולבסוף תפרוס משימות בודדות על בסיס התוכנית הזו."_ ←
  [`/gap-analysis`](../han-research/docs/skills/gap-analysis.md) →
  [`/plan-a-phased-build`](../han-planning/docs/skills/plan-a-phased-build.md) →
  [`/plan-implementation`](../han-planning/docs/skills/plan-implementation.md) →
  [`/plan-work-items`](../han-planning/docs/skills/plan-work-items.md).

## הערה על גודל

הסקילים מודעי-הגודל (`/architectural-analysis`, `/code-overview`, `/code-review`, `/code-walkthrough`, `/design-an-api`, `/gap-analysis`, `/iterative-plan-review`, `/plan-a-feature`, `/plan-implementation`, `/research`) מסווגים את העבודה כ**קטנה**, **בינונית** או **גדולה** לפני שיגור הסוכנים. ברירת המחדל שלהם היא קטן, והם מגדילים את הצוות ואת עומק האיטרציות לפי הרצועה שנבחרה. העבר את הגודל כארגומנט המיקומי הראשון כדי לעקוף (`/code-review medium`, `/plan-a-feature large "describe the feature"`). ראה [Sizing](./sizing.md) למודל המלא.

## הערה על YAGNI

כל סקיל תכנון, סקירה ותקנים מחיל כלל YAGNI מבוסס-ראיות לפני שהוא מתחייב לפריטים בתוצר שלו. פריטים בלי ראיות קבילות עוברים לסעיף `## Deferred (YAGNI)` עם טריגר _reopen-when_ נקוב. לעולם לא נזרקים בשקט. אם סקיל אומר "deferred (YAGNI)", ראה [YAGNI](./yagni.md) לשני השערים, לרשימת הראיות הקבילות ולתהליך העקיפה.

## לאן ממשיכים מכאן

- בחר סקיל מ-[אינדקס הסקילים](./skills/README.md).
- לך לפי מדריך how-to מ-[אינדקס ה-How-to](./how-to/README.md) כשאתה רוצה את המתכון המלא מקצה לקצה לאחד המסלולים למעלה.
- עבור ברפרוף על [אינדקס הסוכנים](./agents/README.md) כדי להבין את המומחים שהסקילים משגרים.
- קרא את [מושגי היסוד](./concepts.md) אם ההפרדה בין סקיל לסוכן עדיין מטושטשת.
- קרא את [Sizing](./sizing.md) כדי להבין איך הסקילים המשגרים מחליטים כמה סוכנים לשגר.
- קרא את [YAGNI](./yagni.md) כדי להבין מה שורד סקירה ומה נדחה.
