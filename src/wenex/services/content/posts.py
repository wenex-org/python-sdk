import httpx

from typing import Optional, Any

from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.core.interfaces.mongo import Filter
from ...common.core.interfaces.elastic import SearchRequest
from ...common.interfaces.content.posts import Post, PostDto


class PostsService[Properties: Any](RestfulService[Post[Properties], PostDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("content/posts", client=client, path_prefix=path_prefix)

  def search(
    self, request: SearchRequest, filter: Filter, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli, query_or_filter=filter)
    response = super().post(self.url("search"), data=request, **{**config, "params": params})
    return response if full_response else response["data"]
