"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0091 import TeamType
from .group_0001 import SimpleUserType
from .group_0159 import RepositoryAdvisoryCreditType


class RepositoryAdvisoryType(TypedDict):
    """RepositoryAdvisory

    A repository security advisory.
    """

    ghsa_id: str
    cve_id: Union[str, None]
    url: str
    html_url: str
    summary: str
    description: Union[str, None]
    severity: Union[None, Literal["critical", "high", "medium", "low"]]
    author: None
    publisher: None
    identifiers: List[RepositoryAdvisoryPropIdentifiersItemsType]
    state: Literal["published", "closed", "withdrawn", "draft", "triage"]
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]
    published_at: Union[datetime, None]
    closed_at: Union[datetime, None]
    withdrawn_at: Union[datetime, None]
    submission: Union[RepositoryAdvisoryPropSubmissionType, None]
    vulnerabilities: Union[List[RepositoryAdvisoryVulnerabilityType], None]
    cvss: Union[RepositoryAdvisoryPropCvssType, None]
    cwes: Union[List[RepositoryAdvisoryPropCwesItemsType], None]
    cwe_ids: Union[List[str], None]
    credits_: Union[List[RepositoryAdvisoryPropCreditsItemsType], None]
    credits_detailed: Union[List[RepositoryAdvisoryCreditType], None]
    collaborating_users: Union[List[SimpleUserType], None]
    collaborating_teams: Union[List[TeamType], None]
    private_fork: None


class RepositoryAdvisoryPropIdentifiersItemsType(TypedDict):
    """RepositoryAdvisoryPropIdentifiersItems"""

    type: Literal["CVE", "GHSA"]
    value: str


class RepositoryAdvisoryPropSubmissionType(TypedDict):
    """RepositoryAdvisoryPropSubmission"""

    accepted: bool


class RepositoryAdvisoryPropCvssType(TypedDict):
    """RepositoryAdvisoryPropCvss"""

    vector_string: Union[str, None]
    score: Union[float, None]


class RepositoryAdvisoryPropCwesItemsType(TypedDict):
    """RepositoryAdvisoryPropCwesItems"""

    cwe_id: str
    name: str


class RepositoryAdvisoryPropCreditsItemsType(TypedDict):
    """RepositoryAdvisoryPropCreditsItems"""

    login: NotRequired[str]
    type: NotRequired[
        Literal[
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
    ]


class RepositoryAdvisoryVulnerabilityType(TypedDict):
    """RepositoryAdvisoryVulnerability

    A product affected by the vulnerability detailed in a repository security
    advisory.
    """

    package: Union[RepositoryAdvisoryVulnerabilityPropPackageType, None]
    vulnerable_version_range: Union[str, None]
    patched_versions: Union[str, None]
    vulnerable_functions: Union[List[str], None]


class RepositoryAdvisoryVulnerabilityPropPackageType(TypedDict):
    """RepositoryAdvisoryVulnerabilityPropPackage

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
    name: Union[str, None]


__all__ = (
    "RepositoryAdvisoryType",
    "RepositoryAdvisoryPropIdentifiersItemsType",
    "RepositoryAdvisoryPropSubmissionType",
    "RepositoryAdvisoryPropCvssType",
    "RepositoryAdvisoryPropCwesItemsType",
    "RepositoryAdvisoryPropCreditsItemsType",
    "RepositoryAdvisoryVulnerabilityType",
    "RepositoryAdvisoryVulnerabilityPropPackageType",
)
