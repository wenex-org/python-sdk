import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.services import Service, ServiceDto


class ServicesService[Properties: Any](RestfulService[Service[Properties], ServiceDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/services", client=client, path_prefix=path_prefix)
