"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0201 import CodeScanningVariantAnalysisRepository


class CodeScanningVariantAnalysisSkippedRepoGroup(GitHubModel):
    """CodeScanningVariantAnalysisSkippedRepoGroup"""

    repository_count: int = Field(
        description="The total number of repositories that were skipped for this reason."
    )
    repositories: List[CodeScanningVariantAnalysisRepository] = Field(
        description="A list of repositories that were skipped. This list may not include all repositories that were skipped. This is only available when the repository was found and the user has access to it."
    )


model_rebuild(CodeScanningVariantAnalysisSkippedRepoGroup)

__all__ = ("CodeScanningVariantAnalysisSkippedRepoGroup",)
