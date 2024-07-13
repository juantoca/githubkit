"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0006 import Integration


class RenamedIssueEvent(GitHubModel):
    """Renamed Issue Event

    Renamed Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["renamed"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration, None] = Field()
    rename: RenamedIssueEventPropRename = Field()


class RenamedIssueEventPropRename(GitHubModel):
    """RenamedIssueEventPropRename"""

    from_: str = Field(alias="from")
    to: str = Field()


model_rebuild(RenamedIssueEvent)
model_rebuild(RenamedIssueEventPropRename)

__all__ = (
    "RenamedIssueEvent",
    "RenamedIssueEventPropRename",
)
