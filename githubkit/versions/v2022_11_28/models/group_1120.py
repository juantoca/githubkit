"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class UserEmailVisibilityPatchBody(GitHubModel):
    """UserEmailVisibilityPatchBody"""

    visibility: Literal["public", "private"] = Field(
        description="Denotes whether an email is publicly visible."
    )


model_rebuild(UserEmailVisibilityPatchBody)

__all__ = ("UserEmailVisibilityPatchBody",)
