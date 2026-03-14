import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.interfaces import Result
from ...common.core.classes import RestfulService
from ...common.interfaces.special.stats import Stat, StatDto, StatCollectDto


class StatsService[Properties: Any](RestfulService[Stat[Properties], StatDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("special/stats", client=client, path_prefix=path_prefix)

  def collect(self, data: StatCollectDto, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("collect"), data=data, **{**config, "params": params})
    return response if full_response else response["items"]

  def stackup(
    self, data: StatCollectDto, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Result:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("stackup"), data=data, **{**config, "params": params})
    return response if full_response else response["result"]
