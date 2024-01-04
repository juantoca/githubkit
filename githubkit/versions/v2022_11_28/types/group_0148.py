"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class ArtifactType(TypedDict):
    """Artifact

    An artifact
    """

    id: int
    node_id: str
    name: str
    size_in_bytes: int
    url: str
    archive_download_url: str
    expired: bool
    created_at: Union[datetime, None]
    expires_at: Union[datetime, None]
    updated_at: Union[datetime, None]
    workflow_run: NotRequired[Union[ArtifactPropWorkflowRunType, None]]


class ArtifactPropWorkflowRunType(TypedDict):
    """ArtifactPropWorkflowRun"""

    id: NotRequired[int]
    repository_id: NotRequired[int]
    head_repository_id: NotRequired[int]
    head_branch: NotRequired[str]
    head_sha: NotRequired[str]


__all__ = (
    "ArtifactType",
    "ArtifactPropWorkflowRunType",
)
