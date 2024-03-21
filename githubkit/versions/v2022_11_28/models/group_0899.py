"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0091 import OrgCustomProperty


class OrgsOrgPropertiesSchemaPatchBody(GitHubModel):
    """OrgsOrgPropertiesSchemaPatchBody"""

    properties: List[OrgCustomProperty] = Field(
        max_length=100,
        min_length=1,
        description="The array of custom properties to create or update.",
    )


model_rebuild(OrgsOrgPropertiesSchemaPatchBody)

__all__ = ("OrgsOrgPropertiesSchemaPatchBody",)
