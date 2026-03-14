import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.logistic.travels import Travel, TravelDto, RoutingRequest


class TravelsService[Properties: Any](RestfulService[Travel[Properties], TravelDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("logistic/travels", client=client, path_prefix=path_prefix)

  def address_lookup(
    self, data: RoutingRequest, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("routing"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]
