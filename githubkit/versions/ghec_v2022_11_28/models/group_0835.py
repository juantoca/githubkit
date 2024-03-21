"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0836 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase,
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead,
)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems"""

    base: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase = Field()
    head: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead = Field()
    id: float = Field()
    number: float = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems)

__all__ = ("WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems",)
