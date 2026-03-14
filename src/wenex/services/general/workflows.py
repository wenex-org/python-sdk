import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.general.workflows import Workflow, WorkflowDto


class WorkflowsService[D: Any, V: Any, Properties: Any](RestfulService[Workflow[D, V, Properties], WorkflowDto[D, V, Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("general/workflows", client=client, path_prefix=path_prefix)
