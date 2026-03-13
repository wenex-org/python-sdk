import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.essential.sagas import Saga, SagaDto, SagaStartDto, SagaStageAddDto

from .saga_stages import SagaStagesService


class SagasService[Properties: Any](RestfulService[Saga[Properties], SagaDto[Properties]]):
  _stages: Optional[SagaStagesService[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("essential/sagas", client=client, path_prefix=path_prefix)

  def start(self, data: SagaStartDto, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("start"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]

  def add(self, data: SagaStageAddDto, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url("add"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]

  def abort(self, id: str, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().get(self.url(f"{id}/abort"), **{**config, "params": params})
    return response if full_response else response["data"]

  def commit(self, id: str, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().get(self.url(f"{id}/commit"), **{**config, "params": params})
    return response if full_response else response["data"]

  @property
  def stages(self):
    self._stages = self._stages or SagaStagesService[Properties](self.client, self.path_prefix)
    return self._stages
