"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0404 import ProjectsV2ItemType
from .group_0368 import SimpleInstallationType
from .group_0371 import SimpleUserWebhooksType
from .group_0403 import WebhooksProjectChangesType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemArchivedType(TypedDict):
    """Projects v2 Item Archived Event"""

    action: Literal["archived"]
    changes: WebhooksProjectChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectsV2ItemArchivedType",)
