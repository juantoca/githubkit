"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


from .group_0078 import CodespaceType


class OrgsOrgCodespacesGetResponse200Type(TypedDict):
    """OrgsOrgCodespacesGetResponse200"""

    total_count: int
    codespaces: List[CodespaceType]


__all__ = ("OrgsOrgCodespacesGetResponse200Type",)
