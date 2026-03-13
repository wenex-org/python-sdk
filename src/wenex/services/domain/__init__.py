__all__ = [
  "Client",
  "AppsService",
  "ClientsService",
]

import httpx

from typing import Optional, Any

from .apps import AppsService
from .clients import ClientsService


class Client[Properties: Any]:
  _apps: Optional[AppsService[Properties]]
  _clients: Optional[ClientsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def apps(self):
    self._apps = self._apps or AppsService[Properties](self.client, self.path_prefix)
    return self._apps

  @property
  def clients(self):
    self._clients = self._clients or ClientsService[Properties](self.client, self.path_prefix)
    return self._clients
