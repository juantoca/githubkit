"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class CodeSecurityConfigurationType(TypedDict):
    """CodeSecurityConfiguration

    A code security configuration
    """

    id: NotRequired[int]
    name: NotRequired[str]
    target_type: NotRequired[Literal["global", "organization"]]
    description: NotRequired[str]
    advanced_security: NotRequired[Literal["enabled", "disabled"]]
    dependency_graph: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_alerts: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_security_updates: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning_push_protection: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_validity_checks: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    private_vulnerability_reporting: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    url: NotRequired[str]
    html_url: NotRequired[str]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


__all__ = ("CodeSecurityConfigurationType",)
