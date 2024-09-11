"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


from .group_0376 import EnterpriseWebhooksType
from .group_0377 import SimpleInstallationType
from .group_0379 import RepositoryWebhooksType
from .group_0380 import SimpleUserWebhooksType
from .group_0378 import OrganizationSimpleWebhooksType


class WebhookSecurityAdvisoryWithdrawnType(TypedDict):
    """security_advisory withdrawn event"""

    action: Literal["withdrawn"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    security_advisory: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryType
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryType(TypedDict):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory

    The details of the security advisory, including summary, description, and
    severity.
    """

    cvss: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvssType
    cwes: List[WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItemsType]
    description: str
    ghsa_id: str
    identifiers: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItemsType
    ]
    published_at: str
    references: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItemsType
    ]
    severity: str
    summary: str
    updated_at: str
    vulnerabilities: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsType
    ]
    withdrawn_at: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvssType(TypedDict):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss"""

    score: float
    vector_string: Union[str, None]


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItemsType(TypedDict):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems"""

    cwe_id: str
    name: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems"""

    type: str
    value: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems"""

    url: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems"""

    first_patched_version: Union[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType,
        None,
    ]
    package: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType
    severity: str
    vulnerable_version_range: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    FirstPatchedVersion
    """

    identifier: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    Package
    """

    ecosystem: str
    name: str


__all__ = (
    "WebhookSecurityAdvisoryWithdrawnType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvssType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType",
)
