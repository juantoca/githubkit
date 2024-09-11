"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


from .group_0213 import DiffEntryType
from .group_0001 import SimpleUserType
from .group_0215 import CommitPropCommitType


class CommitType(TypedDict):
    """Commit

    Commit
    """

    url: str
    sha: str
    node_id: str
    html_url: str
    comments_url: str
    commit: CommitPropCommitType
    author: Union[SimpleUserType, EmptyObjectType, None]
    committer: Union[SimpleUserType, EmptyObjectType, None]
    parents: List[CommitPropParentsItemsType]
    stats: NotRequired[CommitPropStatsType]
    files: NotRequired[List[DiffEntryType]]


class EmptyObjectType(TypedDict):
    """Empty Object

    An object without any properties.
    """


class CommitPropParentsItemsType(TypedDict):
    """CommitPropParentsItems"""

    sha: str
    url: str
    html_url: NotRequired[str]


class CommitPropStatsType(TypedDict):
    """CommitPropStats"""

    additions: NotRequired[int]
    deletions: NotRequired[int]
    total: NotRequired[int]


__all__ = (
    "CommitType",
    "EmptyObjectType",
    "CommitPropParentsItemsType",
    "CommitPropStatsType",
)
