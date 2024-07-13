"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0271 import EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems


class EnvironmentPropProtectionRulesItemsAnyof1(GitHubModel):
    """EnvironmentPropProtectionRulesItemsAnyof1"""

    id: int = Field()
    node_id: str = Field()
    prevent_self_review: Missing[bool] = Field(
        default=UNSET,
        description="Whether deployments to this environment can be approved by the user who created the deployment.",
    )
    type: str = Field()
    reviewers: Missing[
        List[EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems]
    ] = Field(
        default=UNSET,
        description="The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.",
    )


model_rebuild(EnvironmentPropProtectionRulesItemsAnyof1)

__all__ = ("EnvironmentPropProtectionRulesItemsAnyof1",)
