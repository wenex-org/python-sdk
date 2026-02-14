import os
import dotenv  # type: ignore

from httpx import Client
from wenex.common.core.classes.restful import RestfulService


dotenv.load_dotenv()

APT_TOKEN = os.getenv("TEST_APT_TOKEN", "")
PLATFORM_URL = os.getenv("TEST_PLATFORM_URL", "http://localhost:3010")

client = Client(base_url=PLATFORM_URL, headers={"Authorization": f"Bearer {APT_TOKEN}"})
service = RestfulService("auth/grants", client)


def test_count():
  total = service.count({})
  assert total == 1

  total = service.count({}, brotli=True)
  assert total == 1

  data = service.count({}, full_response=True)
  assert data == {"total": 1}
