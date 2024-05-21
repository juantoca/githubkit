"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0135 import RepositoryRuleRequiredDeploymentsPropParametersType


class RepositoryRuleDetailedOneof4Type(TypedDict):
    """RepositoryRuleDetailedOneof4"""

    type: Literal["required_deployments"]
    parameters: NotRequired[RepositoryRuleRequiredDeploymentsPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof4Type",)
