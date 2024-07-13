"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0043 import SimpleRepositoryType


class CodeSecurityConfigurationRepositoriesType(TypedDict):
    """CodeSecurityConfigurationRepositories

    Repositories associated with a code security configuration and attachment status
    """

    status: NotRequired[
        Literal["attached", "attaching", "detached", "enforced", "failed", "updating"]
    ]
    repository: NotRequired[SimpleRepositoryType]


__all__ = ("CodeSecurityConfigurationRepositoriesType",)
