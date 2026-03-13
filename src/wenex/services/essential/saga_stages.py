import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.essential.sagas.stages import SagaStage, SagaStageDto


class SagaStagesService[Properties: Any](RestfulService[SagaStage[Properties], SagaStageDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("essential/saga-stages", client=client, path_prefix=path_prefix)
