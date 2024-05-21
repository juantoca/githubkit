"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0131 import RepositoryRuleUpdate
from .group_0155 import RepositoryRuleOneof17
from .group_0151 import RepositoryRuleWorkflows
from .group_0136 import RepositoryRulePullRequest
from .group_0153 import RepositoryRuleCodeScanning
from .group_0119 import RepositoryRulesetConditions
from .group_0118 import RepositoryRulesetBypassActor
from .group_0148 import RepositoryRuleTagNamePattern
from .group_0146 import RepositoryRuleBranchNamePattern
from .group_0134 import RepositoryRuleRequiredDeployments
from .group_0138 import RepositoryRuleRequiredStatusChecks
from .group_0140 import RepositoryRuleCommitMessagePattern
from .group_0144 import RepositoryRuleCommitterEmailPattern
from .group_0142 import RepositoryRuleCommitAuthorEmailPattern
from .group_0133 import RepositoryRuleOneof15, RepositoryRuleRequiredLinearHistory
from .group_0130 import (
    RepositoryRuleOneof14,
    RepositoryRuleOneof16,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


class ReposOwnerRepoRulesetsPostBody(GitHubModel):
    """ReposOwnerRepoRulesetsPostBody"""

    name: str = Field(description="The name of the ruleset.")
    target: Missing[Literal["branch", "tag", "push"]] = Field(
        default=UNSET,
        description="The target of the ruleset\n\n**Note**: The `push` target is in beta and is subject to change.",
    )
    enforcement: Literal["disabled", "active", "evaluate"] = Field(
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page."
    )
    bypass_actors: Missing[List[RepositoryRulesetBypassActor]] = Field(
        default=UNSET,
        description="The actors that can bypass the rules in this ruleset",
    )
    conditions: Missing[RepositoryRulesetConditions] = Field(
        default=UNSET,
        title="Repository ruleset conditions for ref names",
        description="Parameters for a repository ruleset ref name condition",
    )
    rules: Missing[
        List[
            Union[
                RepositoryRuleCreation,
                RepositoryRuleUpdate,
                RepositoryRuleDeletion,
                RepositoryRuleRequiredLinearHistory,
                RepositoryRuleRequiredDeployments,
                RepositoryRuleRequiredSignatures,
                RepositoryRulePullRequest,
                RepositoryRuleRequiredStatusChecks,
                RepositoryRuleNonFastForward,
                RepositoryRuleCommitMessagePattern,
                RepositoryRuleCommitAuthorEmailPattern,
                RepositoryRuleCommitterEmailPattern,
                RepositoryRuleBranchNamePattern,
                RepositoryRuleTagNamePattern,
                RepositoryRuleOneof14,
                RepositoryRuleOneof15,
                RepositoryRuleOneof16,
                RepositoryRuleOneof17,
                RepositoryRuleWorkflows,
                RepositoryRuleCodeScanning,
            ]
        ]
    ] = Field(default=UNSET, description="An array of rules within the ruleset.")


model_rebuild(ReposOwnerRepoRulesetsPostBody)

__all__ = ("ReposOwnerRepoRulesetsPostBody",)
