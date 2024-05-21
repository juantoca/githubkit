"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class CodespaceExportDetailsType(TypedDict):
    """Fetches information about an export of a codespace.

    An export of a codespace. Also, latest export details for a codespace can be
    fetched with id = latest
    """

    state: NotRequired[Union[str, None]]
    completed_at: NotRequired[Union[datetime, None]]
    branch: NotRequired[Union[str, None]]
    sha: NotRequired[Union[str, None]]
    id: NotRequired[str]
    export_url: NotRequired[str]
    html_url: NotRequired[Union[str, None]]


__all__ = ("CodespaceExportDetailsType",)
