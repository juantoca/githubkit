"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0076 import MinimalRepositoryType


class OrgsOrgActionsVariablesNameRepositoriesGetResponse200Type(TypedDict):
    """OrgsOrgActionsVariablesNameRepositoriesGetResponse200"""

    total_count: int
    repositories: List[MinimalRepositoryType]


__all__ = ("OrgsOrgActionsVariablesNameRepositoriesGetResponse200Type",)
