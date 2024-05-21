"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoMilestonesPostBody(GitHubModel):
    """ReposOwnerRepoMilestonesPostBody"""

    title: str = Field(description="The title of the milestone.")
    state: Missing[Literal["open", "closed"]] = Field(
        default=UNSET,
        description="The state of the milestone. Either `open` or `closed`.",
    )
    description: Missing[str] = Field(
        default=UNSET, description="A description of the milestone."
    )
    due_on: Missing[datetime] = Field(
        default=UNSET,
        description="The milestone due date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )


model_rebuild(ReposOwnerRepoMilestonesPostBody)

__all__ = ("ReposOwnerRepoMilestonesPostBody",)
