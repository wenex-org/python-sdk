__all__ = [
  "Client",
  "FilesService",
  "StatsService",
]

import httpx

from typing import Optional, Any

from .files import FilesService
from .stats import StatsService


class Client[Properties: Any]:
  _files: Optional[FilesService[Properties]]
  _stats: Optional[StatsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def files(self):
    self._files = self._files or FilesService[Properties](self.client, self.path_prefix)
    return self._files

  @property
  def stats(self):
    self._stats = self._stats or StatsService[Properties](self.client, self.path_prefix)
    return self._stats
