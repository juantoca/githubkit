"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0355 import Meta
from .group_0365 import ScimEnterpriseUserResponseAllof1PropGroupsItems


class ScimEnterpriseUserResponseAllof1(GitHubModel):
    """ScimEnterpriseUserResponseAllof1"""

    id: str = Field(description="The internally generated id for the user object.")
    groups: Missing[List[ScimEnterpriseUserResponseAllof1PropGroupsItems]] = Field(
        default=UNSET,
        description="Provisioned SCIM groups that the user is a member of.",
    )
    meta: Meta = Field(
        description="The metadata associated with the creation/updates to the user."
    )


model_rebuild(ScimEnterpriseUserResponseAllof1)

__all__ = ("ScimEnterpriseUserResponseAllof1",)
