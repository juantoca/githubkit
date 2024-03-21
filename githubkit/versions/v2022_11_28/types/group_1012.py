"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0234 import DeploymentBranchPolicySettingsType


class ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyType(TypedDict):
    """ReposOwnerRepoEnvironmentsEnvironmentNamePutBody"""

    wait_timer: NotRequired[int]
    prevent_self_review: NotRequired[bool]
    reviewers: NotRequired[
        Union[
            List[
                ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItemsType
            ],
            None,
        ]
    ]
    deployment_branch_policy: NotRequired[
        Union[DeploymentBranchPolicySettingsType, None]
    ]


class ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItemsType(TypedDict):
    """ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems"""

    type: NotRequired[Literal["User", "Team"]]
    id: NotRequired[int]


__all__ = (
    "ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyType",
    "ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItemsType",
)
