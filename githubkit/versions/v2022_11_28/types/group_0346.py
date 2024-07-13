"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0345 import TrafficType


class CloneTrafficType(TypedDict):
    """Clone Traffic

    Clone Traffic
    """

    count: int
    uniques: int
    clones: List[TrafficType]


__all__ = ("CloneTrafficType",)
