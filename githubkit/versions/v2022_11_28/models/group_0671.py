"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0590 import WebhookRubygemsMetadata


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion(GitHubModel):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion"""

    author: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthor
    ] = Field(default=UNSET)
    body: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1,
        ]
    ] = Field(default=UNSET)
    body_html: Missing[str] = Field(default=UNSET)
    container_metadata: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadata
    ] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    description: str = Field()
    docker_metadata: Missing[
        List[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItems
        ]
    ] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: str = Field()
    id: int = Field()
    installation_command: str = Field()
    manifest: Missing[str] = Field(default=UNSET)
    metadata: List[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItems
    ] = Field()
    name: str = Field()
    npm_metadata: Missing[
        Union[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadata,
            None,
        ]
    ] = Field(default=UNSET)
    nuget_metadata: Missing[
        Union[
            List[
                WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    package_files: List[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItems
    ] = Field()
    package_url: str = Field()
    prerelease: Missing[bool] = Field(default=UNSET)
    release: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropRelease
    ] = Field(default=UNSET)
    rubygems_metadata: Missing[List[WebhookRubygemsMetadata]] = Field(default=UNSET)
    summary: str = Field()
    tag_name: Missing[str] = Field(default=UNSET)
    target_commitish: Missing[str] = Field(default=UNSET)
    target_oid: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    version: str = Field()


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthor(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthor"""

    avatar_url: str = Field()
    events_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    gravatar_id: str = Field()
    html_url: str = Field()
    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organizations_url: str = Field()
    received_events_url: str = Field()
    repos_url: str = Field()
    site_admin: bool = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    type: str = Field()
    url: str = Field()


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneo
    f1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItems(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMe
    tadataItems
    """

    tags: Missing[List[str]] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItems(
    ExtraGitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadata
    Items
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadata(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ata
    """

    name: Missing[str] = Field(default=UNSET)
    version: Missing[str] = Field(default=UNSET)
    npm_user: Missing[str] = Field(default=UNSET)
    author: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1,
            None,
        ]
    ] = Field(default=UNSET)
    bugs: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1,
            None,
        ]
    ] = Field(default=UNSET)
    dependencies: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependencies
    ] = Field(default=UNSET)
    dev_dependencies: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependencies
    ] = Field(default=UNSET)
    peer_dependencies: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependencies
    ] = Field(default=UNSET)
    optional_dependencies: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies
    ] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    dist: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1,
            None,
        ]
    ] = Field(default=UNSET)
    git_head: Missing[str] = Field(default=UNSET)
    homepage: Missing[str] = Field(default=UNSET)
    license_: Missing[str] = Field(default=UNSET, alias="license")
    main: Missing[str] = Field(default=UNSET)
    repository: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1,
            None,
        ]
    ] = Field(default=UNSET)
    scripts: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScripts
    ] = Field(default=UNSET)
    id: Missing[str] = Field(default=UNSET)
    node_version: Missing[str] = Field(default=UNSET)
    npm_version: Missing[str] = Field(default=UNSET)
    has_shrinkwrap: Missing[bool] = Field(default=UNSET)
    maintainers: Missing[List[str]] = Field(default=UNSET)
    contributors: Missing[List[str]] = Field(default=UNSET)
    engines: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEngines
    ] = Field(default=UNSET)
    keywords: Missing[List[str]] = Field(default=UNSET)
    files: Missing[List[str]] = Field(default=UNSET)
    bin_: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBin
    ] = Field(default=UNSET, alias="bin")
    man: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropMan
    ] = Field(default=UNSET)
    directories: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1,
            None,
        ]
    ] = Field(default=UNSET)
    os: Missing[List[str]] = Field(default=UNSET)
    cpu: Missing[List[str]] = Field(default=UNSET)
    readme: Missing[str] = Field(default=UNSET)
    installation_command: Missing[str] = Field(default=UNSET)
    release_id: Missing[int] = Field(default=UNSET)
    commit_oid: Missing[str] = Field(default=UNSET)
    published_via_actions: Missing[bool] = Field(default=UNSET)
    deleted_by_id: Missing[int] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropAuthorOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropBugsOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependencies(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependencies(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDevDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependencies(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropPeerDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropOptionalDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDistOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropRepositoryOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScripts(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropScripts
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEngines(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropEngines
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBin(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropBin
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropMan(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropMan
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDirectoriesOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItems(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageF
    ilesItems
    """

    content_type: str = Field()
    created_at: str = Field()
    download_url: str = Field()
    id: int = Field()
    md5: Union[str, None] = Field()
    name: str = Field()
    sha1: Union[str, None] = Field()
    sha256: Union[str, None] = Field()
    size: int = Field()
    state: Union[str, None] = Field()
    updated_at: str = Field()


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadata(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadata
    """

    labels: Missing[
        Union[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabels,
            None,
        ]
    ] = Field(default=UNSET)
    manifest: Missing[
        Union[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifest,
            None,
        ]
    ] = Field(default=UNSET)
    tag: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTag
    ] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabels(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadataPropLabels
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifest(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadataPropManifest
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTag(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadataPropTag
    """

    digest: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItems(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMet
    adataItems
    """

    id: Missing[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1,
            int,
            None,
        ]
    ] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    value: Missing[
        Union[
            bool,
            str,
            int,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3,
        ]
    ] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMet
    adataItemsPropIdOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMet
    adataItemsPropValueOneof3
    """

    url: Missing[str] = Field(default=UNSET)
    branch: Missing[str] = Field(default=UNSET)
    commit: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropRelease(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropRelease"""

    author: Missing[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthor
    ] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
    prerelease: Missing[bool] = Field(default=UNSET)
    published_at: Missing[str] = Field(default=UNSET)
    tag_name: Missing[str] = Field(default=UNSET)
    target_commitish: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthor(
    GitHubModel
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleaseP
    ropAuthor
    """

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthor
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItems
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItems
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadata
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependencies
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependencies
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependencies
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScripts
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEngines
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBin
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropMan
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItems
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadata
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabels
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifest
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTag
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItems
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropRelease
)
model_rebuild(
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthor
)

__all__ = (
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthor",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItems",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItems",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadata",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependencies",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependencies",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependencies",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScripts",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEngines",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBin",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropMan",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItems",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadata",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabels",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifest",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTag",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItems",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropRelease",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthor",
)
