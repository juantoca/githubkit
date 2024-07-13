"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0365 import Traffic


class ViewTraffic(GitHubModel):
    """View Traffic

    View Traffic
    """

    count: int = Field()
    uniques: int = Field()
    views: List[Traffic] = Field()


model_rebuild(ViewTraffic)

__all__ = ("ViewTraffic",)
