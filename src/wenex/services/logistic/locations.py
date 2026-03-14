import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.logistic.locations import Location, LocationDto, AddressLookup, GeocodeLookup


class LocationsService[Properties: Any](RestfulService[Location[Properties], LocationDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("logistic/locations", client=client, path_prefix=path_prefix)

  def address_lookup(
    self, data: AddressLookup, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("address-lookup"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]

  def geocode_lookup(
    self, data: GeocodeLookup, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("geocode-lookup"), data=data, **{**config, "params": params})
    return response if full_response else response["items"]
