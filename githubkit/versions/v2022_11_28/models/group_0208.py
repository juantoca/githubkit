"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0033 import SimpleRepository
from .group_0210 import CodeScanningVariantAnalysisPropSkippedRepositories
from .group_0209 import CodeScanningVariantAnalysisPropScannedRepositoriesItems


class CodeScanningVariantAnalysis(GitHubModel):
    """Variant Analysis

    A run of a CodeQL query against one or more repositories.
    """

    id: int = Field(description="The ID of the variant analysis.")
    controller_repo: SimpleRepository = Field(
        title="Simple Repository", description="A GitHub repository."
    )
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    query_language: Literal[
        "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "swift"
    ] = Field(description="The language targeted by the CodeQL query")
    query_pack_url: str = Field(description="The download url for the query pack.")
    created_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time at which the variant analysis was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ.",
    )
    updated_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time at which the variant analysis was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ.",
    )
    completed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The date and time at which the variant analysis was completed, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. Will be null if the variant analysis has not yet completed or this information is not available.",
    )
    status: Literal["in_progress", "succeeded", "failed", "cancelled"] = Field()
    actions_workflow_run_id: Missing[int] = Field(
        default=UNSET,
        description="The GitHub Actions workflow run used to execute this variant analysis. This is only available if the workflow run has started.",
    )
    failure_reason: Missing[
        Literal["no_repos_queried", "actions_workflow_run_failed", "internal_error"]
    ] = Field(
        default=UNSET,
        description="The reason for a failure of the variant analysis. This is only available if the variant analysis has failed.",
    )
    scanned_repositories: Missing[
        List[CodeScanningVariantAnalysisPropScannedRepositoriesItems]
    ] = Field(default=UNSET)
    skipped_repositories: Missing[
        CodeScanningVariantAnalysisPropSkippedRepositories
    ] = Field(
        default=UNSET,
        description="Information about repositories that were skipped from processing. This information is only available to the user that initiated the variant analysis.",
    )


model_rebuild(CodeScanningVariantAnalysis)

__all__ = ("CodeScanningVariantAnalysis",)
