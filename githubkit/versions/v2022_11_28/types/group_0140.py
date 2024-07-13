"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0115 import RepositoryRuleUpdateType
from .group_0139 import RepositoryRuleOneof17Type
from .group_0135 import RepositoryRuleWorkflowsType
from .group_0120 import RepositoryRulePullRequestType
from .group_0111 import OrgRulesetConditionsOneof0Type
from .group_0112 import OrgRulesetConditionsOneof1Type
from .group_0113 import OrgRulesetConditionsOneof2Type
from .group_0137 import RepositoryRuleCodeScanningType
from .group_0103 import RepositoryRulesetConditionsType
from .group_0102 import RepositoryRulesetBypassActorType
from .group_0132 import RepositoryRuleTagNamePatternType
from .group_0130 import RepositoryRuleBranchNamePatternType
from .group_0118 import RepositoryRuleRequiredDeploymentsType
from .group_0122 import RepositoryRuleRequiredStatusChecksType
from .group_0124 import RepositoryRuleCommitMessagePatternType
from .group_0128 import RepositoryRuleCommitterEmailPatternType
from .group_0126 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0117 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0114 import (
    RepositoryRuleOneof14Type,
    RepositoryRuleOneof16Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class RepositoryRulesetType(TypedDict):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int
    name: str
    target: NotRequired[Literal["branch", "tag", "push"]]
    source_type: NotRequired[Literal["Repository", "Organization"]]
    source: str
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    current_user_can_bypass: NotRequired[
        Literal["always", "pull_requests_only", "never"]
    ]
    node_id: NotRequired[str]
    links: NotRequired[RepositoryRulesetPropLinksType]
    conditions: NotRequired[
        Union[
            RepositoryRulesetConditionsType,
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
            None,
        ]
    ]
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
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class RepositoryRulesetPropLinksType(TypedDict):
    """RepositoryRulesetPropLinks"""

    self_: NotRequired[RepositoryRulesetPropLinksPropSelfType]
    html: NotRequired[RepositoryRulesetPropLinksPropHtmlType]


class RepositoryRulesetPropLinksPropSelfType(TypedDict):
    """RepositoryRulesetPropLinksPropSelf"""

    href: NotRequired[str]


class RepositoryRulesetPropLinksPropHtmlType(TypedDict):
    """RepositoryRulesetPropLinksPropHtml"""

    href: NotRequired[str]


__all__ = (
    "RepositoryRulesetType",
    "RepositoryRulesetPropLinksType",
    "RepositoryRulesetPropLinksPropSelfType",
    "RepositoryRulesetPropLinksPropHtmlType",
)
