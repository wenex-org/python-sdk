import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.logistic.vehicles import Vehicle, VehicleDto


class VehiclesService[Properties: Any](RestfulService[Vehicle[Properties], VehicleDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("logistic/vehicles", client=client, path_prefix=path_prefix)
