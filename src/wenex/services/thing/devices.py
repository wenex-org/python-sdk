import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.thing.devices import Device, DeviceDto


class DevicesService[Properties: Any](RestfulService[Device[Properties], DeviceDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("thing/devices", client=client, path_prefix=path_prefix)
