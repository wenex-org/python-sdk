__all__ = [
  "Client",
  "DevicesService",
  "MetricsService",
  "SensorsService",
]

import httpx

from typing import Optional, Any

from .devices import DevicesService
from .metrics import MetricsService
from .sensors import SensorsService


class Client[Properties: Any]:
  _devices: Optional[DevicesService[Properties]]
  _metrics: Optional[MetricsService[Properties]]
  _sensors: Optional[SensorsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def devices(self):
    self._devices = self._devices or DevicesService[Properties](self.client, self.path_prefix)
    return self._devices

  @property
  def metrics(self):
    self._metrics = self._metrics or MetricsService[Properties](self.client, self.path_prefix)
    return self._metrics

  @property
  def sensors(self):
    self._sensors = self._sensors or SensorsService[Properties](self.client, self.path_prefix)
    return self._sensors
