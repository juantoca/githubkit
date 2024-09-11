"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


from .group_0420 import WebhooksReleaseType
from .group_0376 import EnterpriseWebhooksType
from .group_0377 import SimpleInstallationType
from .group_0379 import RepositoryWebhooksType
from .group_0380 import SimpleUserWebhooksType
from .group_0378 import OrganizationSimpleWebhooksType


class WebhookReleaseEditedType(TypedDict):
    """release edited event"""

    action: Literal["edited"]
    changes: WebhookReleaseEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    release: WebhooksReleaseType
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookReleaseEditedPropChangesType(TypedDict):
    """WebhookReleaseEditedPropChanges"""

    body: NotRequired[WebhookReleaseEditedPropChangesPropBodyType]
    name: NotRequired[WebhookReleaseEditedPropChangesPropNameType]
    make_latest: NotRequired[WebhookReleaseEditedPropChangesPropMakeLatestType]


class WebhookReleaseEditedPropChangesPropBodyType(TypedDict):
    """WebhookReleaseEditedPropChangesPropBody"""

    from_: str


class WebhookReleaseEditedPropChangesPropNameType(TypedDict):
    """WebhookReleaseEditedPropChangesPropName"""

    from_: str


class WebhookReleaseEditedPropChangesPropMakeLatestType(TypedDict):
    """WebhookReleaseEditedPropChangesPropMakeLatest"""

    to: bool


__all__ = (
    "WebhookReleaseEditedType",
    "WebhookReleaseEditedPropChangesType",
    "WebhookReleaseEditedPropChangesPropBodyType",
    "WebhookReleaseEditedPropChangesPropNameType",
    "WebhookReleaseEditedPropChangesPropMakeLatestType",
)
