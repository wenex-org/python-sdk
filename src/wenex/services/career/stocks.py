import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.stocks import Stock, StockDto


class StocksService[Properties: Any](RestfulService[Stock[Properties], StockDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/stocks", client=client, path_prefix=path_prefix)
