"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict


from .group_0331 import PullRequestPropBasePropRepoType


class PullRequestPropBaseType(TypedDict):
    """PullRequestPropBase"""

    label: str
    ref: str
    repo: PullRequestPropBasePropRepoType
    sha: str
    user: PullRequestPropBasePropUserType


class PullRequestPropBasePropUserType(TypedDict):
    """PullRequestPropBasePropUser"""

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: Union[str, None]
    html_url: str
    id: int
    node_id: str
    login: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str


__all__ = (
    "PullRequestPropBaseType",
    "PullRequestPropBasePropUserType",
)
