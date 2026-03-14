import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.touch.smss import Sms, SmsDto, SmsSendDto


class SmssService[T: Any, Properties: Any](RestfulService[Sms[T, Properties], SmsDto[T, Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("touch/smss", client=client, path_prefix=path_prefix)

  def send(
    self, data: SmsSendDto[T, Properties], brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("send"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]
