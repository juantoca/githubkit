"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType


class WebhookReleaseCreatedType(TypedDict):
    """release created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    release: WebhookReleaseCreatedPropReleaseType
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookReleaseCreatedPropReleaseType(TypedDict):
    """Release

    The [release](https://docs.github.com/enterprise-
    cloud@latest//rest/releases/releases/#get-a-release) object.
    """

    assets: List[WebhookReleaseCreatedPropReleasePropAssetsItemsType]
    assets_url: str
    author: Union[WebhookReleaseCreatedPropReleasePropAuthorType, None]
    body: Union[str, None]
    created_at: Union[datetime, None]
    discussion_url: NotRequired[str]
    draft: bool
    html_url: str
    id: int
    name: Union[str, None]
    node_id: str
    prerelease: bool
    published_at: Union[datetime, None]
    reactions: NotRequired[WebhookReleaseCreatedPropReleasePropReactionsType]
    tag_name: str
    tarball_url: Union[str, None]
    target_commitish: str
    upload_url: str
    url: str
    zipball_url: Union[str, None]


class WebhookReleaseCreatedPropReleasePropAuthorType(TypedDict):
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


class WebhookReleaseCreatedPropReleasePropReactionsType(TypedDict):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookReleaseCreatedPropReleasePropAssetsItemsType(TypedDict):
    """Release Asset

    Data related to a release.
    """

    browser_download_url: str
    content_type: str
    created_at: datetime
    download_count: int
    id: int
    label: Union[str, None]
    name: str
    node_id: str
    size: int
    state: Literal["uploaded"]
    updated_at: datetime
    uploader: NotRequired[
        Union[WebhookReleaseCreatedPropReleasePropAssetsItemsPropUploaderType, None]
    ]
    url: str


class WebhookReleaseCreatedPropReleasePropAssetsItemsPropUploaderType(TypedDict):
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


__all__ = (
    "WebhookReleaseCreatedType",
    "WebhookReleaseCreatedPropReleaseType",
    "WebhookReleaseCreatedPropReleasePropAuthorType",
    "WebhookReleaseCreatedPropReleasePropReactionsType",
    "WebhookReleaseCreatedPropReleasePropAssetsItemsType",
    "WebhookReleaseCreatedPropReleasePropAssetsItemsPropUploaderType",
)
