"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict

from .group_0534 import (
    WebhookIssueCommentCreatedPropIssueAllof0PropMilestonePropCreatorType,
)


class WebhookIssueCommentCreatedPropIssueMergedMilestoneType(TypedDict):
    """WebhookIssueCommentCreatedPropIssueMergedMilestone"""

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookIssueCommentCreatedPropIssueAllof0PropMilestonePropCreatorType, None
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


__all__ = ("WebhookIssueCommentCreatedPropIssueMergedMilestoneType",)
