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
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0395 import WebhooksIssue2
from .group_0372 import EnterpriseWebhooks
from .group_0373 import SimpleInstallation
from .group_0375 import RepositoryWebhooks
from .group_0376 import SimpleUserWebhooks
from .group_0374 import OrganizationSimpleWebhooks


class WebhookIssuesTransferred(GitHubModel):
    """issues transferred event"""

    action: Literal["transferred"] = Field()
    changes: WebhookIssuesTransferredPropChanges = Field()
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
    issue: WebhooksIssue2 = Field(
        title="Issue",
        description="The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.",
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


class WebhookIssuesTransferredPropChanges(GitHubModel):
    """WebhookIssuesTransferredPropChanges"""

    new_issue: WebhookIssuesTransferredPropChangesPropNewIssue = Field(
        title="Issue",
        description="The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.",
    )
    new_repository: WebhookIssuesTransferredPropChangesPropNewRepository = Field(
        title="Repository", description="A git repository"
    )


class WebhookIssuesTransferredPropChangesPropNewIssue(GitHubModel):
    """Issue

    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ] = Field()
    assignee: Missing[
        Union[WebhookIssuesTransferredPropChangesPropNewIssuePropAssignee, None]
    ] = Field(default=UNSET, title="User")
    assignees: List[
        Union[WebhookIssuesTransferredPropChangesPropNewIssuePropAssigneesItems, None]
    ] = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: Union[str, None] = Field(description="Contents of the issue")
    closed_at: Union[datetime, None] = Field()
    comments: int = Field()
    comments_url: str = Field()
    created_at: datetime = Field()
    draft: Missing[bool] = Field(default=UNSET)
    events_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: Missing[
        List[WebhookIssuesTransferredPropChangesPropNewIssuePropLabelsItems]
    ] = Field(default=UNSET)
    labels_url: str = Field()
    locked: Missing[bool] = Field(default=UNSET)
    milestone: Union[
        WebhookIssuesTransferredPropChangesPropNewIssuePropMilestone, None
    ] = Field(
        title="Milestone",
        description="A collection of related issues and pull requests.",
    )
    node_id: str = Field()
    number: int = Field()
    performed_via_github_app: Missing[
        Union[
            WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubApp,
            None,
        ]
    ] = Field(
        default=UNSET,
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    pull_request: Missing[
        WebhookIssuesTransferredPropChangesPropNewIssuePropPullRequest
    ] = Field(default=UNSET)
    reactions: WebhookIssuesTransferredPropChangesPropNewIssuePropReactions = Field(
        title="Reactions"
    )
    repository_url: str = Field()
    state: Missing[Literal["open", "closed"]] = Field(
        default=UNSET, description="State of the issue; either 'open' or 'closed'"
    )
    state_reason: Missing[Union[str, None]] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field(description="Title of the issue")
    updated_at: datetime = Field()
    url: str = Field(description="URL for the issue")
    user: Union[WebhookIssuesTransferredPropChangesPropNewIssuePropUser, None] = Field(
        title="User"
    )


class WebhookIssuesTransferredPropChangesPropNewIssuePropAssignee(GitHubModel):
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


class WebhookIssuesTransferredPropChangesPropNewIssuePropAssigneesItems(GitHubModel):
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


class WebhookIssuesTransferredPropChangesPropNewIssuePropLabelsItems(GitHubModel):
    """Label"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookIssuesTransferredPropChangesPropNewIssuePropMilestone(GitHubModel):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None] = Field()
    closed_issues: int = Field()
    created_at: datetime = Field()
    creator: Union[
        WebhookIssuesTransferredPropChangesPropNewIssuePropMilestonePropCreator, None
    ] = Field(title="User")
    description: Union[str, None] = Field()
    due_on: Union[datetime, None] = Field()
    html_url: str = Field()
    id: int = Field()
    labels_url: str = Field()
    node_id: str = Field()
    number: int = Field(description="The number of the milestone.")
    open_issues: int = Field()
    state: Literal["open", "closed"] = Field(description="The state of the milestone.")
    title: str = Field(description="The title of the milestone.")
    updated_at: datetime = Field()
    url: str = Field()


class WebhookIssuesTransferredPropChangesPropNewIssuePropMilestonePropCreator(
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


class WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubApp(
    GitHubModel
):
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
            ]
        ]
    ] = Field(default=UNSET, description="The list of events for the GitHub app")
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropOwner,
        None,
    ] = Field(title="User")
    permissions: Missing[
        WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropOwner(
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


class WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropPermissions(
    GitHubModel
):
    """WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropPerm
    issions

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
    organization_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_self_hosted_runners: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_user_blocking: Missing[Literal["read", "write"]] = Field(default=UNSET)
    packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pull_requests: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookIssuesTransferredPropChangesPropNewIssuePropPullRequest(GitHubModel):
    """WebhookIssuesTransferredPropChangesPropNewIssuePropPullRequest"""

    diff_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    merged_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    patch_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesTransferredPropChangesPropNewIssuePropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookIssuesTransferredPropChangesPropNewIssuePropUser(GitHubModel):
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


class WebhookIssuesTransferredPropChangesPropNewRepository(GitHubModel):
    """Repository

    A git repository
    """

    allow_auto_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow auto-merge for pull requests."
    )
    allow_forking: Missing[bool] = Field(
        default=UNSET, description="Whether to allow private forks"
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET, description="Whether to allow merge commits for pull requests."
    )
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow rebase merges for pull requests."
    )
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow squash merges for pull requests."
    )
    allow_update_branch: Missing[bool] = Field(default=UNSET)
    archive_url: str = Field()
    archived: bool = Field(
        default=False, description="Whether the repository is archived."
    )
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    clone_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    created_at: Union[int, datetime] = Field()
    custom_properties: Missing[
        WebhookIssuesTransferredPropChangesPropNewRepositoryPropCustomProperties
    ] = Field(
        default=UNSET,
        description="The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )
    default_branch: str = Field(description="The default branch of the repository.")
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to delete head branches when pull requests are merged",
    )
    deployments_url: str = Field()
    description: Union[str, None] = Field()
    disabled: Missing[bool] = Field(
        default=UNSET, description="Returns whether or not this repository is disabled."
    )
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks: int = Field()
    forks_count: int = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    git_url: str = Field()
    has_downloads: bool = Field(
        default=True, description="Whether downloads are enabled."
    )
    has_issues: bool = Field(default=True, description="Whether issues are enabled.")
    has_pages: bool = Field()
    has_projects: bool = Field(
        default=True, description="Whether projects are enabled."
    )
    has_wiki: bool = Field(default=True, description="Whether the wiki is enabled.")
    has_discussions: bool = Field(
        default=False, description="Whether discussions are enabled."
    )
    homepage: Union[str, None] = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    is_template: Missing[bool] = Field(default=UNSET)
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    language: Union[str, None] = Field()
    languages_url: str = Field()
    license_: Union[
        WebhookIssuesTransferredPropChangesPropNewRepositoryPropLicense, None
    ] = Field(alias="license", title="License")
    master_branch: Missing[str] = Field(default=UNSET)
    merges_url: str = Field()
    milestones_url: str = Field()
    mirror_url: Union[str, None] = Field()
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    open_issues: int = Field()
    open_issues_count: int = Field()
    organization: Missing[str] = Field(default=UNSET)
    owner: Union[
        WebhookIssuesTransferredPropChangesPropNewRepositoryPropOwner, None
    ] = Field(title="User")
    permissions: Missing[
        WebhookIssuesTransferredPropChangesPropNewRepositoryPropPermissions
    ] = Field(default=UNSET)
    private: bool = Field(description="Whether the repository is private or public.")
    public: Missing[bool] = Field(default=UNSET)
    pulls_url: str = Field()
    pushed_at: Union[int, datetime, None] = Field()
    releases_url: str = Field()
    role_name: Missing[Union[str, None]] = Field(default=UNSET)
    size: int = Field()
    ssh_url: str = Field()
    stargazers: Missing[int] = Field(default=UNSET)
    stargazers_count: int = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    svn_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    topics: List[str] = Field()
    trees_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()
    visibility: Literal["public", "private", "internal"] = Field()
    watchers: int = Field()
    watchers_count: int = Field()
    web_commit_signoff_required: Missing[bool] = Field(
        default=UNSET,
        description="Whether to require contributors to sign off on web-based commits",
    )


class WebhookIssuesTransferredPropChangesPropNewRepositoryPropCustomProperties(
    ExtraGitHubModel
):
    """WebhookIssuesTransferredPropChangesPropNewRepositoryPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


class WebhookIssuesTransferredPropChangesPropNewRepositoryPropLicense(GitHubModel):
    """License"""

    key: str = Field()
    name: str = Field()
    node_id: str = Field()
    spdx_id: str = Field()
    url: Union[str, None] = Field()


class WebhookIssuesTransferredPropChangesPropNewRepositoryPropOwner(GitHubModel):
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


class WebhookIssuesTransferredPropChangesPropNewRepositoryPropPermissions(GitHubModel):
    """WebhookIssuesTransferredPropChangesPropNewRepositoryPropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)


model_rebuild(WebhookIssuesTransferred)
model_rebuild(WebhookIssuesTransferredPropChanges)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssue)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropAssignee)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropAssigneesItems)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropLabelsItems)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropMilestone)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropMilestonePropCreator)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubApp)
model_rebuild(
    WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropOwner
)
model_rebuild(
    WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropPermissions
)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropPullRequest)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropReactions)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewIssuePropUser)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewRepository)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewRepositoryPropCustomProperties)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewRepositoryPropLicense)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewRepositoryPropOwner)
model_rebuild(WebhookIssuesTransferredPropChangesPropNewRepositoryPropPermissions)

__all__ = (
    "WebhookIssuesTransferred",
    "WebhookIssuesTransferredPropChanges",
    "WebhookIssuesTransferredPropChangesPropNewIssue",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropAssignee",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropAssigneesItems",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropLabelsItems",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropMilestone",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropMilestonePropCreator",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubApp",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropOwner",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropPerformedViaGithubAppPropPermissions",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropPullRequest",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropReactions",
    "WebhookIssuesTransferredPropChangesPropNewIssuePropUser",
    "WebhookIssuesTransferredPropChangesPropNewRepository",
    "WebhookIssuesTransferredPropChangesPropNewRepositoryPropCustomProperties",
    "WebhookIssuesTransferredPropChangesPropNewRepositoryPropLicense",
    "WebhookIssuesTransferredPropChangesPropNewRepositoryPropOwner",
    "WebhookIssuesTransferredPropChangesPropNewRepositoryPropPermissions",
)
