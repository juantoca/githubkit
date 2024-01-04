"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class SimpleUserType(TypedDict):
    """Simple User

    A GitHub user.
    """

    name: NotRequired[Union[str, None]]
    email: NotRequired[Union[str, None]]
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: Union[str, None]
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    starred_at: NotRequired[str]


__all__ = ("SimpleUserType",)
