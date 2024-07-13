"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhooksRelease1(GitHubModel):
    """Release

    The [release](https://docs.github.com/enterprise-
    cloud@latest//rest/releases/releases/#get-a-release) object.
    """

    assets: List[Union[WebhooksRelease1PropAssetsItems, None]] = Field()
    assets_url: str = Field()
    author: Union[WebhooksRelease1PropAuthor, None] = Field(title="User")
    body: Union[str, None] = Field()
    created_at: Union[datetime, None] = Field()
    discussion_url: Missing[str] = Field(default=UNSET)
    draft: bool = Field(description="Whether the release is a draft or published")
    html_url: str = Field()
    id: int = Field()
    name: Union[str, None] = Field()
    node_id: str = Field()
    prerelease: bool = Field(
        description="Whether the release is identified as a prerelease or a full release."
    )
    published_at: Union[datetime, None] = Field()
    reactions: Missing[WebhooksRelease1PropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    tag_name: str = Field(description="The name of the tag.")
    tarball_url: Union[str, None] = Field()
    target_commitish: str = Field(
        description="Specifies the commitish value that determines where the Git tag is created from."
    )
    upload_url: str = Field()
    url: str = Field()
    zipball_url: Union[str, None] = Field()


class WebhooksRelease1PropAssetsItems(GitHubModel):
    """Release Asset

    Data related to a release.
    """

    browser_download_url: str = Field()
    content_type: str = Field()
    created_at: datetime = Field()
    download_count: int = Field()
    id: int = Field()
    label: Union[str, None] = Field()
    name: str = Field(description="The file name of the asset.")
    node_id: str = Field()
    size: int = Field()
    state: Literal["uploaded"] = Field(description="State of the release asset.")
    updated_at: datetime = Field()
    uploader: Missing[Union[WebhooksRelease1PropAssetsItemsPropUploader, None]] = Field(
        default=UNSET, title="User"
    )
    url: str = Field()


class WebhooksRelease1PropAssetsItemsPropUploader(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhooksRelease1PropAuthor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhooksRelease1PropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


model_rebuild(WebhooksRelease1)
model_rebuild(WebhooksRelease1PropAssetsItems)
model_rebuild(WebhooksRelease1PropAssetsItemsPropUploader)
model_rebuild(WebhooksRelease1PropAuthor)
model_rebuild(WebhooksRelease1PropReactions)

__all__ = (
    "WebhooksRelease1",
    "WebhooksRelease1PropAssetsItems",
    "WebhooksRelease1PropAssetsItemsPropUploader",
    "WebhooksRelease1PropAuthor",
    "WebhooksRelease1PropReactions",
)
