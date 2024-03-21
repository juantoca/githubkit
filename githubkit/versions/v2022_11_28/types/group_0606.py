"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0607 import WebhookPingPropHookType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookPingType(TypedDict):
    """WebhookPing"""

    hook: NotRequired[WebhookPingPropHookType]
    hook_id: NotRequired[int]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]
    zen: NotRequired[str]


__all__ = ("WebhookPingType",)
