"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class RepositoryAdvisoryCredit(GitHubModel):
    """RepositoryAdvisoryCredit

    A credit given to a user for a repository security advisory.
    """

    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    type: Literal[
        "analyst",
        "finder",
        "reporter",
        "coordinator",
        "remediation_developer",
        "remediation_reviewer",
        "remediation_verifier",
        "tool",
        "sponsor",
        "other",
    ] = Field(description="The type of credit the user is receiving.")
    state: Literal["accepted", "declined", "pending"] = Field(
        description="The state of the user's acceptance of the credit."
    )


model_rebuild(RepositoryAdvisoryCredit)

__all__ = ("RepositoryAdvisoryCredit",)
