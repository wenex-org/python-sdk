import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.touch.pushes import Push, PushDto, PusHistorySendDto


class PushesService[Properties: Any](RestfulService[Push[Properties], PushDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("touch/pushes", client=client, path_prefix=path_prefix)

  def send(self, data: PusHistorySendDto, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("send"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]
