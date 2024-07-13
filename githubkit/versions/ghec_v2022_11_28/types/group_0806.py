"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class EnterprisesEnterpriseActionsRunnerGroupsGetResponse200Type(TypedDict):
    """EnterprisesEnterpriseActionsRunnerGroupsGetResponse200"""

    total_count: float
    runner_groups: List[RunnerGroupsEnterpriseType]


class RunnerGroupsEnterpriseType(TypedDict):
    """RunnerGroupsEnterprise"""

    id: float
    name: str
    visibility: str
    default: bool
    selected_organizations_url: NotRequired[str]
    runners_url: str
    hosted_runners_url: NotRequired[str]
    allows_public_repositories: bool
    workflow_restrictions_read_only: NotRequired[bool]
    restricted_to_workflows: NotRequired[bool]
    selected_workflows: NotRequired[List[str]]


__all__ = (
    "EnterprisesEnterpriseActionsRunnerGroupsGetResponse200Type",
    "RunnerGroupsEnterpriseType",
)
