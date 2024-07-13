"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0031 import DependabotAlertSecurityVulnerability


class DependabotAlertSecurityAdvisory(GitHubModel):
    """DependabotAlertSecurityAdvisory

    Details for the GitHub Security Advisory.
    """

    ghsa_id: str = Field(
        description="The unique GitHub Security Advisory ID assigned to the advisory."
    )
    cve_id: Union[str, None] = Field(
        description="The unique CVE ID assigned to the advisory."
    )
    summary: str = Field(
        max_length=1024, description="A short, plain text summary of the advisory."
    )
    description: str = Field(
        description="A long-form Markdown-supported description of the advisory."
    )
    vulnerabilities: List[DependabotAlertSecurityVulnerability] = Field(
        description="Vulnerable version range information for the advisory."
    )
    severity: Literal["low", "medium", "high", "critical"] = Field(
        description="The severity of the advisory."
    )
    cvss: DependabotAlertSecurityAdvisoryPropCvss = Field(
        description="Details for the advisory pertaining to the Common Vulnerability Scoring System."
    )
    cwes: List[DependabotAlertSecurityAdvisoryPropCwesItems] = Field(
        description="Details for the advisory pertaining to Common Weakness Enumeration."
    )
    identifiers: List[DependabotAlertSecurityAdvisoryPropIdentifiersItems] = Field(
        description="Values that identify this advisory among security information sources."
    )
    references: List[DependabotAlertSecurityAdvisoryPropReferencesItems] = Field(
        description="Links to additional advisory information."
    )
    published_at: datetime = Field(
        description="The time that the advisory was published in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    updated_at: datetime = Field(
        description="The time that the advisory was last modified in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    withdrawn_at: Union[datetime, None] = Field(
        description="The time that the advisory was withdrawn in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )


class DependabotAlertSecurityAdvisoryPropCvss(GitHubModel):
    """DependabotAlertSecurityAdvisoryPropCvss

    Details for the advisory pertaining to the Common Vulnerability Scoring System.
    """

    score: float = Field(le=10.0, description="The overall CVSS score of the advisory.")
    vector_string: Union[str, None] = Field(
        description="The full CVSS vector string for the advisory."
    )


class DependabotAlertSecurityAdvisoryPropCwesItems(GitHubModel):
    """DependabotAlertSecurityAdvisoryPropCwesItems

    A CWE weakness assigned to the advisory.
    """

    cwe_id: str = Field(description="The unique CWE ID.")
    name: str = Field(description="The short, plain text name of the CWE.")


class DependabotAlertSecurityAdvisoryPropIdentifiersItems(GitHubModel):
    """DependabotAlertSecurityAdvisoryPropIdentifiersItems

    An advisory identifier.
    """

    type: Literal["CVE", "GHSA"] = Field(description="The type of advisory identifier.")
    value: str = Field(description="The value of the advisory identifer.")


class DependabotAlertSecurityAdvisoryPropReferencesItems(GitHubModel):
    """DependabotAlertSecurityAdvisoryPropReferencesItems

    A link to additional advisory information.
    """

    url: str = Field(description="The URL of the reference.")


model_rebuild(DependabotAlertSecurityAdvisory)
model_rebuild(DependabotAlertSecurityAdvisoryPropCvss)
model_rebuild(DependabotAlertSecurityAdvisoryPropCwesItems)
model_rebuild(DependabotAlertSecurityAdvisoryPropIdentifiersItems)
model_rebuild(DependabotAlertSecurityAdvisoryPropReferencesItems)

__all__ = (
    "DependabotAlertSecurityAdvisory",
    "DependabotAlertSecurityAdvisoryPropCvss",
    "DependabotAlertSecurityAdvisoryPropCwesItems",
    "DependabotAlertSecurityAdvisoryPropIdentifiersItems",
    "DependabotAlertSecurityAdvisoryPropReferencesItems",
)
