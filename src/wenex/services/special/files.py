import io
import httpx

from typing import Optional, Literal, Any


from ...common.core.utils import get_params
from ...common.core.classes import RestfulService
from ...common.interfaces.special.files import File, FileDto, ShareLinkReq


class FilesService[Properties: Any](RestfulService[File[Properties], FileDto[Properties]]):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    super().__init__("special/files", client=client, path_prefix=path_prefix)

  def download(self, id: str, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().get(self.url(f"download/{id}"), **{**config, "params": params})
    return response if full_response else response["content"]

  def share(
    self, id: str, data: ShareLinkReq, brotli: Optional[Any] = None, full_response: Optional[bool] = None, **config: Any
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)
    response = super().post(self.url(f"{id}/share"), data=data, **{**config, "params": params})
    return response if full_response else response["data"]

  def upload(
    self,
    items: list[dict[str, Any]],
    scope: Literal["private", "public"],
    brotli: Optional[Any] = None,
    full_response: Optional[bool] = None,
    **config: Any,
  ) -> Any:
    params = get_params(config=config, brotli_cfg=brotli)

    # Build httpx-compatible files list (NO FormData needed in Python)
    files: list[tuple[str, tuple[str | None, bytes | io.BytesIO]]] = []
    for item in items:
      filename = item.get("filename")
      value = item["value"]  # must be bytes
      files.append(("file", (filename, value)))
    # IMPORTANT: httpx automatically adds the correct
    # "multipart/form-data; boundary=xxx" header.
    # Setting Content-Type manually (like in the TS version) WILL break the upload!
    if "headers" in config:
      config["headers"] = dict(config["headers"])  # shallow copy
      config["headers"].pop("Content-Type", None)  # remove if present
    config["files"] = files

    response = super().post(self.url(f"upload/{scope}"), data=None, **{**config, "params": params})
    return response if full_response else response["items"]
