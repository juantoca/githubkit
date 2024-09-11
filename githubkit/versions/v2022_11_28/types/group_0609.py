"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


from .group_0376 import EnterpriseWebhooksType
from .group_0377 import SimpleInstallationType
from .group_0379 import RepositoryWebhooksType
from .group_0380 import SimpleUserWebhooksType
from .group_0408 import WebhooksProjectCardType
from .group_0378 import OrganizationSimpleWebhooksType


class WebhookProjectCardConvertedType(TypedDict):
    """project_card converted event"""

    action: Literal["converted"]
    changes: WebhookProjectCardConvertedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhooksProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookProjectCardConvertedPropChangesType(TypedDict):
    """WebhookProjectCardConvertedPropChanges"""

    note: WebhookProjectCardConvertedPropChangesPropNoteType


class WebhookProjectCardConvertedPropChangesPropNoteType(TypedDict):
    """WebhookProjectCardConvertedPropChangesPropNote"""

    from_: str


__all__ = (
    "WebhookProjectCardConvertedType",
    "WebhookProjectCardConvertedPropChangesType",
    "WebhookProjectCardConvertedPropChangesPropNoteType",
)
