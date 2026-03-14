import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.logistic.cargoes import Cargo, CargoDto


class CargoesService[Properties: Any](RestfulService[Cargo[Properties], CargoDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("logistic/cargoes", client=client, path_prefix=path_prefix)
