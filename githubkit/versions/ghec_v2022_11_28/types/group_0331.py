"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0140 import RepositoryRuleCommitMessagePatternPropParametersType


class RepositoryRuleDetailedOneof9Type(TypedDict):
    """RepositoryRuleDetailedOneof9"""

    type: Literal["commit_message_pattern"]
    parameters: NotRequired[RepositoryRuleCommitMessagePatternPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof9Type",)
