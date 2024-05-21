"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0131 import RepositoryRuleUpdateType
from .group_0155 import RepositoryRuleOneof17Type
from .group_0151 import RepositoryRuleWorkflowsType
from .group_0136 import RepositoryRulePullRequestType
from .group_0153 import RepositoryRuleCodeScanningType
from .group_0119 import RepositoryRulesetConditionsType
from .group_0118 import RepositoryRulesetBypassActorType
from .group_0148 import RepositoryRuleTagNamePatternType
from .group_0146 import RepositoryRuleBranchNamePatternType
from .group_0134 import RepositoryRuleRequiredDeploymentsType
from .group_0138 import RepositoryRuleRequiredStatusChecksType
from .group_0140 import RepositoryRuleCommitMessagePatternType
from .group_0144 import RepositoryRuleCommitterEmailPatternType
from .group_0142 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0133 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0130 import (
    RepositoryRuleOneof14Type,
    RepositoryRuleOneof16Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class ReposOwnerRepoRulesetsPostBodyType(TypedDict):
    """ReposOwnerRepoRulesetsPostBody"""

    name: str
    target: NotRequired[Literal["branch", "tag", "push"]]
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[RepositoryRulesetConditionsType]
    rules: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleOneof14Type,
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]


__all__ = ("ReposOwnerRepoRulesetsPostBodyType",)
