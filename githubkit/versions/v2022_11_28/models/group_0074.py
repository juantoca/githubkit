"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class TeamSimple(GitHubModel):
    """Team Simple

    Groups of organization members that gives permissions on specified repositories.
    """

    id: int = Field(description="Unique identifier of the team")
    node_id: str = Field()
    url: str = Field(description="URL for the team")
    members_url: str = Field()
    name: str = Field(description="Name of the team")
    description: Union[str, None] = Field(description="Description of the team")
    permission: str = Field(
        description="Permission that the team will have for its repositories"
    )
    privacy: Missing[str] = Field(
        default=UNSET, description="The level of privacy this team should have"
    )
    notification_setting: Missing[str] = Field(
        default=UNSET, description="The notification setting the team has set"
    )
    html_url: str = Field()
    repositories_url: str = Field()
    slug: str = Field()
    ldap_dn: Missing[str] = Field(
        default=UNSET,
        description="Distinguished Name (DN) that team maps to within LDAP environment",
    )


model_rebuild(TeamSimple)

__all__ = ("TeamSimple",)
