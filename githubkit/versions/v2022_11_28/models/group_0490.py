"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0015 import Installation
from .group_0367 import EnterpriseWebhooks
from .group_0370 import RepositoryWebhooks
from .group_0371 import SimpleUserWebhooks
from .group_0384 import WebhooksRepositoriesItems
from .group_0369 import OrganizationSimpleWebhooks


class WebhookInstallationNewPermissionsAccepted(GitHubModel):
    """installation new_permissions_accepted event"""

    action: Literal["new_permissions_accepted"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Installation = Field(title="Installation", description="Installation")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repositories: Missing[List[WebhooksRepositoriesItems]] = Field(
        default=UNSET,
        description="An array of repository objects that the installation can access.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    requester: Missing[None] = Field(default=UNSET)
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


model_rebuild(WebhookInstallationNewPermissionsAccepted)

__all__ = ("WebhookInstallationNewPermissionsAccepted",)
