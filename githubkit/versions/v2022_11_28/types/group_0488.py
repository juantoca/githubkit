"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0379 import WebhooksUserType
from .group_0367 import EnterpriseWebhooksType
from .group_0370 import RepositoryWebhooksType
from .group_0371 import SimpleUserWebhooksType
from .group_0384 import WebhooksRepositoriesItemsType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookInstallationCreatedType(TypedDict):
    """installation created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[List[WebhooksRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[Union[WebhooksUserType, None]]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookInstallationCreatedType",)
