"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class TeamMembership(GitHubModel):
    """Team Membership

    Team Membership
    """

    url: str = Field()
    role: Literal["member", "maintainer"] = Field(
        default="member", description="The role of the user in the team."
    )
    state: Literal["active", "pending"] = Field(
        description="The state of the user's membership in the team."
    )


model_rebuild(TeamMembership)

__all__ = ("TeamMembership",)
