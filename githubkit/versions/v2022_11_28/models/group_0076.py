"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0075 import TeamSimple


class Team(GitHubModel):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    id: int = Field()
    node_id: str = Field()
    name: str = Field()
    slug: str = Field()
    description: Union[str, None] = Field()
    privacy: Missing[str] = Field(default=UNSET)
    notification_setting: Missing[str] = Field(default=UNSET)
    permission: str = Field()
    permissions: Missing[TeamPropPermissions] = Field(default=UNSET)
    url: str = Field()
    html_url: str = Field()
    members_url: str = Field()
    repositories_url: str = Field()
    parent: Union[None, TeamSimple] = Field()


class TeamPropPermissions(GitHubModel):
    """TeamPropPermissions"""

    pull: bool = Field()
    triage: bool = Field()
    push: bool = Field()
    maintain: bool = Field()
    admin: bool = Field()


model_rebuild(Team)
model_rebuild(TeamPropPermissions)

__all__ = (
    "Team",
    "TeamPropPermissions",
)
