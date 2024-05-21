"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0416 import WebhooksLabelType
from .group_0400 import EnterpriseWebhooksType
from .group_0401 import SimpleInstallationType
from .group_0403 import RepositoryWebhooksType
from .group_0404 import SimpleUserWebhooksType
from .group_0402 import OrganizationSimpleWebhooksType


class WebhookLabelEditedType(TypedDict):
    """label edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookLabelEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    label: WebhooksLabelType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookLabelEditedPropChangesType(TypedDict):
    """WebhookLabelEditedPropChanges

    The changes to the label if the action was `edited`.
    """

    color: NotRequired[WebhookLabelEditedPropChangesPropColorType]
    description: NotRequired[WebhookLabelEditedPropChangesPropDescriptionType]
    name: NotRequired[WebhookLabelEditedPropChangesPropNameType]


class WebhookLabelEditedPropChangesPropColorType(TypedDict):
    """WebhookLabelEditedPropChangesPropColor"""

    from_: str


class WebhookLabelEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookLabelEditedPropChangesPropDescription"""

    from_: str


class WebhookLabelEditedPropChangesPropNameType(TypedDict):
    """WebhookLabelEditedPropChangesPropName"""

    from_: str


__all__ = (
    "WebhookLabelEditedType",
    "WebhookLabelEditedPropChangesType",
    "WebhookLabelEditedPropChangesPropColorType",
    "WebhookLabelEditedPropChangesPropDescriptionType",
    "WebhookLabelEditedPropChangesPropNameType",
)
