"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPatchBody(GitHubModel):
    """ReposOwnerRepoPatchBody"""

    name: Missing[str] = Field(default=UNSET, description="The name of the repository.")
    description: Missing[str] = Field(
        default=UNSET, description="A short description of the repository."
    )
    homepage: Missing[str] = Field(
        default=UNSET, description="A URL with more information about the repository."
    )
    private: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to make the repository private or `false` to make it public. Default: `false`.  \n**Note**: You will get a `422` error if the organization restricts [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories) to organization owners and a non-owner tries to change the value of private.",
    )
    visibility: Missing[Literal["public", "private"]] = Field(
        default=UNSET, description="The visibility of the repository."
    )
    security_and_analysis: Missing[
        Union[ReposOwnerRepoPatchBodyPropSecurityAndAnalysis, None]
    ] = Field(
        default=UNSET,
        description='Specify which security and analysis features to enable or disable for the repository.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nFor example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request:\n`{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.\n\nYou can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request.',
    )
    has_issues: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to enable issues for this repository or `false` to disable them.",
    )
    has_projects: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to enable projects for this repository or `false` to disable them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the default is `false`, and if you pass `true`, the API returns an error.",
    )
    has_wiki: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to enable the wiki for this repository or `false` to disable it.",
    )
    is_template: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to make this repo available as a template repository or `false` to prevent it.",
    )
    default_branch: Missing[str] = Field(
        default=UNSET, description="Updates the default branch for this repository."
    )
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.",
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.",
    )
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.",
    )
    allow_auto_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge.",
    )
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion.",
    )
    allow_update_branch: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to always allow a pull request head branch that is behind its base branch to be updated even if it is not required to be up to date before merging, or false otherwise.",
    )
    use_squash_pr_title_as_default: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow squash-merge commits to use pull request title, or `false` to use commit message. **This property has been deprecated. Please use `squash_merge_commit_title` instead.",
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
    archived: Missing[bool] = Field(
        default=UNSET,
        description="Whether to archive this repository. `false` will unarchive a previously archived repository.",
    )
    allow_forking: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow private forks, or `false` to prevent private forks.",
    )
    web_commit_signoff_required: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to require contributors to sign off on web-based commits, or `false` to not require contributors to sign off on web-based commits.",
    )


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysis(GitHubModel):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysis

    Specify which security and analysis features to enable or disable for the
    repository.

    To use this parameter, you must have admin permissions for the repository or be
    an owner or security manager for the organization that owns the repository. For
    more information, see "[Managing security managers in your
    organization](https://docs.github.com/organizations/managing-peoples-access-to-
    your-organization-with-roles/managing-security-managers-in-your-organization)."

    For example, to enable GitHub Advanced Security, use this data in the body of
    the `PATCH` request:
    `{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.

    You can check which security and analysis features are currently enabled by
    using a `GET /repos/{owner}/{repo}` request.
    """

    advanced_security: Missing[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurity
    ] = Field(
        default=UNSET,
        description='Use the `status` property to enable or disable GitHub Advanced Security for this repository. For more information, see "[About GitHub Advanced Security](/github/getting-started-with-github/learning-about-github/about-github-advanced-security)."',
    )
    secret_scanning: Missing[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanning
    ] = Field(
        default=UNSET,
        description='Use the `status` property to enable or disable secret scanning for this repository. For more information, see "[About secret scanning](/code-security/secret-security/about-secret-scanning)."',
    )
    secret_scanning_push_protection: Missing[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtection
    ] = Field(
        default=UNSET,
        description='Use the `status` property to enable or disable secret scanning push protection for this repository. For more information, see "[Protecting pushes with secret scanning](/code-security/secret-scanning/protecting-pushes-with-secret-scanning)."',
    )


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurity(GitHubModel):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurity

    Use the `status` property to enable or disable GitHub Advanced Security for this
    repository. For more information, see "[About GitHub Advanced
    Security](/github/getting-started-with-github/learning-about-github/about-
    github-advanced-security)."
    """

    status: Missing[str] = Field(
        default=UNSET, description="Can be `enabled` or `disabled`."
    )


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanning(GitHubModel):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanning

    Use the `status` property to enable or disable secret scanning for this
    repository. For more information, see "[About secret scanning](/code-
    security/secret-security/about-secret-scanning)."
    """

    status: Missing[str] = Field(
        default=UNSET, description="Can be `enabled` or `disabled`."
    )


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtection(
    GitHubModel
):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtection

    Use the `status` property to enable or disable secret scanning push protection
    for this repository. For more information, see "[Protecting pushes with secret
    scanning](/code-security/secret-scanning/protecting-pushes-with-secret-
    scanning)."
    """

    status: Missing[str] = Field(
        default=UNSET, description="Can be `enabled` or `disabled`."
    )


model_rebuild(ReposOwnerRepoPatchBody)
model_rebuild(ReposOwnerRepoPatchBodyPropSecurityAndAnalysis)
model_rebuild(ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurity)
model_rebuild(ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanning)
model_rebuild(
    ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtection
)

__all__ = (
    "ReposOwnerRepoPatchBody",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysis",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurity",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanning",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtection",
)
