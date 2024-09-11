"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


from .group_0427 import WebhooksUserType
from .group_0442 import WebhooksTeamType
from .group_0413 import EnterpriseWebhooksType
from .group_0414 import SimpleInstallationType
from .group_0416 import RepositoryWebhooksType
from .group_0415 import OrganizationSimpleWebhooksType


class WebhookMembershipAddedType(TypedDict):
    """membership added event"""

    action: Literal["added"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    member: Union[WebhooksUserType, None]
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    scope: Literal["team"]
    sender: Union[WebhookMembershipAddedPropSenderType, None]
    team: WebhooksTeamType


class WebhookMembershipAddedPropSenderType(TypedDict):
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
    "WebhookMembershipAddedType",
    "WebhookMembershipAddedPropSenderType",
)
