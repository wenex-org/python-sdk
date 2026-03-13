import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.domain.clients import Client, ClientDto


class ClientsService[Properties: Any](RestfulService[Client[Properties], ClientDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("domain/clients", client=client, path_prefix=path_prefix)
