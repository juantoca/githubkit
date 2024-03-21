"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0075 import Team
from .group_0001 import SimpleUser


class PullRequestReviewRequest(GitHubModel):
    """Pull Request Review Request

    Pull Request Review Request
    """

    users: List[SimpleUser] = Field()
    teams: List[Team] = Field()


model_rebuild(PullRequestReviewRequest)

__all__ = ("PullRequestReviewRequest",)
