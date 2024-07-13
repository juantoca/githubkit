"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0381 import WebhooksWorkflowType
from .group_0372 import EnterpriseWebhooksType
from .group_0373 import SimpleInstallationType
from .group_0375 import RepositoryWebhooksType
from .group_0376 import SimpleUserWebhooksType
from .group_0374 import OrganizationSimpleWebhooksType


class WebhookWorkflowRunCompletedType(TypedDict):
    """workflow_run completed event"""

    action: Literal["completed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    workflow: Union[WebhooksWorkflowType, None]
    workflow_run: WebhookWorkflowRunCompletedPropWorkflowRunType


class WebhookWorkflowRunCompletedPropWorkflowRunType(TypedDict):
    """Workflow Run"""

    actor: Union[WebhookWorkflowRunCompletedPropWorkflowRunPropActorType, None]
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: Union[
        None,
        Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "skipped",
            "stale",
            "success",
            "timed_out",
        ],
    ]
    created_at: datetime
    event: str
    head_branch: Union[str, None]
    head_commit: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitType
    head_repository: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryType
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: Union[str, None]
    node_id: str
    path: str
    previous_attempt_url: Union[str, None]
    pull_requests: List[
        Union[WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsType, None]
    ]
    referenced_workflows: NotRequired[
        Union[
            List[
                WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryType
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "pending", "waiting"
    ]
    triggering_actor: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: str
    display_title: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropActorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitType(TypedDict):
    """SimpleCommit"""

    author: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthorType
    committer: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitterType
    id: str
    message: str
    timestamp: str
    tree_id: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthorType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitterType(
    TypedDict
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """Repository Lite"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwnerType, None
    ]
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwnerType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryType(TypedDict):
    """Repository Lite"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwnerType, None
    ]
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwnerType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItems"""

    base: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBaseType
    head: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadType
    id: float
    number: float
    url: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookWorkflowRunCompletedType",
    "WebhookWorkflowRunCompletedPropWorkflowRunType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropActorType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActorType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthorType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitterType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
)
