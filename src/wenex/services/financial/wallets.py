import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.financial.wallets import Wallet, WalletDto


class WalletsService[Properties: Any](RestfulService[Wallet[Properties], WalletDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("financial/wallets", client=client, path_prefix=path_prefix)
