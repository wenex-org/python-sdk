import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.general.activities import Activity, ActivityDto


class ActivitiesService[T: Any, M: Any, Properties: Any](RestfulService[Activity[T, M, Properties], ActivityDto[T, M, Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("general/activities", client=client, path_prefix=path_prefix)
