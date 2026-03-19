__all__ = [
  "AuthClient",
  "CareerClient",
  "ConjointClient",
  "ContentClient",
  "ContextClient",
  "DomainClient",
  "EssentialClient",
  "FinancialClient",
  "GeneralClient",
  "IdentityClient",
  "LogisticClient",
  "SpecialClient",
  "ThingClient",
  "TouchClient",
]

import httpx

from typing import Optional, Any

from .services import (
  AuthClient,
  CareerClient,
  ConjointClient,
  ContentClient,
  ContextClient,
  DomainClient,
  EssentialClient,
  FinancialClient,
  GeneralClient,
  IdentityClient,
  LogisticClient,
  SpecialClient,
  ThingClient,
  TouchClient,
)

from .common.core.classes import GraphqlService


class Platform[Properties: Any]:
  _graphql: Optional[GraphqlService]

  _auth: Optional[AuthClient[Properties]]
  _context: Optional[ContextClient[Any, Properties]]
  _domain: Optional[DomainClient[Properties]]
  _essential: Optional[EssentialClient[Properties]]
  _financial: Optional[FinancialClient[Properties]]
  _general: Optional[GeneralClient[Properties]]
  _identity: Optional[IdentityClient[Properties]]
  _special: Optional[SpecialClient[Properties]]
  _touch: Optional[TouchClient[Properties]]
  _content: Optional[ContentClient[Properties]]
  _logistic: Optional[LogisticClient[Properties]]
  _conjoint: Optional[ConjointClient[Properties]]
  _career: Optional[CareerClient[Properties]]
  _thing: Optional[ThingClient[Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def auth(self):
    self._auth = self._auth or AuthClient[Properties](self.client, self.path_prefix)
    return self._auth

  @property
  def context(self):
    self._context = self._context or ContextClient[Any, Properties](self.client, self.path_prefix)
    return self._context

  @property
  def domain(self):
    self._domain = self._domain or DomainClient[Properties](self.client, self.path_prefix)
    return self._domain

  @property
  def essential(self):
    self._essential = self._essential or EssentialClient[Properties](self.client, self.path_prefix)
    return self._essential

  @property
  def financial(self):
    self._financial = self._financial or FinancialClient[Properties](self.client, self.path_prefix)
    return self._financial

  @property
  def general(self):
    self._general = self._general or GeneralClient[Properties](self.client, self.path_prefix)
    return self._general

  @property
  def identity(self):
    self._identity = self._identity or IdentityClient[Properties](self.client, self.path_prefix)
    return self._identity

  @property
  def special(self):
    self._special = self._special or SpecialClient[Properties](self.client, self.path_prefix)
    return self._special

  @property
  def touch(self):
    self._touch = self._touch or TouchClient[Properties](self.client, self.path_prefix)
    return self._touch

  @property
  def content(self):
    self._content = self._content or ContentClient[Properties](self.client, self.path_prefix)
    return self._content

  @property
  def logistic(self):
    self._logistic = self._logistic or LogisticClient[Properties](self.client, self.path_prefix)
    return self._logistic

  @property
  def conjoint(self):
    self._conjoint = self._conjoint or ConjointClient[Properties](self.client, self.path_prefix)
    return self._conjoint

  @property
  def career(self):
    self._career = self._career or CareerClient[Properties](self.client, self.path_prefix)
    return self._career

  @property
  def thing(self):
    self._thing = self._thing or ThingClient[Properties](self.client, self.path_prefix)
    return self._thing

  @property
  def graphql(self):
    self._graphql = self._graphql or GraphqlService(self.client, self.path_prefix)
    return self._graphql
