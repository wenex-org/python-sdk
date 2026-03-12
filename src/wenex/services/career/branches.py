import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.career.branches import Branch, BranchDto


class BranchesService[Properties: Any](RestfulService[Branch[Properties], BranchDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("career/branches", client=client, path_prefix=path_prefix)
