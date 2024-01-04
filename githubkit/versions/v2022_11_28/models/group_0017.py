"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0016 import LicenseSimple


class Repository(GitHubModel):
    """Repository

    A repository on GitHub.
    """

    id: int = Field(description="Unique identifier of the repository")
    node_id: str = Field()
    name: str = Field(description="The name of the repository.")
    full_name: str = Field()
    license_: Union[None, LicenseSimple] = Field(alias="license")
    organization: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    forks: int = Field()
    permissions: Missing[RepositoryPropPermissions] = Field(default=UNSET)
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    private: bool = Field(
        default=False, description="Whether the repository is private or public."
    )
    html_url: str = Field()
    description: Union[str, None] = Field()
    fork: bool = Field()
    url: str = Field()
    archive_url: str = Field()
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    deployments_url: str = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    forks_url: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    git_url: str = Field()
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    notifications_url: str = Field()
    pulls_url: str = Field()
    releases_url: str = Field()
    ssh_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    clone_url: str = Field()
    mirror_url: Union[str, None] = Field()
    hooks_url: str = Field()
    svn_url: str = Field()
    homepage: Union[str, None] = Field()
    language: Union[str, None] = Field()
    forks_count: int = Field()
    stargazers_count: int = Field()
    watchers_count: int = Field()
    size: int = Field(
        description="The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0."
    )
    default_branch: str = Field(description="The default branch of the repository.")
    open_issues_count: int = Field()
    is_template: Missing[bool] = Field(
        default=UNSET,
        description="Whether this repository acts as a template that can be used to generate new repositories.",
    )
    topics: Missing[List[str]] = Field(default=UNSET)
    has_issues: bool = Field(default=True, description="Whether issues are enabled.")
    has_projects: bool = Field(
        default=True, description="Whether projects are enabled."
    )
    has_wiki: bool = Field(default=True, description="Whether the wiki is enabled.")
    has_pages: bool = Field()
    has_downloads: bool = Field(
        default=True, description="Whether downloads are enabled."
    )
    has_discussions: Missing[bool] = Field(
        default=UNSET, description="Whether discussions are enabled."
    )
    archived: bool = Field(
        default=False, description="Whether the repository is archived."
    )
    disabled: bool = Field(
        description="Returns whether or not this repository disabled."
    )
    visibility: Missing[str] = Field(
        default=UNSET,
        description="The repository visibility: public, private, or internal.",
    )
    pushed_at: Union[datetime, None] = Field()
    created_at: Union[datetime, None] = Field()
    updated_at: Union[datetime, None] = Field()
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow rebase merges for pull requests."
    )
    template_repository: Missing[Union[RepositoryPropTemplateRepository, None]] = Field(
        default=UNSET
    )
    temp_clone_token: Missing[Union[str, None]] = Field(default=UNSET)
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow squash merges for pull requests."
    )
    allow_auto_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to allow Auto-merge to be used on pull requests.",
    )
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to delete head branches when pull requests are merged",
    )
    allow_update_branch: Missing[bool] = Field(
        default=UNSET,
        description="Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.",
    )
    use_squash_pr_title_as_default: Missing[bool] = Field(
        default=UNSET,
        description="Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead.",
    )
    squash_merge_commit_title: Missing[
        Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    squash_merge_commit_message: Missing[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Missing[Literal["PR_TITLE", "MERGE_MESSAGE"]] = Field(
        default=UNSET,
        description="The default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Missing[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = Field(
        default=UNSET,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET, description="Whether to allow merge commits for pull requests."
    )
    allow_forking: Missing[bool] = Field(
        default=UNSET, description="Whether to allow forking this repo"
    )
    web_commit_signoff_required: Missing[bool] = Field(
        default=UNSET,
        description="Whether to require contributors to sign off on web-based commits",
    )
    subscribers_count: Missing[int] = Field(default=UNSET)
    network_count: Missing[int] = Field(default=UNSET)
    open_issues: int = Field()
    watchers: int = Field()
    master_branch: Missing[str] = Field(default=UNSET)
    starred_at: Missing[str] = Field(default=UNSET)
    anonymous_access_enabled: Missing[bool] = Field(
        default=UNSET,
        description="Whether anonymous git access is enabled for this repository",
    )


class RepositoryPropPermissions(GitHubModel):
    """RepositoryPropPermissions"""

    admin: bool = Field()
    pull: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)
    push: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)


class RepositoryPropTemplateRepository(GitHubModel):
    """RepositoryPropTemplateRepository"""

    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    owner: Missing[RepositoryPropTemplateRepositoryPropOwner] = Field(default=UNSET)
    private: Missing[bool] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    git_url: Missing[str] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    ssh_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    clone_url: Missing[str] = Field(default=UNSET)
    mirror_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    svn_url: Missing[str] = Field(default=UNSET)
    homepage: Missing[str] = Field(default=UNSET)
    language: Missing[str] = Field(default=UNSET)
    forks_count: Missing[int] = Field(default=UNSET)
    stargazers_count: Missing[int] = Field(default=UNSET)
    watchers_count: Missing[int] = Field(default=UNSET)
    size: Missing[int] = Field(default=UNSET)
    default_branch: Missing[str] = Field(default=UNSET)
    open_issues_count: Missing[int] = Field(default=UNSET)
    is_template: Missing[bool] = Field(default=UNSET)
    topics: Missing[List[str]] = Field(default=UNSET)
    has_issues: Missing[bool] = Field(default=UNSET)
    has_projects: Missing[bool] = Field(default=UNSET)
    has_wiki: Missing[bool] = Field(default=UNSET)
    has_pages: Missing[bool] = Field(default=UNSET)
    has_downloads: Missing[bool] = Field(default=UNSET)
    archived: Missing[bool] = Field(default=UNSET)
    disabled: Missing[bool] = Field(default=UNSET)
    visibility: Missing[str] = Field(default=UNSET)
    pushed_at: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    permissions: Missing[RepositoryPropTemplateRepositoryPropPermissions] = Field(
        default=UNSET
    )
    allow_rebase_merge: Missing[bool] = Field(default=UNSET)
    temp_clone_token: Missing[Union[str, None]] = Field(default=UNSET)
    allow_squash_merge: Missing[bool] = Field(default=UNSET)
    allow_auto_merge: Missing[bool] = Field(default=UNSET)
    delete_branch_on_merge: Missing[bool] = Field(default=UNSET)
    allow_update_branch: Missing[bool] = Field(default=UNSET)
    use_squash_pr_title_as_default: Missing[bool] = Field(default=UNSET)
    squash_merge_commit_title: Missing[
        Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    squash_merge_commit_message: Missing[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Missing[Literal["PR_TITLE", "MERGE_MESSAGE"]] = Field(
        default=UNSET,
        description="The default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Missing[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = Field(
        default=UNSET,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    allow_merge_commit: Missing[bool] = Field(default=UNSET)
    subscribers_count: Missing[int] = Field(default=UNSET)
    network_count: Missing[int] = Field(default=UNSET)


class RepositoryPropTemplateRepositoryPropOwner(GitHubModel):
    """RepositoryPropTemplateRepositoryPropOwner"""

    login: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    avatar_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)


class RepositoryPropTemplateRepositoryPropPermissions(GitHubModel):
    """RepositoryPropTemplateRepositoryPropPermissions"""

    admin: Missing[bool] = Field(default=UNSET)
    maintain: Missing[bool] = Field(default=UNSET)
    push: Missing[bool] = Field(default=UNSET)
    triage: Missing[bool] = Field(default=UNSET)
    pull: Missing[bool] = Field(default=UNSET)


model_rebuild(Repository)
model_rebuild(RepositoryPropPermissions)
model_rebuild(RepositoryPropTemplateRepository)
model_rebuild(RepositoryPropTemplateRepositoryPropOwner)
model_rebuild(RepositoryPropTemplateRepositoryPropPermissions)

__all__ = (
    "Repository",
    "RepositoryPropPermissions",
    "RepositoryPropTemplateRepository",
    "RepositoryPropTemplateRepositoryPropOwner",
    "RepositoryPropTemplateRepositoryPropPermissions",
)
