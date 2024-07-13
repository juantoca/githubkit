"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0406 import EnterpriseWebhooksType
from .group_0407 import SimpleInstallationType
from .group_0409 import RepositoryWebhooksType
from .group_0410 import SimpleUserWebhooksType
from .group_0457 import WebhooksSponsorshipType
from .group_0408 import OrganizationSimpleWebhooksType


class WebhookSponsorshipPendingCancellationType(TypedDict):
    """sponsorship pending_cancellation event"""

    action: Literal["pending_cancellation"]
    effective_date: NotRequired[str]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType
    sponsorship: WebhooksSponsorshipType


__all__ = ("WebhookSponsorshipPendingCancellationType",)
