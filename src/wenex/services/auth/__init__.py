__all__ = [
  "Client",
  "AptsService",
  "AuthsService",
  "GrantsService",
]

import httpx

from typing import Optional, Any

from .apts import AptsService
from .auths import AuthsService
from .grants import GrantsService


class Client[Properties: Any]:
  _apts: Optional[AptsService[Properties]]
  _auths: Optional[AuthsService]
  _grants: Optional[GrantsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def apts(self):
    self._apts = self._apts or AptsService[Properties](self.client, self.path_prefix)
    return self._apts

  @property
  def auths(self):
    self._auths = self._auths or AuthsService(self.client, self.path_prefix)
    return self._auths

  @property
  def grants(self):
    self._grants = self._grants or GrantsService[Properties](self.client, self.path_prefix)
    return self._grants
