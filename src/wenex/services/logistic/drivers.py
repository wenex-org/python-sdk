import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.logistic.drivers import Driver, DriverDto


class DriversService[Properties: Any](RestfulService[Driver[Properties], DriverDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("logistic/drivers", client=client, path_prefix=path_prefix)
