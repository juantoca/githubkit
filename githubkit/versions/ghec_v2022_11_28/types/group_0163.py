"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0060 import ReactionRollupType


class TeamDiscussionType(TypedDict):
    """Team Discussion

    A team discussion is a persistent record of a free-form conversation within a
    team.
    """

    author: Union[None, SimpleUserType]
    body: str
    body_html: str
    body_version: str
    comments_count: int
    comments_url: str
    created_at: datetime
    last_edited_at: Union[datetime, None]
    html_url: str
    node_id: str
    number: int
    pinned: bool
    private: bool
    team_url: str
    title: str
    updated_at: datetime
    url: str
    reactions: NotRequired[ReactionRollupType]


__all__ = ("TeamDiscussionType",)
