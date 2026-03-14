__all__ = [
  "Client",
  "CargoesService",
  "DriversService",
  "TravelsService",
  "VehiclesService",
  "LocationsService",
]

import httpx

from typing import Optional, Any

from .cargoes import CargoesService
from .drivers import DriversService
from .travels import TravelsService
from .vehicles import VehiclesService
from .locations import LocationsService


class Client[Properties: Any]:
  _cargoes: Optional[CargoesService[Properties]]
  _drivers: Optional[DriversService[Properties]]
  _travels: Optional[TravelsService[Properties]]
  _vehicles: Optional[VehiclesService[Properties]]
  _locations: Optional[LocationsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def cargoes(self):
    self._cargoes = self._cargoes or CargoesService[Properties](self.client, self.path_prefix)
    return self._cargoes

  @property
  def drivers(self):
    self._drivers = self._drivers or DriversService[Properties](self.client, self.path_prefix)
    return self._drivers

  @property
  def travels(self):
    self._travels = self._travels or TravelsService[Properties](self.client, self.path_prefix)
    return self._travels

  @property
  def vehicles(self):
    self._vehicles = self._vehicles or VehiclesService[Properties](self.client, self.path_prefix)
    return self._vehicles

  @property
  def locations(self):
    self._locations = self._locations or LocationsService[Properties](self.client, self.path_prefix)
    return self._locations
