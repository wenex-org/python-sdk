__all__ = [
  "Client",
  "NotesService",
  "PostsService",
  "TicketsService",
]

import httpx

from typing import Optional, Any

from .notes import NotesService
from .posts import PostsService
from .tickets import TicketsService


class Client[Properties: Any]:
  _notes: Optional[NotesService[Properties]]
  _posts: Optional[PostsService[Properties]]
  _tickets: Optional[TicketsService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def notes(self):
    self._notes = self._notes or NotesService[Properties](self.client, self.path_prefix)
    return self._notes

  @property
  def posts(self):
    self._posts = self._posts or PostsService[Properties](self.client, self.path_prefix)
    return self._posts

  @property
  def tickets(self):
    self._tickets = self._tickets or TicketsService[Properties](self.client, self.path_prefix)
    return self._tickets
