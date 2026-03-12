import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.auth.grants import Grant, GrantDto


class GrantsService[Properties: Any](RestfulService[Grant[Properties], GrantDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("auth/grants", client=client, path_prefix=path_prefix)
