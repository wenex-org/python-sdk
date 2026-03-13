import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.context.settings import Setting, SettingDto


class SettingsService[T: Any, Properties: Any](RestfulService[Setting[T, Properties], SettingDto[T, Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("context/settings", client=client, path_prefix=path_prefix)
