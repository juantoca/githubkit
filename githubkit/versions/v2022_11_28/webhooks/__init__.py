"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fork import ForkEvent as ForkEvent
    from .meta import MetaEvent as MetaEvent
    from .ping import PingEvent as PingEvent
    from .push import PushEvent as PushEvent
    from .star import StarEvent as StarEvent
    from .team import TeamEvent as TeamEvent
    from .label import LabelEvent as LabelEvent
    from .watch import WatchEvent as WatchEvent
    from .create import CreateEvent as CreateEvent
    from .delete import DeleteEvent as DeleteEvent
    from .gollum import GollumEvent as GollumEvent
    from .issues import IssuesEvent as IssuesEvent
    from .member import MemberEvent as MemberEvent
    from .public import PublicEvent as PublicEvent
    from .status import StatusEvent as StatusEvent
    from ._types import WebhookEvent as WebhookEvent
    from .package import PackageEvent as PackageEvent
    from .project import ProjectEvent as ProjectEvent
    from .release import ReleaseEvent as ReleaseEvent
    from .team_add import TeamAddEvent as TeamAddEvent
    from .check_run import CheckRunEvent as CheckRunEvent
    from .org_block import OrgBlockEvent as OrgBlockEvent
    from ._namespace import EventNameType as EventNameType
    from .milestone import MilestoneEvent as MilestoneEvent
    from .deploy_key import DeployKeyEvent as DeployKeyEvent
    from .fork import fork_action_types as fork_action_types
    from .meta import meta_action_types as meta_action_types
    from .page_build import PageBuildEvent as PageBuildEvent
    from .ping import ping_action_types as ping_action_types
    from .push import push_action_types as push_action_types
    from .star import star_action_types as star_action_types
    from .team import team_action_types as team_action_types
    from .deployment import DeploymentEvent as DeploymentEvent
    from .discussion import DiscussionEvent as DiscussionEvent
    from .membership import MembershipEvent as MembershipEvent
    from .repository import RepositoryEvent as RepositoryEvent
    from .check_suite import CheckSuiteEvent as CheckSuiteEvent
    from .label import label_action_types as label_action_types
    from .merge_group import MergeGroupEvent as MergeGroupEvent
    from .projects_v2 import ProjectsV2Event as ProjectsV2Event
    from .watch import watch_action_types as watch_action_types
    from ._namespace import WebhookNamespace as WebhookNamespace
    from .sponsorship import SponsorshipEvent as SponsorshipEvent
    from ._namespace import VALID_EVENT_NAMES as VALID_EVENT_NAMES
    from ._types import webhook_event_types as webhook_event_types
    from .create import create_action_types as create_action_types
    from .delete import delete_action_types as delete_action_types
    from .gollum import gollum_action_types as gollum_action_types
    from .issues import issues_action_types as issues_action_types
    from .member import member_action_types as member_action_types
    from .project_card import ProjectCardEvent as ProjectCardEvent
    from .public import public_action_types as public_action_types
    from .pull_request import PullRequestEvent as PullRequestEvent
    from .status import status_action_types as status_action_types
    from .workflow_job import WorkflowJobEvent as WorkflowJobEvent
    from .workflow_run import WorkflowRunEvent as WorkflowRunEvent
    from ._types import webhook_action_types as webhook_action_types
    from .installation import InstallationEvent as InstallationEvent
    from .organization import OrganizationEvent as OrganizationEvent
    from .issue_comment import IssueCommentEvent as IssueCommentEvent
    from .package import package_action_types as package_action_types
    from .project import project_action_types as project_action_types
    from .release import release_action_types as release_action_types
    from .commit_comment import CommitCommentEvent as CommitCommentEvent
    from .project_column import ProjectColumnEvent as ProjectColumnEvent
    from .team_add import team_add_action_types as team_add_action_types
    from .check_run import check_run_action_types as check_run_action_types
    from .custom_property import CustomPropertyEvent as CustomPropertyEvent
    from .milestone import milestone_action_types as milestone_action_types
    from .org_block import org_block_action_types as org_block_action_types
    from .projects_v2_item import ProjectsV2ItemEvent as ProjectsV2ItemEvent
    from .dependabot_alert import DependabotAlertEvent as DependabotAlertEvent
    from .deploy_key import deploy_key_action_types as deploy_key_action_types
    from .deployment import deployment_action_types as deployment_action_types
    from .discussion import discussion_action_types as discussion_action_types
    from .membership import membership_action_types as membership_action_types
    from .page_build import page_build_action_types as page_build_action_types
    from .registry_package import RegistryPackageEvent as RegistryPackageEvent
    from .repository import repository_action_types as repository_action_types
    from .check_suite import check_suite_action_types as check_suite_action_types
    from .deployment_review import DeploymentReviewEvent as DeploymentReviewEvent
    from .deployment_status import DeploymentStatusEvent as DeploymentStatusEvent
    from .merge_group import merge_group_action_types as merge_group_action_types
    from .projects_v2 import projects_v2_action_types as projects_v2_action_types
    from .repository_import import RepositoryImportEvent as RepositoryImportEvent
    from .security_advisory import SecurityAdvisoryEvent as SecurityAdvisoryEvent
    from .sponsorship import sponsorship_action_types as sponsorship_action_types
    from .workflow_dispatch import WorkflowDispatchEvent as WorkflowDispatchEvent
    from .discussion_comment import DiscussionCommentEvent as DiscussionCommentEvent
    from .installation import installation_action_types as installation_action_types
    from .organization import organization_action_types as organization_action_types
    from .project_card import project_card_action_types as project_card_action_types
    from .pull_request import pull_request_action_types as pull_request_action_types
    from .repository_ruleset import RepositoryRulesetEvent as RepositoryRulesetEvent
    from .workflow_job import workflow_job_action_types as workflow_job_action_types
    from .workflow_run import workflow_run_action_types as workflow_run_action_types
    from .code_scanning_alert import CodeScanningAlertEvent as CodeScanningAlertEvent
    from .pull_request_review import PullRequestReviewEvent as PullRequestReviewEvent
    from .installation_target import InstallationTargetEvent as InstallationTargetEvent
    from .issue_comment import issue_comment_action_types as issue_comment_action_types
    from .repository_advisory import RepositoryAdvisoryEvent as RepositoryAdvisoryEvent
    from .repository_dispatch import RepositoryDispatchEvent as RepositoryDispatchEvent
    from .commit_comment import (
        commit_comment_action_types as commit_comment_action_types,
    )
    from .marketplace_purchase import (
        MarketplacePurchaseEvent as MarketplacePurchaseEvent,
    )
    from .project_column import (
        project_column_action_types as project_column_action_types,
    )
    from .secret_scanning_alert import (
        SecretScanningAlertEvent as SecretScanningAlertEvent,
    )
    from .security_and_analysis import (
        SecurityAndAnalysisEvent as SecurityAndAnalysisEvent,
    )
    from .custom_property import (
        custom_property_action_types as custom_property_action_types,
    )
    from .branch_protection_rule import (
        BranchProtectionRuleEvent as BranchProtectionRuleEvent,
    )
    from .custom_property_values import (
        CustomPropertyValuesEvent as CustomPropertyValuesEvent,
    )
    from .dependabot_alert import (
        dependabot_alert_action_types as dependabot_alert_action_types,
    )
    from .projects_v2_item import (
        projects_v2_item_action_types as projects_v2_item_action_types,
    )
    from .registry_package import (
        registry_package_action_types as registry_package_action_types,
    )
    from .deployment_review import (
        deployment_review_action_types as deployment_review_action_types,
    )
    from .deployment_status import (
        deployment_status_action_types as deployment_status_action_types,
    )
    from .repository_import import (
        repository_import_action_types as repository_import_action_types,
    )
    from .security_advisory import (
        security_advisory_action_types as security_advisory_action_types,
    )
    from .workflow_dispatch import (
        workflow_dispatch_action_types as workflow_dispatch_action_types,
    )
    from .github_app_authorization import (
        GithubAppAuthorizationEvent as GithubAppAuthorizationEvent,
    )
    from .projects_v2_status_update import (
        ProjectsV2StatusUpdateEvent as ProjectsV2StatusUpdateEvent,
    )
    from .discussion_comment import (
        discussion_comment_action_types as discussion_comment_action_types,
    )
    from .repository_ruleset import (
        repository_ruleset_action_types as repository_ruleset_action_types,
    )
    from .pull_request_review_thread import (
        PullRequestReviewThreadEvent as PullRequestReviewThreadEvent,
    )
    from .code_scanning_alert import (
        code_scanning_alert_action_types as code_scanning_alert_action_types,
    )
    from .installation_repositories import (
        InstallationRepositoriesEvent as InstallationRepositoriesEvent,
    )
    from .installation_target import (
        installation_target_action_types as installation_target_action_types,
    )
    from .pull_request_review import (
        pull_request_review_action_types as pull_request_review_action_types,
    )
    from .repository_advisory import (
        repository_advisory_action_types as repository_advisory_action_types,
    )
    from .repository_dispatch import (
        repository_dispatch_action_types as repository_dispatch_action_types,
    )
    from .deployment_protection_rule import (
        DeploymentProtectionRuleEvent as DeploymentProtectionRuleEvent,
    )
    from .pull_request_review_comment import (
        PullRequestReviewCommentEvent as PullRequestReviewCommentEvent,
    )
    from .marketplace_purchase import (
        marketplace_purchase_action_types as marketplace_purchase_action_types,
    )
    from .secret_scanning_alert import (
        secret_scanning_alert_action_types as secret_scanning_alert_action_types,
    )
    from .security_and_analysis import (
        security_and_analysis_action_types as security_and_analysis_action_types,
    )
    from .personal_access_token_request import (
        PersonalAccessTokenRequestEvent as PersonalAccessTokenRequestEvent,
    )
    from .branch_protection_rule import (
        branch_protection_rule_action_types as branch_protection_rule_action_types,
    )
    from .custom_property_values import (
        custom_property_values_action_types as custom_property_values_action_types,
    )
    from .secret_scanning_alert_location import (
        SecretScanningAlertLocationEvent as SecretScanningAlertLocationEvent,
    )
    from .repository_vulnerability_alert import (
        RepositoryVulnerabilityAlertEvent as RepositoryVulnerabilityAlertEvent,
    )
    from .github_app_authorization import (
        github_app_authorization_action_types as github_app_authorization_action_types,
    )
    from .branch_protection_configuration import (
        BranchProtectionConfigurationEvent as BranchProtectionConfigurationEvent,
    )
    from .installation_repositories import (
        installation_repositories_action_types as installation_repositories_action_types,
    )
    from .projects_v2_status_update import (
        projects_v2_status_update_action_types as projects_v2_status_update_action_types,
    )
    from .deployment_protection_rule import (
        deployment_protection_rule_action_types as deployment_protection_rule_action_types,
    )
    from .pull_request_review_thread import (
        pull_request_review_thread_action_types as pull_request_review_thread_action_types,
    )
    from .pull_request_review_comment import (
        pull_request_review_comment_action_types as pull_request_review_comment_action_types,
    )
    from .personal_access_token_request import (
        personal_access_token_request_action_types as personal_access_token_request_action_types,
    )
    from .repository_vulnerability_alert import (
        repository_vulnerability_alert_action_types as repository_vulnerability_alert_action_types,
    )
    from .secret_scanning_alert_location import (
        secret_scanning_alert_location_action_types as secret_scanning_alert_location_action_types,
    )
    from .branch_protection_configuration import (
        branch_protection_configuration_action_types as branch_protection_configuration_action_types,
    )
else:
    __lazy_vars__ = {
        ".branch_protection_configuration": (
            "BranchProtectionConfigurationEvent",
            "branch_protection_configuration_action_types",
        ),
        ".branch_protection_rule": (
            "BranchProtectionRuleEvent",
            "branch_protection_rule_action_types",
        ),
        ".check_run": ("CheckRunEvent", "check_run_action_types"),
        ".check_suite": ("CheckSuiteEvent", "check_suite_action_types"),
        ".code_scanning_alert": (
            "CodeScanningAlertEvent",
            "code_scanning_alert_action_types",
        ),
        ".commit_comment": ("CommitCommentEvent", "commit_comment_action_types"),
        ".create": ("CreateEvent", "create_action_types"),
        ".custom_property": ("CustomPropertyEvent", "custom_property_action_types"),
        ".custom_property_values": (
            "CustomPropertyValuesEvent",
            "custom_property_values_action_types",
        ),
        ".delete": ("DeleteEvent", "delete_action_types"),
        ".dependabot_alert": ("DependabotAlertEvent", "dependabot_alert_action_types"),
        ".deploy_key": ("DeployKeyEvent", "deploy_key_action_types"),
        ".deployment": ("DeploymentEvent", "deployment_action_types"),
        ".deployment_protection_rule": (
            "DeploymentProtectionRuleEvent",
            "deployment_protection_rule_action_types",
        ),
        ".deployment_review": (
            "DeploymentReviewEvent",
            "deployment_review_action_types",
        ),
        ".deployment_status": (
            "DeploymentStatusEvent",
            "deployment_status_action_types",
        ),
        ".discussion": ("DiscussionEvent", "discussion_action_types"),
        ".discussion_comment": (
            "DiscussionCommentEvent",
            "discussion_comment_action_types",
        ),
        ".fork": ("ForkEvent", "fork_action_types"),
        ".github_app_authorization": (
            "GithubAppAuthorizationEvent",
            "github_app_authorization_action_types",
        ),
        ".gollum": ("GollumEvent", "gollum_action_types"),
        ".installation": ("InstallationEvent", "installation_action_types"),
        ".installation_repositories": (
            "InstallationRepositoriesEvent",
            "installation_repositories_action_types",
        ),
        ".installation_target": (
            "InstallationTargetEvent",
            "installation_target_action_types",
        ),
        ".issue_comment": ("IssueCommentEvent", "issue_comment_action_types"),
        ".issues": ("IssuesEvent", "issues_action_types"),
        ".label": ("LabelEvent", "label_action_types"),
        ".marketplace_purchase": (
            "MarketplacePurchaseEvent",
            "marketplace_purchase_action_types",
        ),
        ".member": ("MemberEvent", "member_action_types"),
        ".membership": ("MembershipEvent", "membership_action_types"),
        ".merge_group": ("MergeGroupEvent", "merge_group_action_types"),
        ".meta": ("MetaEvent", "meta_action_types"),
        ".milestone": ("MilestoneEvent", "milestone_action_types"),
        ".org_block": ("OrgBlockEvent", "org_block_action_types"),
        ".organization": ("OrganizationEvent", "organization_action_types"),
        ".package": ("PackageEvent", "package_action_types"),
        ".page_build": ("PageBuildEvent", "page_build_action_types"),
        ".personal_access_token_request": (
            "PersonalAccessTokenRequestEvent",
            "personal_access_token_request_action_types",
        ),
        ".ping": ("PingEvent", "ping_action_types"),
        ".project_card": ("ProjectCardEvent", "project_card_action_types"),
        ".project": ("ProjectEvent", "project_action_types"),
        ".project_column": ("ProjectColumnEvent", "project_column_action_types"),
        ".projects_v2": ("ProjectsV2Event", "projects_v2_action_types"),
        ".projects_v2_item": ("ProjectsV2ItemEvent", "projects_v2_item_action_types"),
        ".projects_v2_status_update": (
            "ProjectsV2StatusUpdateEvent",
            "projects_v2_status_update_action_types",
        ),
        ".public": ("PublicEvent", "public_action_types"),
        ".pull_request": ("PullRequestEvent", "pull_request_action_types"),
        ".pull_request_review_comment": (
            "PullRequestReviewCommentEvent",
            "pull_request_review_comment_action_types",
        ),
        ".pull_request_review": (
            "PullRequestReviewEvent",
            "pull_request_review_action_types",
        ),
        ".pull_request_review_thread": (
            "PullRequestReviewThreadEvent",
            "pull_request_review_thread_action_types",
        ),
        ".push": ("PushEvent", "push_action_types"),
        ".registry_package": ("RegistryPackageEvent", "registry_package_action_types"),
        ".release": ("ReleaseEvent", "release_action_types"),
        ".repository_advisory": (
            "RepositoryAdvisoryEvent",
            "repository_advisory_action_types",
        ),
        ".repository": ("RepositoryEvent", "repository_action_types"),
        ".repository_dispatch": (
            "RepositoryDispatchEvent",
            "repository_dispatch_action_types",
        ),
        ".repository_import": (
            "RepositoryImportEvent",
            "repository_import_action_types",
        ),
        ".repository_ruleset": (
            "RepositoryRulesetEvent",
            "repository_ruleset_action_types",
        ),
        ".repository_vulnerability_alert": (
            "RepositoryVulnerabilityAlertEvent",
            "repository_vulnerability_alert_action_types",
        ),
        ".secret_scanning_alert": (
            "SecretScanningAlertEvent",
            "secret_scanning_alert_action_types",
        ),
        ".secret_scanning_alert_location": (
            "SecretScanningAlertLocationEvent",
            "secret_scanning_alert_location_action_types",
        ),
        ".security_advisory": (
            "SecurityAdvisoryEvent",
            "security_advisory_action_types",
        ),
        ".security_and_analysis": (
            "SecurityAndAnalysisEvent",
            "security_and_analysis_action_types",
        ),
        ".sponsorship": ("SponsorshipEvent", "sponsorship_action_types"),
        ".star": ("StarEvent", "star_action_types"),
        ".status": ("StatusEvent", "status_action_types"),
        ".team_add": ("TeamAddEvent", "team_add_action_types"),
        ".team": ("TeamEvent", "team_action_types"),
        ".watch": ("WatchEvent", "watch_action_types"),
        ".workflow_dispatch": (
            "WorkflowDispatchEvent",
            "workflow_dispatch_action_types",
        ),
        ".workflow_job": ("WorkflowJobEvent", "workflow_job_action_types"),
        ".workflow_run": ("WorkflowRunEvent", "workflow_run_action_types"),
        "._types": ("WebhookEvent", "webhook_action_types", "webhook_event_types"),
        "._namespace": ("EventNameType", "VALID_EVENT_NAMES", "WebhookNamespace"),
    }
