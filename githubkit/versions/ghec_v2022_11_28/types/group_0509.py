"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0414 import DiscussionType
from .group_0403 import RepositoryWebhooksType


class WebhookDiscussionTransferredPropChangesType(TypedDict):
    """WebhookDiscussionTransferredPropChanges"""

    new_discussion: DiscussionType
    new_repository: RepositoryWebhooksType


__all__ = ("WebhookDiscussionTransferredPropChangesType",)
