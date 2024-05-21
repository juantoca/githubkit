"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import WebhooksIssue2Type
from .group_0367 import EnterpriseWebhooksType
from .group_0368 import SimpleInstallationType
from .group_0370 import RepositoryWebhooksType
from .group_0371 import SimpleUserWebhooksType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookIssuesPinnedType(TypedDict):
    """issues pinned event"""

    action: Literal["pinned"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhooksIssue2Type
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookIssuesPinnedType",)
