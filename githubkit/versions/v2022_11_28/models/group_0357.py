"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0005 import Integration
from .group_0183 import DeploymentSimple
from .group_0356 import SimpleCheckSuite
from .group_0156 import PullRequestMinimal


class CheckRunWithSimpleCheckSuite(GitHubModel):
    """CheckRun

    A check performed on the code of a given code change
    """

    app: Union[None, Integration] = Field()
    check_suite: SimpleCheckSuite = Field(
        description="A suite of checks performed on the code of a given code change"
    )
    completed_at: Union[datetime, None] = Field()
    conclusion: Union[
        None,
        Literal[
            "waiting",
            "pending",
            "startup_failure",
            "stale",
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
        ],
    ] = Field()
    deployment: Missing[DeploymentSimple] = Field(
        default=UNSET,
        title="Deployment",
        description="A deployment created as the result of an Actions check run from a workflow that references an environment",
    )
    details_url: str = Field()
    external_id: str = Field()
    head_sha: str = Field(description="The SHA of the commit that is being checked.")
    html_url: str = Field()
    id: int = Field(description="The id of the check.")
    name: str = Field(description="The name of the check.")
    node_id: str = Field()
    output: CheckRunWithSimpleCheckSuitePropOutput = Field()
    pull_requests: List[PullRequestMinimal] = Field()
    started_at: datetime = Field()
    status: Literal["queued", "in_progress", "completed", "pending"] = Field(
        description="The phase of the lifecycle that the check is currently in."
    )
    url: str = Field()


class CheckRunWithSimpleCheckSuitePropOutput(GitHubModel):
    """CheckRunWithSimpleCheckSuitePropOutput"""

    annotations_count: int = Field()
    annotations_url: str = Field()
    summary: Union[str, None] = Field()
    text: Union[str, None] = Field()
    title: Union[str, None] = Field()


model_rebuild(CheckRunWithSimpleCheckSuite)
model_rebuild(CheckRunWithSimpleCheckSuitePropOutput)

__all__ = (
    "CheckRunWithSimpleCheckSuite",
    "CheckRunWithSimpleCheckSuitePropOutput",
)
