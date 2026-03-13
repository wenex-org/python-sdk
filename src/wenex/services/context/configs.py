import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.context.configs import Config, ConfigDto


class ConfigsService[T: Any, Properties: Any](RestfulService[Config[T, Properties], ConfigDto[T, Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("context/configs", client=client, path_prefix=path_prefix)
