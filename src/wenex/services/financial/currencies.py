import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.financial.currencies import Currency, CurrencyDto


class CurrenciesService[Properties: Any](RestfulService[Currency[Properties], CurrencyDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("financial/currencies", client=client, path_prefix=path_prefix)
