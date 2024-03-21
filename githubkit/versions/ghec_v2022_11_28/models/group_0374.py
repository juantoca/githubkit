"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0016 import LicenseSimple
from .group_0368 import SearchResultTextMatchesItems


class RepoSearchResultItem(GitHubModel):
    """Repo Search Result Item

    Repo Search Result Item
    """

    id: int = Field()
    node_id: str = Field()
    name: str = Field()
    full_name: str = Field()
    owner: Union[None, SimpleUser] = Field()
    private: bool = Field()
    html_url: str = Field()
    description: Union[str, None] = Field()
    fork: bool = Field()
    url: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    pushed_at: datetime = Field()
    homepage: Union[str, None] = Field()
    size: int = Field()
    stargazers_count: int = Field()
    watchers_count: int = Field()
    language: Union[str, None] = Field()
    forks_count: int = Field()
    open_issues_count: int = Field()
    master_branch: Missing[str] = Field(default=UNSET)
    default_branch: str = Field()
    score: float = Field()
    forks_url: str = Field()
    keys_url: str = Field()
    collaborators_url: str = Field()
    teams_url: str = Field()
    hooks_url: str = Field()
    issue_events_url: str = Field()
    events_url: str = Field()
    assignees_url: str = Field()
    branches_url: str = Field()
    tags_url: str = Field()
    blobs_url: str = Field()
    git_tags_url: str = Field()
    git_refs_url: str = Field()
    trees_url: str = Field()
    statuses_url: str = Field()
    languages_url: str = Field()
    stargazers_url: str = Field()
    contributors_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    commits_url: str = Field()
    git_commits_url: str = Field()
    comments_url: str = Field()
    issue_comment_url: str = Field()
    contents_url: str = Field()
    compare_url: str = Field()
    merges_url: str = Field()
    archive_url: str = Field()
    downloads_url: str = Field()
    issues_url: str = Field()
    pulls_url: str = Field()
    milestones_url: str = Field()
    notifications_url: str = Field()
    labels_url: str = Field()
    releases_url: str = Field()
    deployments_url: str = Field()
    git_url: str = Field()
    ssh_url: str = Field()
    clone_url: str = Field()
    svn_url: str = Field()
    forks: int = Field()
    open_issues: int = Field()
    watchers: int = Field()
    topics: Missing[List[str]] = Field(default=UNSET)
    mirror_url: Union[str, None] = Field()
    has_issues: bool = Field()
    has_projects: bool = Field()
    has_pages: bool = Field()
    has_wiki: bool = Field()
    has_downloads: bool = Field()
    has_discussions: Missing[bool] = Field(default=UNSET)
    archived: bool = Field()
    disabled: bool = Field(
        description="Returns whether or not this repository disabled."
    )
    visibility: Missing[str] = Field(
        default=UNSET,
        description="The repository visibility: public, private, or internal.",
    )
    license_: Union[None, LicenseSimple] = Field(alias="license")
    permissions: Missing[RepoSearchResultItemPropPermissions] = Field(default=UNSET)
    text_matches: Missing[List[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )
    temp_clone_token: Missing[Union[str, None]] = Field(default=UNSET)
    allow_merge_commit: Missing[bool] = Field(default=UNSET)
    allow_squash_merge: Missing[bool] = Field(default=UNSET)
    allow_rebase_merge: Missing[bool] = Field(default=UNSET)
    allow_auto_merge: Missing[bool] = Field(default=UNSET)
    delete_branch_on_merge: Missing[bool] = Field(default=UNSET)
    allow_forking: Missing[bool] = Field(default=UNSET)
    is_template: Missing[bool] = Field(default=UNSET)
    web_commit_signoff_required: Missing[bool] = Field(default=UNSET)


class RepoSearchResultItemPropPermissions(GitHubModel):
    """RepoSearchResultItemPropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()


class SearchRepositoriesGetResponse200(GitHubModel):
    """SearchRepositoriesGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: List[RepoSearchResultItem] = Field()


model_rebuild(RepoSearchResultItem)
model_rebuild(RepoSearchResultItemPropPermissions)
model_rebuild(SearchRepositoriesGetResponse200)

__all__ = (
    "RepoSearchResultItem",
    "RepoSearchResultItemPropPermissions",
    "SearchRepositoriesGetResponse200",
)
