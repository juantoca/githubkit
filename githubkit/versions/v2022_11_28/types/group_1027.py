"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict


class ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBodyType(TypedDict):
    """ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBody"""

    content: Literal[
        "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
    ]


__all__ = ("ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBodyType",)
