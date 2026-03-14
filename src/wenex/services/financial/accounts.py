import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.financial.accounts import Account, AccountDto


class AccountsService[Properties: Any](RestfulService[Account[Properties], AccountDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("financial/accounts", client=client, path_prefix=path_prefix)
