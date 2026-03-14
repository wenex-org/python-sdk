import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.thing.sensors import Sensor, SensorDto


class SensorsService[Properties: Any](RestfulService[Sensor[Properties], SensorDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("thing/sensors", client=client, path_prefix=path_prefix)
