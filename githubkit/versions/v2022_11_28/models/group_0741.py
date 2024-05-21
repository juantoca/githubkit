"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0376 import WebhooksWorkflow
from .group_0367 import EnterpriseWebhooks
from .group_0368 import SimpleInstallation
from .group_0370 import RepositoryWebhooks
from .group_0371 import SimpleUserWebhooks
from .group_0369 import OrganizationSimpleWebhooks


class WebhookWorkflowRunInProgress(GitHubModel):
    """workflow_run in_progress event"""

    action: Literal["in_progress"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    workflow: Union[WebhooksWorkflow, None] = Field(title="Workflow")
    workflow_run: WebhookWorkflowRunInProgressPropWorkflowRun = Field(
        title="Workflow Run"
    )


class WebhookWorkflowRunInProgressPropWorkflowRun(GitHubModel):
    """Workflow Run"""

    actor: Union[WebhookWorkflowRunInProgressPropWorkflowRunPropActor, None] = Field(
        title="User"
    )
    artifacts_url: str = Field()
    cancel_url: str = Field()
    check_suite_id: int = Field()
    check_suite_node_id: str = Field()
    check_suite_url: str = Field()
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
    ] = Field()
    created_at: datetime = Field()
    event: str = Field()
    head_branch: Union[str, None] = Field()
    head_commit: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommit = Field(
        title="SimpleCommit"
    )
    head_repository: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepository = (
        Field(title="Repository Lite")
    )
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    jobs_url: str = Field()
    logs_url: str = Field()
    name: Union[str, None] = Field()
    node_id: str = Field()
    path: str = Field()
    previous_attempt_url: Union[str, None] = Field()
    pull_requests: List[
        Union[WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItems, None]
    ] = Field()
    referenced_workflows: Missing[
        Union[
            List[
                WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: WebhookWorkflowRunInProgressPropWorkflowRunPropRepository = Field(
        title="Repository Lite"
    )
    rerun_url: str = Field()
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal["requested", "in_progress", "completed", "queued", "pending"] = (
        Field()
    )
    triggering_actor: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActor, None
    ] = Field(title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropActor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItems(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str = Field()
    ref: Missing[str] = Field(default=UNSET)
    sha: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommit(GitHubModel):
    """SimpleCommit"""

    author: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthor = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    committer: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitter = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthor(GitHubModel):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitter(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepository(GitHubModel):
    """Repository Lite"""

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
    description: Union[str, None] = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    name: Union[str, None] = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    owner: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwner, None
    ] = Field(title="User")
    private: bool = Field(description="Whether the repository is private or public.")
    pulls_url: str = Field()
    releases_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwner(
    GitHubModel
):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunPropRepository(GitHubModel):
    """Repository Lite"""

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
    description: Union[str, None] = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    owner: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwner, None
    ] = Field(title="User")
    private: bool = Field(description="Whether the repository is private or public.")
    pulls_url: str = Field()
    releases_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwner(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItems(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItems"""

    base: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBase = (
        Field()
    )
    head: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHead = (
        Field()
    )
    id: float = Field()
    number: float = Field()
    url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunInProgress)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRun)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropActor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItems)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommit)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitter)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepository)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwner)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropRepository)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwner)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItems)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBase)
model_rebuild(
    WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepo
)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHead)
model_rebuild(
    WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookWorkflowRunInProgress",
    "WebhookWorkflowRunInProgressPropWorkflowRun",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropActor",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItems",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActor",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommit",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthor",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitter",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepository",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwner",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropRepository",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwner",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItems",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBase",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepo",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHead",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo",
)
