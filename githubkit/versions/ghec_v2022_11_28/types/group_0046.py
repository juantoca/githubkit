"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class GetConsumedLicensesType(TypedDict):
    """Enterprise Consumed Licenses

    A breakdown of the licenses consumed by an enterprise.
    """

    total_seats_consumed: NotRequired[int]
    total_seats_purchased: NotRequired[int]
    users: NotRequired[List[GetConsumedLicensesPropUsersItemsType]]


class GetConsumedLicensesPropUsersItemsType(TypedDict):
    """GetConsumedLicensesPropUsersItems"""

    github_com_login: NotRequired[str]
    github_com_name: NotRequired[Union[str, None]]
    enterprise_server_user_ids: NotRequired[List[str]]
    github_com_user: NotRequired[bool]
    enterprise_server_user: NotRequired[Union[bool, None]]
    visual_studio_subscription_user: NotRequired[bool]
    license_type: NotRequired[str]
    github_com_profile: NotRequired[Union[str, None]]
    github_com_member_roles: NotRequired[List[str]]
    github_com_enterprise_roles: NotRequired[List[str]]
    github_com_verified_domain_emails: NotRequired[List[str]]
    github_com_saml_name_id: NotRequired[Union[str, None]]
    github_com_orgs_with_pending_invites: NotRequired[List[str]]
    github_com_two_factor_auth: NotRequired[Union[bool, None]]
    enterprise_server_emails: NotRequired[List[str]]
    visual_studio_license_status: NotRequired[Union[str, None]]
    visual_studio_subscription_email: NotRequired[Union[str, None]]
    total_user_accounts: NotRequired[int]


__all__ = (
    "GetConsumedLicensesType",
    "GetConsumedLicensesPropUsersItemsType",
)
