"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0190 import Commit
from .group_0189 import DiffEntry


class CommitComparison(GitHubModel):
    """Commit Comparison

    Commit Comparison
    """

    url: str = Field()
    html_url: str = Field()
    permalink_url: str = Field()
    diff_url: str = Field()
    patch_url: str = Field()
    base_commit: Commit = Field(title="Commit", description="Commit")
    merge_base_commit: Commit = Field(title="Commit", description="Commit")
    status: Literal["diverged", "ahead", "behind", "identical"] = Field()
    ahead_by: int = Field()
    behind_by: int = Field()
    total_commits: int = Field()
    commits: List[Commit] = Field()
    files: Missing[List[DiffEntry]] = Field(default=UNSET)


model_rebuild(CommitComparison)

__all__ = ("CommitComparison",)
