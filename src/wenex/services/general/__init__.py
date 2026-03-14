__all__ = [
  "Client",
  "EventsService",
  "CommentsService",
  "ArtifactsService",
  "WorkflowsService",
  "ActivitiesService",
]

import httpx

from typing import Optional, Any

from .events import EventsService
from .comments import CommentsService
from .artifacts import ArtifactsService
from .workflows import WorkflowsService
from .activities import ActivitiesService


class Client[Properties: Any]:
  _events: Optional[EventsService[Properties]]
  _comments: Optional[CommentsService[Properties]]
  _artifacts: Optional[ArtifactsService[Any, Properties]]
  _workflows: Optional[WorkflowsService[Any, Any, Properties]]
  _activities: Optional[ActivitiesService[Any, Any, Properties]]

  def __init__(self, client: httpx.Client, path_prefix: str = "/"):
    self.client, self.path_prefix = client, path_prefix

  @property
  def events(self):
    self._events = self._events or EventsService[Properties](self.client, self.path_prefix)
    return self._events

  @property
  def comments(self):
    self._comments = self._comments or CommentsService[Properties](self.client, self.path_prefix)
    return self._comments

  @property
  def artifacts(self):
    self._artifacts = self._artifacts or ArtifactsService[Any, Properties](self.client, self.path_prefix)
    return self._artifacts

  @property
  def workflows(self):
    self._workflows = self._workflows or WorkflowsService[Any, Any, Properties](self.client, self.path_prefix)
    return self._workflows

  @property
  def activities(self):
    self._activities = self._activities or ActivitiesService[Any, Any, Properties](self.client, self.path_prefix)
    return self._activities
