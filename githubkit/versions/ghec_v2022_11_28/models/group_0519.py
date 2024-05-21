"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0404 import SimpleUserWebhooks


class WebhookGithubAppAuthorizationRevoked(GitHubModel):
    """github_app_authorization revoked event"""

    action: Literal["revoked"] = Field()
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


model_rebuild(WebhookGithubAppAuthorizationRevoked)

__all__ = ("WebhookGithubAppAuthorizationRevoked",)
