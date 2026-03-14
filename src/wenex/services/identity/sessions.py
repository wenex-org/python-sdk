import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.identity.sessions import Session, SessionDto


class SessionsService[Properties: Any](RestfulService[Session[Properties], SessionDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("identity/sessions", client=client, path_prefix=path_prefix)
