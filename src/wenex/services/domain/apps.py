import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.domain.apps import App, AppDto


class AppsService[Properties: Any](RestfulService[App[Properties], AppDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("domain/apps", client=client, path_prefix=path_prefix)
