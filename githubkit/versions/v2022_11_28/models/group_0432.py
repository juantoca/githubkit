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

from .group_0367 import EnterpriseWebhooks
from .group_0368 import SimpleInstallation
from .group_0370 import RepositoryWebhooks
from .group_0371 import SimpleUserWebhooks
from .group_0369 import OrganizationSimpleWebhooks


class WebhookCheckSuiteRequested(GitHubModel):
    """check_suite requested event"""

    action: Literal["requested"] = Field()
    check_suite: WebhookCheckSuiteRequestedPropCheckSuite = Field(
        description="The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."
    )
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


class WebhookCheckSuiteRequestedPropCheckSuite(GitHubModel):
    """WebhookCheckSuiteRequestedPropCheckSuite

    The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite).
    """

    after: Union[str, None] = Field()
    app: WebhookCheckSuiteRequestedPropCheckSuitePropApp = Field(
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    before: Union[str, None] = Field()
    check_runs_url: str = Field()
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
        ],
    ] = Field(
        description="The summary conclusion for all check runs that are part of the check suite. This value will be `null` until the check run has completed."
    )
    created_at: datetime = Field()
    head_branch: Union[str, None] = Field(
        description="The head branch name the changes are on."
    )
    head_commit: WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommit = Field(
        title="SimpleCommit"
    )
    head_sha: str = Field(
        description="The SHA of the head commit that is being checked."
    )
    id: int = Field()
    latest_check_runs_count: int = Field()
    node_id: str = Field()
    pull_requests: List[
        WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItems
    ] = Field(
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_sha` and `head_branch`. When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty."
    )
    rerequestable: Missing[bool] = Field(default=UNSET)
    runs_rerequestable: Missing[bool] = Field(default=UNSET)
    status: Union[None, Literal["requested", "in_progress", "completed", "queued"]] = (
        Field(
            description="The summary status for all check runs that are part of the check suite. Can be `requested`, `in_progress`, or `completed`."
        )
    )
    updated_at: datetime = Field()
    url: str = Field(description="URL that points to the check suite API resource.")


class WebhookCheckSuiteRequestedPropCheckSuitePropApp(GitHubModel):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[
        List[
            Literal[
                "branch_protection_rule",
                "check_run",
                "check_suite",
                "code_scanning_alert",
                "commit_comment",
                "content_reference",
                "create",
                "delete",
                "deployment",
                "deployment_review",
                "deployment_status",
                "deploy_key",
                "discussion",
                "discussion_comment",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "member",
                "membership",
                "milestone",
                "organization",
                "org_block",
                "page_build",
                "project",
                "project_card",
                "project_column",
                "public",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "registry_package",
                "release",
                "repository",
                "repository_dispatch",
                "secret_scanning_alert",
                "star",
                "status",
                "team",
                "team_add",
                "watch",
                "workflow_dispatch",
                "workflow_run",
                "pull_request_review_thread",
                "workflow_job",
                "merge_queue_entry",
                "security_and_analysis",
                "secret_scanning_alert_location",
                "projects_v2_item",
                "merge_group",
                "repository_import",
            ]
        ]
    ] = Field(default=UNSET, description="The list of events for the GitHub app")
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwner, None] = (
        Field(title="User")
    )
    permissions: Missing[
        WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwner(GitHubModel):
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


class WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissions(GitHubModel):
    """WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissions

    The set of permissions for the GitHub app
    """

    actions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    administration: Missing[Literal["read", "write"]] = Field(default=UNSET)
    checks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    content_references: Missing[Literal["read", "write"]] = Field(default=UNSET)
    contents: Missing[Literal["read", "write"]] = Field(default=UNSET)
    deployments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    emails: Missing[Literal["read", "write"]] = Field(default=UNSET)
    environments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    issues: Missing[Literal["read", "write"]] = Field(default=UNSET)
    keys: Missing[Literal["read", "write"]] = Field(default=UNSET)
    members: Missing[Literal["read", "write"]] = Field(default=UNSET)
    metadata: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_administration: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_plan: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_projects: Missing[Literal["read", "write", "admin"]] = Field(
        default=UNSET
    )
    organization_secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_self_hosted_runners: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_user_blocking: Missing[Literal["read", "write"]] = Field(default=UNSET)
    packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pull_requests: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_projects: Missing[Literal["read", "write", "admin"]] = Field(
        default=UNSET
    )
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommit(GitHubModel):
    """SimpleCommit"""

    author: WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthor = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    committer: WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitter = (
        Field(
            title="Committer",
            description="Metaproperties for Git author/committer information.",
        )
    )
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthor(GitHubModel):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitter(GitHubModel):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItems(GitHubModel):
    """Check Run Pull Request"""

    base: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBase = (
        Field()
    )
    head: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHead = (
        Field()
    )
    id: int = Field()
    number: int = Field()
    url: str = Field()


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookCheckSuiteRequested)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuite)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropApp)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwner)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissions)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommit)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthor)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitter)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItems)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBase)
model_rebuild(
    WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo
)
model_rebuild(WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHead)
model_rebuild(
    WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookCheckSuiteRequested",
    "WebhookCheckSuiteRequestedPropCheckSuite",
    "WebhookCheckSuiteRequestedPropCheckSuitePropApp",
    "WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwner",
    "WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissions",
    "WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommit",
    "WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthor",
    "WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitter",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItems",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBase",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHead",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo",
)
