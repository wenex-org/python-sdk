import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.content.tickets import Ticket, TicketDto


class TicketsService[Properties: Any](RestfulService[Ticket[Properties], TicketDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("content/tickets", client=client, path_prefix=path_prefix)
