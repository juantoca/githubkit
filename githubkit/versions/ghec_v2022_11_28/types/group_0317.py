"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


from .group_0001 import SimpleUserType
from .group_0006 import IntegrationType


class StateChangeIssueEventType(TypedDict):
    """State Change Issue Event

    State Change Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: str
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: Union[None, IntegrationType, None]
    state_reason: NotRequired[Union[str, None]]


__all__ = ("StateChangeIssueEventType",)
