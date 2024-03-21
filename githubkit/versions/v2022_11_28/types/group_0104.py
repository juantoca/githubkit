"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType(
    TypedDict
):
    """RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty"""

    include: NotRequired[List[RepositoryRulesetConditionsRepositoryPropertySpecType]]
    exclude: NotRequired[List[RepositoryRulesetConditionsRepositoryPropertySpecType]]


class RepositoryRulesetConditionsRepositoryPropertySpecType(TypedDict):
    """Repository ruleset property targeting definition

    Parameters for a targeting a repository property
    """

    name: str
    property_values: List[str]


__all__ = (
    "RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType",
    "RepositoryRulesetConditionsRepositoryPropertySpecType",
)
