from wenex.common.core.decorators.validation.category import is_category


def test_is_category():
  assert is_category("") is False
  assert is_category("for > test") is True
  assert is_category("single-category") is True
