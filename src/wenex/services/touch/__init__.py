__all__ = [
  "Client",
  "SmssService",
  "EmailsService",
  "PushesService",
  "NoticesService",
]

import httpx

from typing import Optional, Any

from .smss import SmssService
from .emails import EmailsService
from .pushes import PushesService
from .notices import NoticesService


class Client[Properties: Any]:
  _smss: Optional[SmssService[Any, Properties]]
  _emails: Optional[EmailsService[Properties]]
  _pushes: Optional[PushesService[Properties]]
  _notices: Optional[NoticesService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def smss(self):
    self._smss = self._smss or SmssService[Any, Properties](self.client, self.path_prefix)
    return self._smss

  @property
  def emails(self):
    self._emails = self._emails or EmailsService[Properties](self.client, self.path_prefix)
    return self._emails

  @property
  def pushes(self):
    self._pushes = self._pushes or PushesService[Properties](self.client, self.path_prefix)
    return self._pushes

  @property
  def notices(self):
    self._notices = self._notices or NoticesService[Properties](self.client, self.path_prefix)
    return self._notices
