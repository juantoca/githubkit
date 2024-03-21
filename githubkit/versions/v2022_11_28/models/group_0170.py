"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WorkflowUsage(GitHubModel):
    """Workflow Usage

    Workflow Usage
    """

    billable: WorkflowUsagePropBillable = Field()


class WorkflowUsagePropBillable(GitHubModel):
    """WorkflowUsagePropBillable"""

    ubuntu: Missing[WorkflowUsagePropBillablePropUbuntu] = Field(
        default=UNSET, alias="UBUNTU"
    )
    macos: Missing[WorkflowUsagePropBillablePropMacos] = Field(
        default=UNSET, alias="MACOS"
    )
    windows: Missing[WorkflowUsagePropBillablePropWindows] = Field(
        default=UNSET, alias="WINDOWS"
    )


class WorkflowUsagePropBillablePropUbuntu(GitHubModel):
    """WorkflowUsagePropBillablePropUbuntu"""

    total_ms: Missing[int] = Field(default=UNSET)


class WorkflowUsagePropBillablePropMacos(GitHubModel):
    """WorkflowUsagePropBillablePropMacos"""

    total_ms: Missing[int] = Field(default=UNSET)


class WorkflowUsagePropBillablePropWindows(GitHubModel):
    """WorkflowUsagePropBillablePropWindows"""

    total_ms: Missing[int] = Field(default=UNSET)


model_rebuild(WorkflowUsage)
model_rebuild(WorkflowUsagePropBillable)
model_rebuild(WorkflowUsagePropBillablePropUbuntu)
model_rebuild(WorkflowUsagePropBillablePropMacos)
model_rebuild(WorkflowUsagePropBillablePropWindows)

__all__ = (
    "WorkflowUsage",
    "WorkflowUsagePropBillable",
    "WorkflowUsagePropBillablePropUbuntu",
    "WorkflowUsagePropBillablePropMacos",
    "WorkflowUsagePropBillablePropWindows",
)
