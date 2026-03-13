import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.conjoint.channels import Channel, ChannelDto


class ChannelsService[Properties: Any](RestfulService[Channel[Properties], ChannelDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("conjoint/channels", client=client, path_prefix=path_prefix)
