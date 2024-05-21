"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0367 import EnterpriseWebhooksType
from .group_0368 import SimpleInstallationType
from .group_0370 import RepositoryWebhooksType
from .group_0371 import SimpleUserWebhooksType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookMetaDeletedType(TypedDict):
    """meta deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    hook: WebhookMetaDeletedPropHookType
    hook_id: int
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[Union[None, RepositoryWebhooksType]]
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookMetaDeletedPropHookType(TypedDict):
    """WebhookMetaDeletedPropHook

    The modified webhook. This will contain different keys based on the type of
    webhook it is: repository, organization, business, app, or GitHub Marketplace.
    """

    active: bool
    config: WebhookMetaDeletedPropHookPropConfigType
    created_at: str
    events: List[
        Literal[
            "*",
            "branch_protection_rule",
            "check_run",
            "check_suite",
            "code_scanning_alert",
            "commit_comment",
            "create",
            "delete",
            "deployment",
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
            "meta",
            "milestone",
            "organization",
            "org_block",
            "package",
            "page_build",
            "project",
            "project_card",
            "project_column",
            "public",
            "pull_request",
            "pull_request_review",
            "pull_request_review_comment",
            "pull_request_review_thread",
            "push",
            "registry_package",
            "release",
            "repository",
            "repository_import",
            "repository_vulnerability_alert",
            "secret_scanning_alert",
            "secret_scanning_alert_location",
            "security_and_analysis",
            "star",
            "status",
            "team",
            "team_add",
            "watch",
            "workflow_job",
            "workflow_run",
            "repository_dispatch",
            "projects_v2_item",
        ]
    ]
    id: int
    name: str
    type: str
    updated_at: str


class WebhookMetaDeletedPropHookPropConfigType(TypedDict):
    """WebhookMetaDeletedPropHookPropConfig"""

    content_type: Literal["json", "form"]
    insecure_ssl: str
    secret: NotRequired[str]
    url: str


__all__ = (
    "WebhookMetaDeletedType",
    "WebhookMetaDeletedPropHookType",
    "WebhookMetaDeletedPropHookPropConfigType",
)
