"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import ExtraGitHubModel, model_rebuild

from .group_0928 import (
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems,
)


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0(ExtraGitHubModel):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0"""

    name: Missing[str] = Field(
        default=UNSET,
        description='The name of the check. For example, "code-coverage".',
    )
    details_url: Missing[str] = Field(
        default=UNSET,
        description="The URL of the integrator's site that has the full details of the check.",
    )
    external_id: Missing[str] = Field(
        default=UNSET, description="A reference for the run on the integrator's system."
    )
    started_at: Missing[datetime] = Field(
        default=UNSET,
        description="This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    status: Missing[Literal["completed"]] = Field(default=UNSET)
    conclusion: Literal[
        "action_required",
        "cancelled",
        "failure",
        "neutral",
        "success",
        "skipped",
        "stale",
        "timed_out",
    ] = Field(
        description="**Required if you provide `completed_at` or a `status` of `completed`**. The final conclusion of the check. \n**Note:** Providing `conclusion` will automatically set the `status` parameter to `completed`. You cannot change a check run conclusion to `stale`, only GitHub can set this."
    )
    completed_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    output: Missing[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput] = Field(
        default=UNSET,
        description="Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run.",
    )
    actions: Missing[
        List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems]
    ] = Field(
        max_length=3,
        default=UNSET,
        description='Possible further actions the integrator can perform, which a user may trigger. Each action includes a `label`, `identifier` and `description`. A maximum of three actions are accepted. To learn more about check runs and requested actions, see "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."',
    )


model_rebuild(ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0)

__all__ = ("ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0",)
