"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict

from .group_0027 import DependabotAlertSecurityVulnerabilityType


class DependabotAlertSecurityAdvisoryType(TypedDict):
    """DependabotAlertSecurityAdvisory

    Details for the GitHub Security Advisory.
    """

    ghsa_id: str
    cve_id: Union[str, None]
    summary: str
    description: str
    vulnerabilities: List[DependabotAlertSecurityVulnerabilityType]
    severity: Literal["low", "medium", "high", "critical"]
    cvss: DependabotAlertSecurityAdvisoryPropCvssType
    cwes: List[DependabotAlertSecurityAdvisoryPropCwesItemsType]
    identifiers: List[DependabotAlertSecurityAdvisoryPropIdentifiersItemsType]
    references: List[DependabotAlertSecurityAdvisoryPropReferencesItemsType]
    published_at: datetime
    updated_at: datetime
    withdrawn_at: Union[datetime, None]


class DependabotAlertSecurityAdvisoryPropCvssType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropCvss

    Details for the advisory pertaining to the Common Vulnerability Scoring System.
    """

    score: float
    vector_string: Union[str, None]


class DependabotAlertSecurityAdvisoryPropCwesItemsType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropCwesItems

    A CWE weakness assigned to the advisory.
    """

    cwe_id: str
    name: str


class DependabotAlertSecurityAdvisoryPropIdentifiersItemsType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropIdentifiersItems

    An advisory identifier.
    """

    type: Literal["CVE", "GHSA"]
    value: str


class DependabotAlertSecurityAdvisoryPropReferencesItemsType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropReferencesItems

    A link to additional advisory information.
    """

    url: str


__all__ = (
    "DependabotAlertSecurityAdvisoryType",
    "DependabotAlertSecurityAdvisoryPropCvssType",
    "DependabotAlertSecurityAdvisoryPropCwesItemsType",
    "DependabotAlertSecurityAdvisoryPropIdentifiersItemsType",
    "DependabotAlertSecurityAdvisoryPropReferencesItemsType",
)
