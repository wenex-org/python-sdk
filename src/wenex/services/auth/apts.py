import httpx

from typing import Optional, Any

from ...common.core.classes import RestfulService
from ...common.core.interfaces.mongo import Query
from ...common.interfaces.auth.apts import Apt, AptDto


class AptsService[Properties: Any](RestfulService[Apt[Properties], AptDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("auth/apts", client=client, path_prefix=path_prefix)

  def update_bulk(
    self,
    data: Optional[AptDto[Properties]],
    query: Query,
    brotli: Optional[Any] = None,
    full_response: Optional[bool] = None,
    **config: Any,
  ) -> Any:
    """
    Method not implemented.
    """
    raise Exception("Method not implemented.")

  def update_by_id(
    self,
    id: str,
    data: Optional[AptDto[Properties]],
    brotli: Optional[Any] = None,
    full_response: Optional[bool] = None,
    **config: Any,
  ) -> Any:
    """
    Method not implemented.
    """
    raise Exception("Method not implemented.")
