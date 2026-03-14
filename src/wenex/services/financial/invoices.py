import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.financial.invoices import Invoice, InvoiceDto


class InvoicesService[Properties: Any](RestfulService[Invoice[Properties], InvoiceDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("financial/invoices", client=client, path_prefix=path_prefix)

  def payment(self, id: str, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli, query_or_filter=filter)
    response = super().get(self.url(f"{id}/payment"), **{**config, "params": params})
    return response if full_response else response["data"]
