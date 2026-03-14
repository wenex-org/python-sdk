__all__ = [
  "Client",
  "UsersService",
  "ProfilesService",
  "SessionsService",
]

import httpx

from typing import Optional, Any

from .users import UsersService
from .profiles import ProfilesService
from .sessions import SessionsService


class Client[Properties: Any]:
  _users: Optional[UsersService[Properties]]
  _profiles: Optional[ProfilesService[Properties]]
  _sessions: Optional[SessionsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def users(self):
    self._users = self._users or UsersService[Properties](self.client, self.path_prefix)
    return self._users

  @property
  def profiles(self):
    self._profiles = self._profiles or ProfilesService[Properties](self.client, self.path_prefix)
    return self._profiles

  @property
  def sessions(self):
    self._sessions = self._sessions or SessionsService[Properties](self.client, self.path_prefix)
    return self._sessions
