"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0017 import RepositoryType


class MigrationType(TypedDict):
    """Migration

    A migration.
    """

    id: int
    owner: Union[None, SimpleUserType]
    guid: str
    state: str
    lock_repositories: bool
    exclude_metadata: bool
    exclude_git_data: bool
    exclude_attachments: bool
    exclude_releases: bool
    exclude_owner_projects: bool
    org_metadata_only: bool
    repositories: List[RepositoryType]
    url: str
    created_at: datetime
    updated_at: datetime
    node_id: str
    archive_url: NotRequired[str]
    exclude: NotRequired[List[str]]


__all__ = ("MigrationType",)
