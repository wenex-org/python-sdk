__all__ = [
  "Client",
  "MembersService",
  "AccountsService",
  "ChannelsService",
  "ContactsService",
  "MessagesService",
]

import httpx

from typing import Optional, Any

from .members import MembersService
from .accounts import AccountsService
from .channels import ChannelsService
from .contacts import ContactsService
from .messages import MessagesService


class Client[Properties: Any]:
  _members: Optional[MembersService[Properties]]
  _accounts: Optional[AccountsService[Properties]]
  _channels: Optional[ChannelsService[Properties]]
  _contacts: Optional[ContactsService[Properties]]
  _messages: Optional[MessagesService[Any, Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def members(self):
    self._members = self._members or MembersService[Properties](self.client, self.path_prefix)
    return self._members

  @property
  def accounts(self):
    self._accounts = self._accounts or AccountsService[Properties](self.client, self.path_prefix)
    return self._accounts

  @property
  def channels(self):
    self._channels = self._channels or ChannelsService[Properties](self.client, self.path_prefix)
    return self._channels

  @property
  def contacts(self):
    self._contacts = self._contacts or ContactsService[Properties](self.client, self.path_prefix)
    return self._contacts

  @property
  def messages(self):
    self._messages = self._messages or MessagesService[Any, Properties](self.client, self.path_prefix)
    return self._messages
