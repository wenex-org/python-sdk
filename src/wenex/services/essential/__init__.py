__all__ = [
  "Client",
  "SagasService",
]

import httpx

from typing import Optional, Any

from .sagas import SagasService


class Client[Properties: Any]:
  _sagas: Optional[SagasService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def sagas(self):
    self._sagas = self._sagas or SagasService[Properties](self.client, self.path_prefix)
    return self._sagas
