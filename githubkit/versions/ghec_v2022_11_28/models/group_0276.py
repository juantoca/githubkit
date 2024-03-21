"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0005 import Integration


class UnassignedIssueEvent(GitHubModel):
    """Unassigned Issue Event

    Unassigned Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: str = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    assignee: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    assigner: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(UnassignedIssueEvent)

__all__ = ("UnassignedIssueEvent",)
