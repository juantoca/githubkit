"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0066 import RunnerType


class OrgsOrgActionsRunnersGenerateJitconfigPostResponse201Type(TypedDict):
    """OrgsOrgActionsRunnersGenerateJitconfigPostResponse201"""

    runner: RunnerType
    encoded_jit_config: str


__all__ = ("OrgsOrgActionsRunnersGenerateJitconfigPostResponse201Type",)
