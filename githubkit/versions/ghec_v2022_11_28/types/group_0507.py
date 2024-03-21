"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0509 import WebhookIssueCommentEditedPropIssueType
from .group_0508 import WebhookIssueCommentEditedPropCommentType


class WebhookIssueCommentEditedType(TypedDict):
    """issue_comment edited event"""

    action: Literal["edited"]
    changes: WebhookIssueCommentEditedPropChangesType
    comment: WebhookIssueCommentEditedPropCommentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssueCommentEditedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookIssueCommentEditedPropChangesType(TypedDict):
    """WebhookIssueCommentEditedPropChanges

    The changes to the comment.
    """

    body: NotRequired[WebhookIssueCommentEditedPropChangesPropBodyType]


class WebhookIssueCommentEditedPropChangesPropBodyType(TypedDict):
    """WebhookIssueCommentEditedPropChangesPropBody"""

    from_: str


__all__ = (
    "WebhookIssueCommentEditedType",
    "WebhookIssueCommentEditedPropChangesType",
    "WebhookIssueCommentEditedPropChangesPropBodyType",
)
