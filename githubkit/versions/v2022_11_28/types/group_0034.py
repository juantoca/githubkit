"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0033 import SimpleRepositoryType
from .group_0032 import DependabotAlertSecurityAdvisoryType
from .group_0031 import DependabotAlertSecurityVulnerabilityType
from .group_0035 import DependabotAlertWithRepositoryPropDependencyType


class DependabotAlertWithRepositoryType(TypedDict):
    """DependabotAlertWithRepository

    A Dependabot alert.
    """

    number: int
    state: Literal["auto_dismissed", "dismissed", "fixed", "open"]
    dependency: DependabotAlertWithRepositoryPropDependencyType
    security_advisory: DependabotAlertSecurityAdvisoryType
    security_vulnerability: DependabotAlertSecurityVulnerabilityType
    url: str
    html_url: str
    created_at: datetime
    updated_at: datetime
    dismissed_at: Union[datetime, None]
    dismissed_by: Union[None, SimpleUserType]
    dismissed_reason: Union[
        None,
        Literal[
            "fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"
        ],
    ]
    dismissed_comment: Union[str, None]
    fixed_at: Union[datetime, None]
    auto_dismissed_at: NotRequired[Union[datetime, None]]
    repository: SimpleRepositoryType


__all__ = ("DependabotAlertWithRepositoryType",)
