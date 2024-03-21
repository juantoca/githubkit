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

from .group_0769 import WebhookSecurityAndAnalysisPropChangesPropFrom


class WebhookSecurityAndAnalysisPropChanges(GitHubModel):
    """WebhookSecurityAndAnalysisPropChanges"""

    from_: Missing[WebhookSecurityAndAnalysisPropChangesPropFrom] = Field(
        default=UNSET, alias="from"
    )


model_rebuild(WebhookSecurityAndAnalysisPropChanges)

__all__ = ("WebhookSecurityAndAnalysisPropChanges",)
