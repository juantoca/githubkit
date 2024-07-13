"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0038 import ReactionRollup


class TeamDiscussion(GitHubModel):
    """Team Discussion

    A team discussion is a persistent record of a free-form conversation within a
    team.
    """

    author: Union[None, SimpleUser] = Field()
    body: str = Field(description="The main text of the discussion.")
    body_html: str = Field()
    body_version: str = Field(
        description="The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server."
    )
    comments_count: int = Field()
    comments_url: str = Field()
    created_at: datetime = Field()
    last_edited_at: Union[datetime, None] = Field()
    html_url: str = Field()
    node_id: str = Field()
    number: int = Field(description="The unique sequence number of a team discussion.")
    pinned: bool = Field(
        description="Whether or not this discussion should be pinned for easy retrieval."
    )
    private: bool = Field(
        description="Whether or not this discussion should be restricted to team members and organization owners."
    )
    team_url: str = Field()
    title: str = Field(description="The title of the discussion.")
    updated_at: datetime = Field()
    url: str = Field()
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")


model_rebuild(TeamDiscussion)

__all__ = ("TeamDiscussion",)
