"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class RepositoryAdvisoryUpdateType(TypedDict):
    """RepositoryAdvisoryUpdate"""

    summary: NotRequired[str]
    description: NotRequired[str]
    cve_id: NotRequired[Union[str, None]]
    vulnerabilities: NotRequired[
        List[RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType]
    ]
    cwe_ids: NotRequired[Union[List[str], None]]
    credits_: NotRequired[
        Union[List[RepositoryAdvisoryUpdatePropCreditsItemsType], None]
    ]
    severity: NotRequired[Union[None, Literal["critical", "high", "medium", "low"]]]
    cvss_vector_string: NotRequired[Union[str, None]]
    state: NotRequired[Literal["published", "closed", "draft"]]
    collaborating_users: NotRequired[Union[List[str], None]]
    collaborating_teams: NotRequired[Union[List[str], None]]


class RepositoryAdvisoryUpdatePropCreditsItemsType(TypedDict):
    """RepositoryAdvisoryUpdatePropCreditsItems"""

    login: str
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
    ]


class RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType(TypedDict):
    """RepositoryAdvisoryUpdatePropVulnerabilitiesItems"""

    package: RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackageType
    vulnerable_version_range: NotRequired[Union[str, None]]
    patched_versions: NotRequired[Union[str, None]]
    vulnerable_functions: NotRequired[Union[List[str], None]]


class RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackageType(TypedDict):
    """RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackage

    The name of the package affected by the vulnerability.
    """

    ecosystem: Literal[
        "rubygems",
        "npm",
        "pip",
        "maven",
        "nuget",
        "composer",
        "go",
        "rust",
        "erlang",
        "actions",
        "pub",
        "other",
        "swift",
    ]
    name: NotRequired[Union[str, None]]


__all__ = (
    "RepositoryAdvisoryUpdateType",
    "RepositoryAdvisoryUpdatePropCreditsItemsType",
    "RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType",
    "RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackageType",
)
