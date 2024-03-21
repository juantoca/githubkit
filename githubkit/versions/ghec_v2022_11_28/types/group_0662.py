"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0401 import ProjectsV2ItemType
from .group_0391 import SimpleInstallationType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemArchivedType(TypedDict):
    """Projects v2 Item Archived Event"""

    action: Literal["archived"]
    changes: WebhookProjectsV2ItemArchivedPropChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


class WebhookProjectsV2ItemArchivedPropChangesType(TypedDict):
    """WebhookProjectsV2ItemArchivedPropChanges"""

    archived_at: NotRequired[WebhookProjectsV2ItemArchivedPropChangesPropArchivedAtType]


class WebhookProjectsV2ItemArchivedPropChangesPropArchivedAtType(TypedDict):
    """WebhookProjectsV2ItemArchivedPropChangesPropArchivedAt"""

    from_: NotRequired[Union[datetime, None]]
    to: NotRequired[Union[datetime, None]]


__all__ = (
    "WebhookProjectsV2ItemArchivedType",
    "WebhookProjectsV2ItemArchivedPropChangesType",
    "WebhookProjectsV2ItemArchivedPropChangesPropArchivedAtType",
)
