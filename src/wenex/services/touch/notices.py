import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.touch.notices import Notice, NoticeDto


class NoticesService[Properties: Any](RestfulService[Notice[Properties], NoticeDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("touch/notices", client=client, path_prefix=path_prefix)
