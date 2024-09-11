"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


from .group_0413 import EnterpriseWebhooksType
from .group_0414 import SimpleInstallationType
from .group_0416 import RepositoryWebhooksType
from .group_0417 import SimpleUserWebhooksType
from .group_0447 import WebhooksProjectCardType
from .group_0415 import OrganizationSimpleWebhooksType


class WebhookProjectCardEditedType(TypedDict):
    """project_card edited event"""

    action: Literal["edited"]
    changes: WebhookProjectCardEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhooksProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookProjectCardEditedPropChangesType(TypedDict):
    """WebhookProjectCardEditedPropChanges"""

    note: WebhookProjectCardEditedPropChangesPropNoteType


class WebhookProjectCardEditedPropChangesPropNoteType(TypedDict):
    """WebhookProjectCardEditedPropChangesPropNote"""

    from_: Union[str, None]


__all__ = (
    "WebhookProjectCardEditedType",
    "WebhookProjectCardEditedPropChangesType",
    "WebhookProjectCardEditedPropChangesPropNoteType",
)
