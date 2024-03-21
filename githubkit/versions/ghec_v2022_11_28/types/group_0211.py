"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0076 import MinimalRepositoryType


class CheckSuitePreferenceType(TypedDict):
    """Check Suite Preference

    Check suite configuration preferences for a repository.
    """

    preferences: CheckSuitePreferencePropPreferencesType
    repository: MinimalRepositoryType


class CheckSuitePreferencePropPreferencesType(TypedDict):
    """CheckSuitePreferencePropPreferences"""

    auto_trigger_checks: NotRequired[
        List[CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItemsType]
    ]


class CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItemsType(TypedDict):
    """CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItems"""

    app_id: int
    setting: bool


__all__ = (
    "CheckSuitePreferenceType",
    "CheckSuitePreferencePropPreferencesType",
    "CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItemsType",
)
