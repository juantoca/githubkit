"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRulesetBypassActor(GitHubModel):
    """Repository Ruleset Bypass Actor

    An actor that can bypass rules in a ruleset
    """

    actor_id: int = Field(
        description="The ID of the actor that can bypass a ruleset. If `actor_type` is `OrganizationAdmin`, this should be `1`."
    )
    actor_type: Literal[
        "RepositoryRole", "Team", "Integration", "OrganizationAdmin"
    ] = Field(description="The type of actor that can bypass a ruleset")
    bypass_mode: Literal["always", "pull_request"] = Field(
        description="When the specified actor can bypass the ruleset. `pull_request` means that an actor can only bypass rules on pull requests."
    )


model_rebuild(RepositoryRulesetBypassActor)

__all__ = ("RepositoryRulesetBypassActor",)
