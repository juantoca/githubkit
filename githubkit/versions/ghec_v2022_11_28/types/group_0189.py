"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class WorkflowUsageType(TypedDict):
    """Workflow Usage

    Workflow Usage
    """

    billable: WorkflowUsagePropBillableType


class WorkflowUsagePropBillableType(TypedDict):
    """WorkflowUsagePropBillable"""

    ubuntu: NotRequired[WorkflowUsagePropBillablePropUbuntuType]
    macos: NotRequired[WorkflowUsagePropBillablePropMacosType]
    windows: NotRequired[WorkflowUsagePropBillablePropWindowsType]


class WorkflowUsagePropBillablePropUbuntuType(TypedDict):
    """WorkflowUsagePropBillablePropUbuntu"""

    total_ms: NotRequired[int]


class WorkflowUsagePropBillablePropMacosType(TypedDict):
    """WorkflowUsagePropBillablePropMacos"""

    total_ms: NotRequired[int]


class WorkflowUsagePropBillablePropWindowsType(TypedDict):
    """WorkflowUsagePropBillablePropWindows"""

    total_ms: NotRequired[int]


__all__ = (
    "WorkflowUsageType",
    "WorkflowUsagePropBillableType",
    "WorkflowUsagePropBillablePropUbuntuType",
    "WorkflowUsagePropBillablePropMacosType",
    "WorkflowUsagePropBillablePropWindowsType",
)
