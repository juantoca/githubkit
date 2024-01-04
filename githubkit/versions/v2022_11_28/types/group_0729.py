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


class WebhookRepositoryTransferredType(TypedDict):
    """repository transferred event"""

    action: Literal["transferred"]
    changes: WebhookRepositoryTransferredPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookRepositoryTransferredPropChangesType(TypedDict):
    """WebhookRepositoryTransferredPropChanges"""

    owner: WebhookRepositoryTransferredPropChangesPropOwnerType


class WebhookRepositoryTransferredPropChangesPropOwnerType(TypedDict):
    """WebhookRepositoryTransferredPropChangesPropOwner"""

    from_: WebhookRepositoryTransferredPropChangesPropOwnerPropFromType


class WebhookRepositoryTransferredPropChangesPropOwnerPropFromType(TypedDict):
    """WebhookRepositoryTransferredPropChangesPropOwnerPropFrom"""

    organization: NotRequired[
        WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropOrganizationType
    ]
    user: NotRequired[
        Union[
            WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropUserType, None
        ]
    ]


class WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropOrganizationType(
    TypedDict
):
    """Organization"""

    avatar_url: str
    description: Union[str, None]
    events_url: str
    hooks_url: str
    html_url: NotRequired[str]
    id: int
    issues_url: str
    login: str
    members_url: str
    node_id: str
    public_members_url: str
    repos_url: str
    url: str


class WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropUserType(TypedDict):
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
    "WebhookRepositoryTransferredType",
    "WebhookRepositoryTransferredPropChangesType",
    "WebhookRepositoryTransferredPropChangesPropOwnerType",
    "WebhookRepositoryTransferredPropChangesPropOwnerPropFromType",
    "WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropOrganizationType",
    "WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropUserType",
)
