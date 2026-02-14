import os
import pytest

from wenex.common.core.collection import COLLECTION, COLL


def test_COLLECTION():
  assert COLLECTION("grants", "auth") == "auth/grants"

  # Unset db test
  with pytest.raises(Exception):
    COLLECTION("grants")

  # Optional db test
  os.environ.update({"PROTOTYPING_APP": "AUTH"})
  assert COLLECTION("grants") == "auth/grants"

  # Invalid app test
  os.environ.update({"PROTOTYPING_APP": "AUTHS"})
  with pytest.raises(Exception):
    COLLECTION("grants")


def test_COLL():
  coll, db = COLL("auth/grants")
  assert coll == "grants" and db == "auth"
