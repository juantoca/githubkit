"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0075 import TeamSimpleType


class TeamFullType(TypedDict):
    """Full Team

    Groups of organization members that gives permissions on specified repositories.
    """

    id: int
    node_id: str
    url: str
    html_url: str
    name: str
    slug: str
    description: Union[str, None]
    privacy: NotRequired[Literal["closed", "secret"]]
    notification_setting: NotRequired[
        Literal["notifications_enabled", "notifications_disabled"]
    ]
    permission: str
    members_url: str
    repositories_url: str
    parent: NotRequired[Union[None, TeamSimpleType]]
    members_count: int
    repos_count: int
    created_at: datetime
    updated_at: datetime
    organization: TeamOrganizationType
    ldap_dn: NotRequired[str]


class TeamOrganizationType(TypedDict):
    """Team Organization

    Team Organization
    """

    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: Union[str, None]
    name: NotRequired[Union[str, None]]
    company: NotRequired[Union[str, None]]
    blog: NotRequired[Union[str, None]]
    location: NotRequired[Union[str, None]]
    email: NotRequired[Union[str, None]]
    twitter_username: NotRequired[Union[str, None]]
    is_verified: NotRequired[bool]
    has_organization_projects: bool
    has_repository_projects: bool
    public_repos: int
    public_gists: int
    followers: int
    following: int
    html_url: str
    created_at: datetime
    type: str
    total_private_repos: NotRequired[int]
    owned_private_repos: NotRequired[int]
    private_gists: NotRequired[Union[int, None]]
    disk_usage: NotRequired[Union[int, None]]
    collaborators: NotRequired[Union[int, None]]
    billing_email: NotRequired[Union[str, None]]
    plan: NotRequired[TeamOrganizationPropPlanType]
    default_repository_permission: NotRequired[Union[str, None]]
    members_can_create_repositories: NotRequired[Union[bool, None]]
    two_factor_requirement_enabled: NotRequired[Union[bool, None]]
    members_allowed_repository_creation_type: NotRequired[str]
    members_can_create_public_repositories: NotRequired[bool]
    members_can_create_private_repositories: NotRequired[bool]
    members_can_create_internal_repositories: NotRequired[bool]
    members_can_create_pages: NotRequired[bool]
    members_can_create_public_pages: NotRequired[bool]
    members_can_create_private_pages: NotRequired[bool]
    members_can_fork_private_repositories: NotRequired[Union[bool, None]]
    web_commit_signoff_required: NotRequired[bool]
    updated_at: datetime
    archived_at: Union[datetime, None]


class TeamOrganizationPropPlanType(TypedDict):
    """TeamOrganizationPropPlan"""

    name: str
    space: int
    private_repos: int
    filled_seats: NotRequired[int]
    seats: NotRequired[int]


__all__ = (
    "TeamFullType",
    "TeamOrganizationType",
    "TeamOrganizationPropPlanType",
)
