import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.conjoint.accounts import Account, AccountDto, Credential


class AccountsService[Properties: Any](RestfulService[Account[Properties], AccountDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("conjoint/accounts", client=client, path_prefix=path_prefix)

  def cred(self, **config: Any) -> Credential:
    return super().post(self.url(), **config)
