"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


from .group_0578 import WebhookIssueCommentEditedPropIssueAllof0PropMilestoneType
from .group_0580 import (
    WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppType,
)
from .group_0576 import (
    WebhookIssueCommentEditedPropIssueAllof0PropAssigneeType,
    WebhookIssueCommentEditedPropIssueAllof0PropLabelsItemsType,
    WebhookIssueCommentEditedPropIssueAllof0PropPullRequestType,
)


class WebhookIssueCommentEditedPropIssueAllof0Type(TypedDict):
    """Issue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: NotRequired[
        Union[WebhookIssueCommentEditedPropIssueAllof0PropAssigneeType, None]
    ]
    assignees: List[
        Union[WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItemsType, None]
    ]
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
    body: Union[str, None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: NotRequired[
        List[WebhookIssueCommentEditedPropIssueAllof0PropLabelsItemsType]
    ]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssueCommentEditedPropIssueAllof0PropMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[
            WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppType, None
        ]
    ]
    pull_request: NotRequired[
        WebhookIssueCommentEditedPropIssueAllof0PropPullRequestType
    ]
    reactions: WebhookIssueCommentEditedPropIssueAllof0PropReactionsType
    repository_url: str
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookIssueCommentEditedPropIssueAllof0PropUserType, None]


class WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItemsType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookIssueCommentEditedPropIssueAllof0PropReactionsType(TypedDict):
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


class WebhookIssueCommentEditedPropIssueAllof0PropUserType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


__all__ = (
    "WebhookIssueCommentEditedPropIssueAllof0Type",
    "WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItemsType",
    "WebhookIssueCommentEditedPropIssueAllof0PropReactionsType",
    "WebhookIssueCommentEditedPropIssueAllof0PropUserType",
)
