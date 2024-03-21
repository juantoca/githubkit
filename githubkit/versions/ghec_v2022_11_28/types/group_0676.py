"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class WebhookPullRequestClosedPropPullRequestAllof1Type(TypedDict):
    """WebhookPullRequestClosedPropPullRequestAllof1"""

    allow_auto_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    use_squash_pr_title_as_default: NotRequired[bool]


__all__ = ("WebhookPullRequestClosedPropPullRequestAllof1Type",)
