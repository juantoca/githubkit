"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookBranchProtectionRuleEditedType(TypedDict):
    """branch protection rule edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookBranchProtectionRuleEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    rule: WebhookBranchProtectionRuleEditedPropRuleType
    sender: SimpleUserWebhooksType


class WebhookBranchProtectionRuleEditedPropRuleType(TypedDict):
    """branch protection rule

    The branch protection rule. Includes a `name` and all the [branch protection
    settings](https://docs.github.com/github/administering-a-repository/defining-
    the-mergeability-of-pull-requests/about-protected-branches#about-branch-
    protection-settings) applied to branches that match the name. Binary settings
    are boolean. Multi-level configurations are one of `off`, `non_admins`, or
    `everyone`. Actor and build lists are arrays of strings.
    """

    admin_enforced: bool
    allow_deletions_enforcement_level: Literal["off", "non_admins", "everyone"]
    allow_force_pushes_enforcement_level: Literal["off", "non_admins", "everyone"]
    authorized_actor_names: List[str]
    authorized_actors_only: bool
    authorized_dismissal_actors_only: bool
    create_protected: NotRequired[bool]
    created_at: datetime
    dismiss_stale_reviews_on_push: bool
    id: int
    ignore_approvals_from_contributors: bool
    linear_history_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ]
    merge_queue_enforcement_level: Literal["off", "non_admins", "everyone"]
    name: str
    pull_request_reviews_enforcement_level: Literal["off", "non_admins", "everyone"]
    repository_id: int
    require_code_owner_review: bool
    require_last_push_approval: NotRequired[bool]
    required_approving_review_count: int
    required_conversation_resolution_level: Literal["off", "non_admins", "everyone"]
    required_deployments_enforcement_level: Literal["off", "non_admins", "everyone"]
    required_status_checks: List[str]
    required_status_checks_enforcement_level: Literal["off", "non_admins", "everyone"]
    signature_requirement_enforcement_level: Literal["off", "non_admins", "everyone"]
    strict_required_status_checks_policy: bool
    updated_at: datetime


class WebhookBranchProtectionRuleEditedPropChangesType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChanges

    If the action was `edited`, the changes to the rule.
    """

    admin_enforced: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType
    ]
    authorized_actor_names: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType
    ]
    authorized_actors_only: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType
    ]
    authorized_dismissal_actors_only: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType
    ]
    linear_history_requirement_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType
    ]
    required_status_checks: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType
    ]
    required_status_checks_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType
    ]


class WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames"""

    from_: List[str]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcem
    entLevel
    """

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks"""

    from_: List[str]


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementL
    evel
    """

    from_: Literal["off", "non_admins", "everyone"]


__all__ = (
    "WebhookBranchProtectionRuleEditedType",
    "WebhookBranchProtectionRuleEditedPropRuleType",
    "WebhookBranchProtectionRuleEditedPropChangesType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType",
)
