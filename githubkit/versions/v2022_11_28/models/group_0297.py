"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class Page(GitHubModel):
    """GitHub Pages

    The configuration for GitHub Pages for a repository.
    """

    url: str = Field(description="The API address for accessing this Page resource.")
    status: Union[None, Literal["built", "building", "errored"]] = Field(
        description="The status of the most recent build of the Page."
    )
    cname: Union[str, None] = Field(description="The Pages site's custom domain")
    protected_domain_state: Missing[
        Union[None, Literal["pending", "verified", "unverified"]]
    ] = Field(default=UNSET, description="The state if the domain is verified")
    pending_domain_unverified_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The timestamp when a pending domain becomes unverified.",
    )
    custom_404: bool = Field(
        default=False, description="Whether the Page has a custom 404 page."
    )
    html_url: Missing[str] = Field(
        default=UNSET, description="The web address the Page can be accessed from."
    )
    build_type: Missing[Union[None, Literal["legacy", "workflow"]]] = Field(
        default=UNSET, description="The process in which the Page will be built."
    )
    source: Missing[PagesSourceHash] = Field(default=UNSET, title="Pages Source Hash")
    public: bool = Field(
        description="Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site."
    )
    https_certificate: Missing[PagesHttpsCertificate] = Field(
        default=UNSET, title="Pages Https Certificate"
    )
    https_enforced: Missing[bool] = Field(
        default=UNSET, description="Whether https is enabled on the domain"
    )


class PagesSourceHash(GitHubModel):
    """Pages Source Hash"""

    branch: str = Field()
    path: str = Field()


class PagesHttpsCertificate(GitHubModel):
    """Pages Https Certificate"""

    state: Literal[
        "new",
        "authorization_created",
        "authorization_pending",
        "authorized",
        "authorization_revoked",
        "issued",
        "uploaded",
        "approved",
        "errored",
        "bad_authz",
        "destroy_pending",
        "dns_changed",
    ] = Field()
    description: str = Field()
    domains: List[str] = Field(
        description="Array of the domain set and its alternate name (if it is configured)"
    )
    expires_at: Missing[date] = Field(default=UNSET)


model_rebuild(Page)
model_rebuild(PagesSourceHash)
model_rebuild(PagesHttpsCertificate)

__all__ = (
    "Page",
    "PagesSourceHash",
    "PagesHttpsCertificate",
)
