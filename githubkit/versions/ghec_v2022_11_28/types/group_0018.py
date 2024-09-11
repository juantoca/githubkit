"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


from .group_0017 import RepositoryType
from .group_0014 import AppPermissionsType


class InstallationTokenType(TypedDict):
    """Installation Token

    Authentication token for a GitHub App installed on a user or org.
    """

    token: str
    expires_at: str
    permissions: NotRequired[AppPermissionsType]
    repository_selection: NotRequired[Literal["all", "selected"]]
    repositories: NotRequired[List[RepositoryType]]
    single_file: NotRequired[str]
    has_multiple_single_files: NotRequired[bool]
    single_file_paths: NotRequired[List[str]]


__all__ = ("InstallationTokenType",)
