import httpx

from typing import Any

from ...common.core.classes import RestfulService
from ...common.interfaces.general.comments import Comment, CommentDto


class CommentsService[Properties: Any](RestfulService[Comment[Properties], CommentDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("general/comments", client=client, path_prefix=path_prefix)
