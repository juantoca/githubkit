"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import TypedDict, NotRequired

from .group_0026 import TeamType
from .group_0001 import SimpleUserType
from .group_0027 import OrganizationSimpleType


class CopilotSeatDetailsType(TypedDict):
    """Copilot Business Seat Detail

    Information about a Copilot Business seat assignment for a user, team, or
    organization.
    """

    assignee: Union[SimpleUserType, TeamType, OrganizationType]
    organization: NotRequired[Union[OrganizationSimpleType, None]]
    assigning_team: NotRequired[Union[TeamType, EnterpriseTeamType, None]]
    pending_cancellation_date: NotRequired[Union[date, None]]
    last_activity_at: NotRequired[Union[datetime, None]]
    last_activity_editor: NotRequired[Union[str, None]]
    created_at: datetime
    updated_at: NotRequired[datetime]


class EnterpriseTeamType(TypedDict):
    """Enterprise Team

    Group of enterprise owners and/or members
    """

    id: int
    name: str
    slug: str
    url: str
    sync_to_organizations: str
    group_id: NotRequired[Union[int, None]]
    html_url: str
    members_url: str
    created_at: datetime
    updated_at: datetime


class OrganizationType(TypedDict):
    """Organization

    GitHub account for managing multiple users, teams, and repositories
    """

    login: str
    url: str
    id: int
    node_id: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: Union[str, None]
    blog: NotRequired[str]
    html_url: str
    name: NotRequired[str]
    company: NotRequired[str]
    location: NotRequired[str]
    email: NotRequired[str]
    has_organization_projects: bool
    has_repository_projects: bool
    is_verified: NotRequired[bool]
    public_repos: int
    public_gists: int
    followers: int
    following: int
    type: str
    created_at: datetime
    updated_at: datetime
    plan: NotRequired[OrganizationPropPlanType]


class OrganizationPropPlanType(TypedDict):
    """OrganizationPropPlan"""

    name: NotRequired[str]
    space: NotRequired[int]
    private_repos: NotRequired[int]
    filled_seats: NotRequired[int]
    seats: NotRequired[int]


__all__ = (
    "CopilotSeatDetailsType",
    "EnterpriseTeamType",
    "OrganizationType",
    "OrganizationPropPlanType",
)
