"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0039 import IssueType
from .group_0040 import IssueCommentType


class EventPropPayloadType(TypedDict):
    """EventPropPayload"""

    action: NotRequired[str]
    issue: NotRequired[IssueType]
    comment: NotRequired[IssueCommentType]
    pages: NotRequired[List[EventPropPayloadPropPagesItemsType]]


class EventPropPayloadPropPagesItemsType(TypedDict):
    """EventPropPayloadPropPagesItems"""

    page_name: NotRequired[str]
    title: NotRequired[str]
    summary: NotRequired[Union[str, None]]
    action: NotRequired[str]
    sha: NotRequired[str]
    html_url: NotRequired[str]


class EventType(TypedDict):
    """Event

    Event
    """

    id: str
    type: Union[str, None]
    actor: ActorType
    repo: EventPropRepoType
    org: NotRequired[ActorType]
    payload: EventPropPayloadType
    public: bool
    created_at: Union[datetime, None]


class ActorType(TypedDict):
    """Actor

    Actor
    """

    id: int
    login: str
    display_login: NotRequired[str]
    gravatar_id: Union[str, None]
    url: str
    avatar_url: str


class EventPropRepoType(TypedDict):
    """EventPropRepo"""

    id: int
    name: str
    url: str


__all__ = (
    "EventPropPayloadType",
    "EventPropPayloadPropPagesItemsType",
    "EventType",
    "ActorType",
    "EventPropRepoType",
)
