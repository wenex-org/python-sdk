__all__ = [
  "Client",
  "ConfigsService",
  "SettingsService",
]

import httpx

from typing import Optional, Any

from .configs import ConfigsService
from .settings import SettingsService


class Client[T: Any, Properties: Any]:
  _configs: Optional[ConfigsService[T, Properties]]
  _settings: Optional[SettingsService[T, Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def configs(self):
    self._configs = self._configs or ConfigsService[T, Properties](self.client, self.path_prefix)
    return self._configs

  @property
  def settings(self):
    self._settings = self._settings or SettingsService[T, Properties](self.client, self.path_prefix)
    return self._settings
