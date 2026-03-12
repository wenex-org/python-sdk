import httpx

from typing import Optional, Any

from ...common.core.providers import RequestService
from ...common.core.interfaces.auth import JwtToken
from ...common.interfaces.auth.auths import AuthCheck
from ...common.core.interfaces.serializer import Result
from ...common.interfaces.auth.auths import AuthorizationRequest, AuthorizationResponse
from ...common.interfaces.auth.auths import AuthenticationRequest, AuthenticationResponse


class AuthsService(RequestService):
  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.path_prefix = path_prefix
    super().__init__(client=client)

  def url(self, path: str, prefix: Optional[str] = None):
    prefix = prefix or self.path_prefix or "/"
    return f"{prefix}auth/{path}"

  def check(self, data: AuthCheck, **config: Any) -> Result:
    return super().post(self.url("check"), data=data, **config)

  def token(self, data: AuthenticationRequest, **config: Any) -> AuthenticationResponse:
    return super().post(self.url("token"), data=data, **config)

  def verify(self, **config: Any) -> JwtToken:
    return self.get(self.url("verify"), **config)

  def logout(self, **config: Any) -> Result:
    return self.get(self.url("logout"), **config)

  def can(self, data: AuthorizationRequest, **config: Any) -> AuthorizationResponse:
    return self.post(self.url("can"), data=data, **config)
