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

from .group_0090 import CodeSecurityConfiguration


class CodeSecurityDefaultConfigurationsItems(GitHubModel):
    """CodeSecurityDefaultConfigurationsItems"""

    default_for_new_repos: Missing[Literal["public", "private_and_internal", "all"]] = (
        Field(
            default=UNSET,
            description="The visibility of newly created repositories for which the code security configuration will be applied to by default",
        )
    )
    configuration: Missing[CodeSecurityConfiguration] = Field(
        default=UNSET, description="A code security configuration"
    )


model_rebuild(CodeSecurityDefaultConfigurationsItems)

__all__ = ("CodeSecurityDefaultConfigurationsItems",)
