"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0405 import WebhooksRuleType
from .group_0400 import EnterpriseWebhooksType
from .group_0401 import SimpleInstallationType
from .group_0403 import RepositoryWebhooksType
from .group_0404 import SimpleUserWebhooksType
from .group_0402 import OrganizationSimpleWebhooksType


class WebhookBranchProtectionRuleCreatedType(TypedDict):
    """branch protection rule created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    rule: WebhooksRuleType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookBranchProtectionRuleCreatedType",)
