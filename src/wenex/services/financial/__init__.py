__all__ = [
  "Client",
  "WalletsService",
  "AccountsService",
  "InvoicesService",
  "CurrenciesService",
  "TransactionsService",
]

import httpx

from typing import Optional, Any

from .wallets import WalletsService
from .accounts import AccountsService
from .invoices import InvoicesService
from .currencies import CurrenciesService
from .transactions import TransactionsService


class Client[Properties: Any]:
  _wallets: Optional[WalletsService[Properties]]
  _accounts: Optional[AccountsService[Properties]]
  _invoices: Optional[InvoicesService[Properties]]
  _currencies: Optional[CurrenciesService[Properties]]
  _transactions: Optional[TransactionsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def wallets(self):
    self._wallets = self._wallets or WalletsService[Properties](self.client, self.path_prefix)
    return self._wallets

  @property
  def accounts(self):
    self._accounts = self._accounts or AccountsService[Properties](self.client, self.path_prefix)
    return self._accounts

  @property
  def invoices(self):
    self._invoices = self._invoices or InvoicesService[Properties](self.client, self.path_prefix)
    return self._invoices

  @property
  def currencies(self):
    self._currencies = self._currencies or CurrenciesService[Properties](self.client, self.path_prefix)
    return self._currencies

  @property
  def transactions(self):
    self._transactions = self._transactions or TransactionsService[Properties](self.client, self.path_prefix)
    return self._transactions
