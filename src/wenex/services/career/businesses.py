import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.businesses import Business, BusinessDto


class BusinessesService[Properties: Any](RestfulService[Business[Properties], BusinessDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/businesses", client=client, path_prefix=path_prefix)
