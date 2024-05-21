"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0395 import MergeGroupType
from .group_0368 import SimpleInstallationType
from .group_0370 import RepositoryWebhooksType
from .group_0371 import SimpleUserWebhooksType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookMergeGroupChecksRequestedType(TypedDict):
    """WebhookMergeGroupChecksRequested"""

    action: Literal["checks_requested"]
    installation: NotRequired[SimpleInstallationType]
    merge_group: MergeGroupType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookMergeGroupChecksRequestedType",)
