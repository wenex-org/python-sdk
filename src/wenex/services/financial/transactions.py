import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.financial.transactions import Transaction, TransactionDto, TransactionInitDto


class TransactionsService[Properties: Any](RestfulService[Transaction[Properties], TransactionDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("financial/transactions", client=client, path_prefix=path_prefix)

  def init(
    self, data: TransactionInitDto[Properties], brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("init"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]

  def abort(self, id: str, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli, query_or_filter=filter)
    response = super().get(self.url(f"{id}/abort"), **{**config, "params": params})
    return response if full_response else response["data"]

  def verify(self, id: str, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli, query_or_filter=filter)
    response = super().get(self.url(f"{id}/verify"), **{**config, "params": params})
    return response if full_response else response["data"]
