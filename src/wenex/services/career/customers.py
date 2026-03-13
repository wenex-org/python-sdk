import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.customers import Customer, CustomerDto


class CustomersService[Properties: Any](RestfulService[Customer[Properties], CustomerDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/customers", client=client, path_prefix=path_prefix)
