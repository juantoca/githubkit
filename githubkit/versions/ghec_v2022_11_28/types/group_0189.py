"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0091 import TeamType
from .group_0001 import SimpleUserType


class PendingDeploymentPropReviewersItemsType(TypedDict):
    """PendingDeploymentPropReviewersItems"""

    type: NotRequired[Literal["User", "Team"]]
    reviewer: NotRequired[Union[SimpleUserType, TeamType]]


class PendingDeploymentType(TypedDict):
    """Pending Deployment

    Details of a deployment that is waiting for protection rules to pass
    """

    environment: PendingDeploymentPropEnvironmentType
    wait_timer: int
    wait_timer_started_at: Union[datetime, None]
    current_user_can_approve: bool
    reviewers: List[PendingDeploymentPropReviewersItemsType]


class PendingDeploymentPropEnvironmentType(TypedDict):
    """PendingDeploymentPropEnvironment"""

    id: NotRequired[int]
    node_id: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    html_url: NotRequired[str]


__all__ = (
    "PendingDeploymentPropReviewersItemsType",
    "PendingDeploymentType",
    "PendingDeploymentPropEnvironmentType",
)
