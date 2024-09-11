"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


from .group_0066 import IssueType
from .group_0017 import RepositoryType
from .group_0414 import SimpleInstallationType
from .group_0416 import RepositoryWebhooksType
from .group_0417 import SimpleUserWebhooksType
from .group_0415 import OrganizationSimpleWebhooksType


class WebhookSubIssuesSubIssueRemovedType(TypedDict):
    """sub-issue removed event"""

    action: Literal["sub_issue_removed"]
    sub_issue_id: float
    sub_issue: IssueType
    sub_issue_repo: RepositoryType
    parent_issue_id: float
    parent_issue: IssueType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookSubIssuesSubIssueRemovedType",)
