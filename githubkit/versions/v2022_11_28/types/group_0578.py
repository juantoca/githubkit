"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0351 import EnterpriseWebhooksType
from .group_0352 import SimpleInstallationType
from .group_0354 import RepositoryWebhooksType
from .group_0355 import SimpleUserWebhooksType
from .group_0353 import OrganizationSimpleWebhooksType


class WebhookMilestoneDeletedType(TypedDict):
    """milestone deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    milestone: WebhookMilestoneDeletedPropMilestoneType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookMilestoneDeletedPropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[WebhookMilestoneDeletedPropMilestonePropCreatorType, None]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookMilestoneDeletedPropMilestonePropCreatorType(TypedDict):
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
    "WebhookMilestoneDeletedType",
    "WebhookMilestoneDeletedPropMilestoneType",
    "WebhookMilestoneDeletedPropMilestonePropCreatorType",
)
