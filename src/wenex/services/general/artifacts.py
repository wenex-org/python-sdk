import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.general.artifacts import Artifact, ArtifactDto


class ArtifactsService[T: Any, Properties: Any](RestfulService[Artifact[T, Properties], ArtifactDto[T, Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("general/artifacts", client=client, path_prefix=path_prefix)
