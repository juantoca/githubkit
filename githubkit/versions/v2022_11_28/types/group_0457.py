"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0171 import DeploymentType
from .group_0298 import PullRequestType
from .group_0368 import SimpleInstallationType
from .group_0370 import RepositoryWebhooksType
from .group_0371 import SimpleUserWebhooksType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookDeploymentProtectionRuleRequestedType(TypedDict):
    """deployment protection rule requested event"""

    action: Literal["requested"]
    environment: NotRequired[str]
    event: NotRequired[str]
    deployment_callback_url: NotRequired[str]
    deployment: NotRequired[DeploymentType]
    pull_requests: NotRequired[List[PullRequestType]]
    repository: NotRequired[RepositoryWebhooksType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookDeploymentProtectionRuleRequestedType",)
