#!/usr/bin/env bats

setup() {
  REPO_ROOT="$(cd "${BATS_TEST_DIRNAME}/.." && pwd)"
  SCRIPT="${REPO_ROOT}/scripts/translation-status.py"
  WORK="$(mktemp -d)"
  mkdir -p "${WORK}/scripts" "${WORK}/docs"
  cp "${SCRIPT}" "${WORK}/scripts/"
  cp "${REPO_ROOT}/scripts/check-translation-anchors.py" "${WORK}/scripts/"
}

teardown() {
  rm -rf "${WORK}"
}

@test "מדרג קובץ בעברית כמתורגם" {
  printf '# כותרת\n\nזו פסקה בעברית שמסבירה משהו על הפרויקט הזה.\n' > "${WORK}/docs/heb.md"
  cd "${WORK}" && python3 scripts/translation-status.py
  grep -q -- "- ✅.*docs/heb.md" "${WORK}/docs/translation-status.md"
}

@test "מדרג קובץ באנגלית כלא מתורגם" {
  printf '# Title\n\nThis paragraph explains something about the project in English prose.\n' > "${WORK}/docs/eng.md"
  cd "${WORK}" && python3 scripts/translation-status.py
  grep -q -- "- ⬜.*docs/eng.md" "${WORK}/docs/translation-status.md"
}

@test "כותרת ציטוט באנגלית ושורת URL לא מורידות קובץ מתורגם לחלקי" {
  printf '# כותרת\n\nפסקה בעברית שמסבירה את הרעיון.\n\n### Kent Beck: Test-Driven Development\n\nURL: https://example.com/book\n' > "${WORK}/docs/cite.md"
  cd "${WORK}" && python3 scripts/translation-status.py
  grep -q -- "- ✅.*docs/cite.md" "${WORK}/docs/translation-status.md"
}

@test "מזהה קובץ מתורגם למחצה כחלקי" {
  {
    printf '# כותרת\n\n'
    for i in 1 2 3 4 5 6 7 8 9; do printf 'This English paragraph still needs translating into Hebrew.\n\n'; done
    printf 'פסקה אחת בלבד כבר תורגמה לעברית.\n'
  } > "${WORK}/docs/half.md"
  cd "${WORK}" && python3 scripts/translation-status.py
  grep -q -- "- 🟡.*docs/half.md" "${WORK}/docs/translation-status.md"
}

@test "check נכשל כשהמפה לא מעודכנת" {
  printf '# כותרת\n\nפסקה בעברית.\n' > "${WORK}/docs/heb.md"
  cd "${WORK}" && python3 scripts/translation-status.py
  printf '# Title\n\nA new English document that the map does not know about yet.\n' > "${WORK}/docs/new.md"
  cd "${WORK}" && run python3 scripts/translation-status.py --check
  [ "$status" -eq 1 ]
}
