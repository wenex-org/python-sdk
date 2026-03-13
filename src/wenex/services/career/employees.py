import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.employees import Employee, EmployeeDto


class EmployeesService[Properties: Any](RestfulService[Employee[Properties], EmployeeDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/employees", client=client, path_prefix=path_prefix)
