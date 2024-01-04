"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import Annotated

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCodespacesAccessSelectedUsersPostBody(GitHubModel):
    """OrgsOrgCodespacesAccessSelectedUsersPostBody"""

    selected_usernames: Annotated[List[str], Field(max_length=100)] = Field(
        description="The usernames of the organization members whose codespaces be billed to the organization."
    )


model_rebuild(OrgsOrgCodespacesAccessSelectedUsersPostBody)

__all__ = ("OrgsOrgCodespacesAccessSelectedUsersPostBody",)
