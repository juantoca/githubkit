"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0153 import RateLimit


class RateLimitOverviewPropResources(GitHubModel):
    """RateLimitOverviewPropResources"""

    core: RateLimit = Field(title="Rate Limit")
    graphql: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")
    search: RateLimit = Field(title="Rate Limit")
    code_search: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")
    source_import: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")
    integration_manifest: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")
    code_scanning_upload: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")
    actions_runner_registration: Missing[RateLimit] = Field(
        default=UNSET, title="Rate Limit"
    )
    scim: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")
    dependency_snapshots: Missing[RateLimit] = Field(default=UNSET, title="Rate Limit")


model_rebuild(RateLimitOverviewPropResources)

__all__ = ("RateLimitOverviewPropResources",)
