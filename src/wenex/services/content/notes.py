import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.content.notes import Note, NoteDto


class NotesService[Properties: Any](RestfulService[Note[Properties], NoteDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("content/notes", client=client, path_prefix=path_prefix)
