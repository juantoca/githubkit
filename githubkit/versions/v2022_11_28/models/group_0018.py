"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0017 import Repository
from .group_0014 import AppPermissions


class InstallationToken(GitHubModel):
    """Installation Token

    Authentication token for a GitHub App installed on a user or org.
    """

    token: str = Field()
    expires_at: str = Field()
    permissions: Missing[AppPermissions] = Field(
        default=UNSET,
        title="App Permissions",
        description="The permissions granted to the user access token.",
    )
    repository_selection: Missing[Literal["all", "selected"]] = Field(default=UNSET)
    repositories: Missing[List[Repository]] = Field(default=UNSET)
    single_file: Missing[str] = Field(default=UNSET)
    has_multiple_single_files: Missing[bool] = Field(default=UNSET)
    single_file_paths: Missing[List[str]] = Field(default=UNSET)


model_rebuild(InstallationToken)

__all__ = ("InstallationToken",)
