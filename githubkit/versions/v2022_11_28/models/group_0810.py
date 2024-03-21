"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0811 import (
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropBase,
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropHead,
)


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItems(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItems"""

    base: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropBase = Field()
    head: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropHead = Field()
    id: float = Field()
    number: float = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItems)

__all__ = ("WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItems",)
