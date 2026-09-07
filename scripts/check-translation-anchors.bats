#!/usr/bin/env bats
#
# Guards the slug function behind the translation anchor checker. GitHub builds
# a heading's anchor from the rendered text, so emphasis markers disappear while
# an underscore inside a word survives. Getting either half wrong is silent: the
# checker reports a working anchor as broken, or passes a broken one. The repo's
# citation headings are written as `_Book Title_`, so a rule that drops every
# underscore would misreport all of them at once.

REPO_ROOT="${BATS_TEST_DIRNAME}/.."
CHECKER="${REPO_ROOT}/scripts/check-translation-anchors.py"

slug() {
  python3 -c "
import importlib.util, sys
spec = importlib.util.spec_from_file_location('c', '${CHECKER}')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
print(m.slug(sys.argv[1]))
" "$1"
}

@test "emphasis underscores are dropped, as GitHub drops them when rendering" {
  run slug 'Kent Beck, _Test-Driven Development: By Example_, 2002'
  [ "$status" -eq 0 ]
  [ "$output" = 'kent-beck-test-driven-development-by-example-2002' ]
}

@test "an emphasised word mid-heading loses its underscores" {
  run slug 'What is _not_ the long-form doc'
  [ "$status" -eq 0 ]
  [ "$output" = 'what-is-not-the-long-form-doc' ]
}

@test "an underscore inside a word survives" {
  run slug 'The feature_name field'
  [ "$status" -eq 0 ]
  [ "$output" = 'the-feature_name-field' ]
}

@test "backticks and asterisks are still stripped" {
  run slug '**Bold** and `code` heading'
  [ "$status" -eq 0 ]
  [ "$output" = 'bold-and-code-heading' ]
}

@test "a Hebrew heading keeps its letters and drops punctuation" {
  run slug 'הפורמט של סעיף Deferred (YAGNI)'
  [ "$status" -eq 0 ]
  [ "$output" = 'הפורמט-של-סעיף-deferred-yagni' ]
}
