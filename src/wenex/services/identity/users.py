import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.identity.users import User, UserDto


class UsersService[Properties: Any](RestfulService[User[Properties], UserDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("identity/users", client=client, path_prefix=path_prefix)
