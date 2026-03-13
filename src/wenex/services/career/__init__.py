__all__ = [
  "Client",
  "StoresService",
  "StocksService",
  "BranchesService",
  "ProductsService",
  "ServicesService",
  "CustomersService",
  "EmployeesService",
  "BusinessesService",
]

import httpx

from typing import Optional, Any

from .stores import StoresService
from .stocks import StocksService
from .branches import BranchesService
from .products import ProductsService
from .services import ServicesService
from .customers import CustomersService
from .employees import EmployeesService
from .businesses import BusinessesService


class Client[Properties: Any]:
  _stores: Optional[StoresService[Properties]]
  _stocks: Optional[StocksService[Properties]]
  _branches: Optional[BranchesService[Properties]]
  _products: Optional[ProductsService[Properties]]
  _services: Optional[ServicesService[Properties]]
  _customers: Optional[CustomersService[Properties]]
  _employees: Optional[EmployeesService[Properties]]
  _businesses: Optional[BusinessesService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def stores(self):
    self._stores = self._stores or StoresService[Properties](self.client, self.path_prefix)
    return self._stores

  @property
  def stocks(self):
    self._stocks = self._stocks or StocksService[Properties](self.client, self.path_prefix)
    return self._stocks

  @property
  def branches(self):
    self._branches = self._branches or BranchesService[Properties](self.client, self.path_prefix)
    return self._branches

  @property
  def products(self):
    self._products = self._products or ProductsService[Properties](self.client, self.path_prefix)
    return self._products

  @property
  def services(self):
    self._services = self._services or ServicesService[Properties](self.client, self.path_prefix)
    return self._services

  @property
  def customers(self):
    self._customers = self._customers or CustomersService[Properties](self.client, self.path_prefix)
    return self._customers

  @property
  def employees(self):
    self._employees = self._employees or EmployeesService[Properties](self.client, self.path_prefix)
    return self._employees

  @property
  def businesses(self):
    self._businesses = self._businesses or BusinessesService[Properties](self.client, self.path_prefix)
    return self._businesses
