import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.stores import Store, StoreDto


class StoresService[Properties: Any](RestfulService[Store[Properties], StoreDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/stores", client=client, path_prefix=path_prefix)
