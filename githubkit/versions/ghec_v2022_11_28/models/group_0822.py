"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgActionsPermissionsRepositoriesPutBody(GitHubModel):
    """OrgsOrgActionsPermissionsRepositoriesPutBody"""

    selected_repository_ids: List[int] = Field(
        description="List of repository IDs to enable for GitHub Actions."
    )


model_rebuild(OrgsOrgActionsPermissionsRepositoriesPutBody)

__all__ = ("OrgsOrgActionsPermissionsRepositoriesPutBody",)
