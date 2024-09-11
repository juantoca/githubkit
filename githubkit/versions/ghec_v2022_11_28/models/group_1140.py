"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild


class ScimV2OrganizationsOrgUsersScimUserIdPatchBody(GitHubModel):
    """ScimV2OrganizationsOrgUsersScimUserIdPatchBody"""

    schemas: Missing[List[str]] = Field(default=UNSET)
    operations: List[
        ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems
    ] = Field(
        min_length=1 if PYDANTIC_V2 else None,
        alias="Operations",
        description="Set of operations to be performed",
    )


class ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems(GitHubModel):
    """ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems"""

    op: Literal["add", "remove", "replace"] = Field()
    path: Missing[str] = Field(default=UNSET)
    value: Missing[
        Union[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof0,
            List[
                ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof1Items
            ],
            str,
        ]
    ] = Field(default=UNSET)


class ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof0(
    GitHubModel
):
    """ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof0"""

    active: Missing[Union[bool, None]] = Field(default=UNSET)
    user_name: Missing[Union[str, None]] = Field(default=UNSET, alias="userName")
    external_id: Missing[Union[str, None]] = Field(default=UNSET, alias="externalId")
    given_name: Missing[Union[str, None]] = Field(default=UNSET, alias="givenName")
    family_name: Missing[Union[str, None]] = Field(default=UNSET, alias="familyName")


class ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof1Items(
    GitHubModel
):
    """ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof1
    Items
    """

    value: Missing[str] = Field(default=UNSET)
    primary: Missing[bool] = Field(default=UNSET)


model_rebuild(ScimV2OrganizationsOrgUsersScimUserIdPatchBody)
model_rebuild(ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems)
model_rebuild(
    ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof0
)
model_rebuild(
    ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof1Items
)

__all__ = (
    "ScimV2OrganizationsOrgUsersScimUserIdPatchBody",
    "ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems",
    "ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof0",
    "ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsPropValueOneof1Items",
)
