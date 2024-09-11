"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


from .group_0600 import WebhookPackageUpdatedPropPackagePropPackageVersionType


class WebhookPackageUpdatedPropPackageType(TypedDict):
    """WebhookPackageUpdatedPropPackage

    Information about the package.
    """

    created_at: str
    description: Union[str, None]
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: Union[WebhookPackageUpdatedPropPackagePropOwnerType, None]
    package_type: str
    package_version: WebhookPackageUpdatedPropPackagePropPackageVersionType
    registry: Union[WebhookPackageUpdatedPropPackagePropRegistryType, None]
    updated_at: str


class WebhookPackageUpdatedPropPackagePropOwnerType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPackageUpdatedPropPackagePropRegistryType(TypedDict):
    """WebhookPackageUpdatedPropPackagePropRegistry"""

    about_url: str
    name: str
    type: str
    url: str
    vendor: str


__all__ = (
    "WebhookPackageUpdatedPropPackageType",
    "WebhookPackageUpdatedPropPackagePropOwnerType",
    "WebhookPackageUpdatedPropPackagePropRegistryType",
)
