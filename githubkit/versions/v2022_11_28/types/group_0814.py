"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0811 import (
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType,
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType,
)


class WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequestsType(TypedDict):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests"""

    base: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType
    head: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType
    id: float
    number: float
    url: str


__all__ = ("WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequestsType",)
