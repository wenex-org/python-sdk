import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.conjoint.members import Member, MemberDto


class MembersService[Properties: Any](RestfulService[Member[Properties], MemberDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("conjoint/members", client=client, path_prefix=path_prefix)
