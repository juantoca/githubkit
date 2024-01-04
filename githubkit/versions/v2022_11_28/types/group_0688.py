"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0689 import (
    WebhookReleasePrereleasedPropReleaseAllof0PropAssetsItemsPropUploaderType,
)


class WebhookReleasePrereleasedPropReleaseAllof0PropAssetsItemsType(TypedDict):
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
        Union[
            WebhookReleasePrereleasedPropReleaseAllof0PropAssetsItemsPropUploaderType,
            None,
        ]
    ]
    url: str


__all__ = ("WebhookReleasePrereleasedPropReleaseAllof0PropAssetsItemsType",)
