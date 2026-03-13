import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.conjoint.contacts import Contact, ContactDto


class ContactsService[Properties: Any](RestfulService[Contact[Properties], ContactDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("conjoint/contacts", client=client, path_prefix=path_prefix)
