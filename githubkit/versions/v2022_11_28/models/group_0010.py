"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ValidationError(GitHubModel):
    """Validation Error

    Validation Error
    """

    message: str = Field()
    documentation_url: str = Field()
    errors: Missing[List[ValidationErrorPropErrorsItems]] = Field(default=UNSET)


class ValidationErrorPropErrorsItems(GitHubModel):
    """ValidationErrorPropErrorsItems"""

    resource: Missing[str] = Field(default=UNSET)
    field: Missing[str] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)
    code: str = Field()
    index: Missing[int] = Field(default=UNSET)
    value: Missing[Union[str, None, int, None, List[str], None]] = Field(default=UNSET)


model_rebuild(ValidationError)
model_rebuild(ValidationErrorPropErrorsItems)

__all__ = (
    "ValidationError",
    "ValidationErrorPropErrorsItems",
)
