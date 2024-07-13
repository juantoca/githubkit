"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class WebhookRubygemsMetadataType(TypedDict):
    """Ruby Gems metadata"""

    name: NotRequired[str]
    description: NotRequired[str]
    readme: NotRequired[str]
    homepage: NotRequired[str]
    version_info: NotRequired[WebhookRubygemsMetadataPropVersionInfoType]
    platform: NotRequired[str]
    metadata: NotRequired[WebhookRubygemsMetadataPropMetadataType]
    repo: NotRequired[str]
    dependencies: NotRequired[List[WebhookRubygemsMetadataPropDependenciesItemsType]]
    commit_oid: NotRequired[str]


class WebhookRubygemsMetadataPropVersionInfoType(TypedDict):
    """WebhookRubygemsMetadataPropVersionInfo"""

    version: NotRequired[str]


class WebhookRubygemsMetadataPropMetadataType(TypedDict):
    """WebhookRubygemsMetadataPropMetadata"""


class WebhookRubygemsMetadataPropDependenciesItemsType(TypedDict):
    """WebhookRubygemsMetadataPropDependenciesItems"""


__all__ = (
    "WebhookRubygemsMetadataType",
    "WebhookRubygemsMetadataPropVersionInfoType",
    "WebhookRubygemsMetadataPropMetadataType",
    "WebhookRubygemsMetadataPropDependenciesItemsType",
)
