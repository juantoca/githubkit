"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0006 import Integration


class DeploymentSimple(GitHubModel):
    """Deployment

    A deployment created as the result of an Actions check run from a workflow that
    references an environment
    """

    url: str = Field()
    id: int = Field(description="Unique identifier of the deployment")
    node_id: str = Field()
    task: str = Field(description="Parameter to specify a task to execute")
    original_environment: Missing[str] = Field(default=UNSET)
    environment: str = Field(description="Name for the target deployment environment.")
    description: Union[str, None] = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    statuses_url: str = Field()
    repository_url: str = Field()
    transient_environment: Missing[bool] = Field(
        default=UNSET,
        description="Specifies if the given environment is will no longer exist at some point in the future. Default: false.",
    )
    production_environment: Missing[bool] = Field(
        default=UNSET,
        description="Specifies if the given environment is one that end-users directly interact with. Default: false.",
    )
    performed_via_github_app: Missing[Union[None, Integration, None]] = Field(
        default=UNSET
    )


model_rebuild(DeploymentSimple)

__all__ = ("DeploymentSimple",)
