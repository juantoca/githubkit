"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0364 import DiscussionType
from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookDiscussionCommentDeletedType(TypedDict):
    """discussion_comment deleted event"""

    action: Literal["deleted"]
    comment: WebhookDiscussionCommentDeletedPropCommentType
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookDiscussionCommentDeletedPropCommentType(TypedDict):
    """WebhookDiscussionCommentDeletedPropComment"""

    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: str
    child_comment_count: int
    created_at: str
    discussion_id: int
    html_url: str
    id: int
    node_id: str
    parent_id: Union[int, None]
    reactions: WebhookDiscussionCommentDeletedPropCommentPropReactionsType
    repository_url: str
    updated_at: str
    user: Union[WebhookDiscussionCommentDeletedPropCommentPropUserType, None]


class WebhookDiscussionCommentDeletedPropCommentPropReactionsType(TypedDict):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookDiscussionCommentDeletedPropCommentPropUserType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookDiscussionCommentDeletedType",
    "WebhookDiscussionCommentDeletedPropCommentType",
    "WebhookDiscussionCommentDeletedPropCommentPropReactionsType",
    "WebhookDiscussionCommentDeletedPropCommentPropUserType",
)
