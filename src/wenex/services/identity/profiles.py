import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.identity.profiles import Profile, ProfileDto


class ProfilesService[Properties: Any](RestfulService[Profile[Properties], ProfileDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("identity/profiles", client=client, path_prefix=path_prefix)
