import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.general.events import Event, EventDto


class EventsService[Properties: Any](RestfulService[Event[Properties], EventDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("general/events", client=client, path_prefix=path_prefix)
