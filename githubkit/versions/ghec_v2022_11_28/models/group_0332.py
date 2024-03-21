"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0142 import RepositoryRuleCommitAuthorEmailPatternPropParameters


class RepositoryRuleDetailedOneof10(GitHubModel):
    """RepositoryRuleDetailedOneof10"""

    type: Literal["commit_author_email_pattern"] = Field()
    parameters: Missing[RepositoryRuleCommitAuthorEmailPatternPropParameters] = Field(
        default=UNSET
    )
    ruleset_source_type: Missing[Literal["Repository", "Organization"]] = Field(
        default=UNSET,
        description="The type of source for the ruleset that includes this rule.",
    )
    ruleset_source: Missing[str] = Field(
        default=UNSET,
        description="The name of the source of the ruleset that includes this rule.",
    )
    ruleset_id: Missing[int] = Field(
        default=UNSET, description="The ID of the ruleset that includes this rule."
    )


model_rebuild(RepositoryRuleDetailedOneof10)

__all__ = ("RepositoryRuleDetailedOneof10",)
