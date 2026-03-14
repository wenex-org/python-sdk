import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.thing.metrics import Metric, MetricDto


class MetricsService[Properties: Any](RestfulService[Metric[Properties], MetricDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("thing/metrics", client=client, path_prefix=path_prefix)
