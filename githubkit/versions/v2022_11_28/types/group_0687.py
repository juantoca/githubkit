"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0594 import WebhookRubygemsMetadataType


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionType(TypedDict):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion"""

    author: (
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthorType
    )
    body: str
    body_html: str
    created_at: str
    description: str
    docker_metadata: NotRequired[
        List[
            Union[
                WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItemsType,
                None,
            ]
        ]
    ]
    draft: NotRequired[bool]
    html_url: str
    id: int
    installation_command: str
    manifest: NotRequired[str]
    metadata: List[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItemsType
    ]
    name: str
    package_files: List[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItemsType
    ]
    package_url: str
    prerelease: NotRequired[bool]
    release: NotRequired[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleaseType
    ]
    rubygems_metadata: NotRequired[List[WebhookRubygemsMetadataType]]
    summary: str
    tag_name: NotRequired[str]
    target_commitish: str
    target_oid: str
    updated_at: str
    version: str


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthorType(
    TypedDict
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthor"""

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItemsType(
    TypedDict
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMeta
    dataItems
    """

    tags: NotRequired[List[str]]


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItemsType(
    TypedDict
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataIt
    ems
    """


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItemsType(
    TypedDict
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFil
    esItems
    """

    content_type: NotRequired[str]
    created_at: NotRequired[str]
    download_url: NotRequired[str]
    id: NotRequired[int]
    md5: NotRequired[Union[str, None]]
    name: NotRequired[str]
    sha1: NotRequired[Union[str, None]]
    sha256: NotRequired[str]
    size: NotRequired[int]
    state: NotRequired[str]
    updated_at: NotRequired[str]


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleaseType(
    TypedDict
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropRelease"""

    author: WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthorType
    created_at: str
    draft: bool
    html_url: str
    id: int
    name: str
    prerelease: bool
    published_at: str
    tag_name: str
    target_commitish: str
    url: str


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthorType(
    TypedDict
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePro
    pAuthor
    """

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str


__all__ = (
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthorType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItemsType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItemsType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItemsType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleaseType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthorType",
)
