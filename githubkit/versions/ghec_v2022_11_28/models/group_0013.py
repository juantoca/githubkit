"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0012 import Enterprise


class IntegrationInstallationRequest(GitHubModel):
    """Integration Installation Request

    Request to install an integration on a target
    """

    id: int = Field(description="Unique identifier of the request installation.")
    node_id: Missing[str] = Field(default=UNSET)
    account: Union[SimpleUser, Enterprise] = Field()
    requester: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    created_at: datetime = Field()


model_rebuild(IntegrationInstallationRequest)

__all__ = ("IntegrationInstallationRequest",)
