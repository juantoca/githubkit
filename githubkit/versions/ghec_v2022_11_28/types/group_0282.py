"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class ReviewDismissedIssueEventType(TypedDict):
    """Review Dismissed Issue Event

    Review Dismissed Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: Literal["review_dismissed"]
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: Union[None, IntegrationType]
    dismissed_review: ReviewDismissedIssueEventPropDismissedReviewType


class ReviewDismissedIssueEventPropDismissedReviewType(TypedDict):
    """ReviewDismissedIssueEventPropDismissedReview"""

    state: str
    review_id: int
    dismissal_message: Union[str, None]
    dismissal_commit_id: NotRequired[str]


__all__ = (
    "ReviewDismissedIssueEventType",
    "ReviewDismissedIssueEventPropDismissedReviewType",
)
