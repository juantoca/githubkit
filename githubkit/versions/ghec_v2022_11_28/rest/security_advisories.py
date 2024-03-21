"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import BaseModel

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import List, Union, Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import (
        FullRepository,
        GlobalAdvisory,
        RepositoryAdvisory,
        AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
    )
    from ..types import (
        RepositoryAdvisoryCreateType,
        RepositoryAdvisoryUpdateType,
        PrivateVulnerabilityReportCreateType,
        RepositoryAdvisoryCreatePropCreditsItemsType,
        RepositoryAdvisoryUpdatePropCreditsItemsType,
        RepositoryAdvisoryCreatePropVulnerabilitiesItemsType,
        RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType,
        PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsType,
    )


class SecurityAdvisoriesClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def list_global_advisories(
        self,
        ghsa_id: Missing[str] = UNSET,
        type: Missing[Literal["reviewed", "malware", "unreviewed"]] = UNSET,
        cve_id: Missing[str] = UNSET,
        ecosystem: Missing[
            Literal[
                "actions",
                "composer",
                "erlang",
                "go",
                "maven",
                "npm",
                "nuget",
                "other",
                "pip",
                "pub",
                "rubygems",
                "rust",
            ]
        ] = UNSET,
        severity: Missing[
            Literal["unknown", "low", "medium", "high", "critical"]
        ] = UNSET,
        cwes: Missing[Union[str, List[str]]] = UNSET,
        is_withdrawn: Missing[bool] = UNSET,
        affects: Missing[Union[str, List[str]]] = UNSET,
        published: Missing[str] = UNSET,
        updated: Missing[str] = UNSET,
        modified: Missing[str] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        sort: Missing[Literal["updated", "published"]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[GlobalAdvisory]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/global-advisories#list-global-security-advisories"""

        from typing import List

        from ..models import BasicError, GlobalAdvisory, ValidationErrorSimple

        url = "/advisories"

        params = {
            "ghsa_id": ghsa_id,
            "type": type,
            "cve_id": cve_id,
            "ecosystem": ecosystem,
            "severity": severity,
            "cwes": cwes,
            "is_withdrawn": is_withdrawn,
            "affects": affects,
            "published": published,
            "updated": updated,
            "modified": modified,
            "before": before,
            "after": after,
            "direction": direction,
            "per_page": per_page,
            "sort": sort,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[GlobalAdvisory],
            error_models={
                "429": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    async def async_list_global_advisories(
        self,
        ghsa_id: Missing[str] = UNSET,
        type: Missing[Literal["reviewed", "malware", "unreviewed"]] = UNSET,
        cve_id: Missing[str] = UNSET,
        ecosystem: Missing[
            Literal[
                "actions",
                "composer",
                "erlang",
                "go",
                "maven",
                "npm",
                "nuget",
                "other",
                "pip",
                "pub",
                "rubygems",
                "rust",
            ]
        ] = UNSET,
        severity: Missing[
            Literal["unknown", "low", "medium", "high", "critical"]
        ] = UNSET,
        cwes: Missing[Union[str, List[str]]] = UNSET,
        is_withdrawn: Missing[bool] = UNSET,
        affects: Missing[Union[str, List[str]]] = UNSET,
        published: Missing[str] = UNSET,
        updated: Missing[str] = UNSET,
        modified: Missing[str] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        sort: Missing[Literal["updated", "published"]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[GlobalAdvisory]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/global-advisories#list-global-security-advisories"""

        from typing import List

        from ..models import BasicError, GlobalAdvisory, ValidationErrorSimple

        url = "/advisories"

        params = {
            "ghsa_id": ghsa_id,
            "type": type,
            "cve_id": cve_id,
            "ecosystem": ecosystem,
            "severity": severity,
            "cwes": cwes,
            "is_withdrawn": is_withdrawn,
            "affects": affects,
            "published": published,
            "updated": updated,
            "modified": modified,
            "before": before,
            "after": after,
            "direction": direction,
            "per_page": per_page,
            "sort": sort,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[GlobalAdvisory],
            error_models={
                "429": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    def get_global_advisory(
        self,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GlobalAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/global-advisories#get-a-global-security-advisory"""

        from ..models import BasicError, GlobalAdvisory

        url = f"/advisories/{ghsa_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GlobalAdvisory,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_global_advisory(
        self,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GlobalAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/global-advisories#get-a-global-security-advisory"""

        from ..models import BasicError, GlobalAdvisory

        url = f"/advisories/{ghsa_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GlobalAdvisory,
            error_models={
                "404": BasicError,
            },
        )

    def list_org_repository_advisories(
        self,
        org: str,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        sort: Missing[Literal["created", "updated", "published"]] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        per_page: Missing[int] = UNSET,
        state: Missing[Literal["triage", "draft", "published", "closed"]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[RepositoryAdvisory]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#list-repository-security-advisories-for-an-organization"""

        from typing import List

        from ..models import BasicError, RepositoryAdvisory

        url = f"/orgs/{org}/security-advisories"

        params = {
            "direction": direction,
            "sort": sort,
            "before": before,
            "after": after,
            "per_page": per_page,
            "state": state,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[RepositoryAdvisory],
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_org_repository_advisories(
        self,
        org: str,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        sort: Missing[Literal["created", "updated", "published"]] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        per_page: Missing[int] = UNSET,
        state: Missing[Literal["triage", "draft", "published", "closed"]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[RepositoryAdvisory]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#list-repository-security-advisories-for-an-organization"""

        from typing import List

        from ..models import BasicError, RepositoryAdvisory

        url = f"/orgs/{org}/security-advisories"

        params = {
            "direction": direction,
            "sort": sort,
            "before": before,
            "after": after,
            "per_page": per_page,
            "state": state,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[RepositoryAdvisory],
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    def list_repository_advisories(
        self,
        owner: str,
        repo: str,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        sort: Missing[Literal["created", "updated", "published"]] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        per_page: Missing[int] = UNSET,
        state: Missing[Literal["triage", "draft", "published", "closed"]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[RepositoryAdvisory]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#list-repository-security-advisories"""

        from typing import List

        from ..models import BasicError, RepositoryAdvisory

        url = f"/repos/{owner}/{repo}/security-advisories"

        params = {
            "direction": direction,
            "sort": sort,
            "before": before,
            "after": after,
            "per_page": per_page,
            "state": state,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[RepositoryAdvisory],
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_repository_advisories(
        self,
        owner: str,
        repo: str,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        sort: Missing[Literal["created", "updated", "published"]] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        per_page: Missing[int] = UNSET,
        state: Missing[Literal["triage", "draft", "published", "closed"]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[RepositoryAdvisory]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#list-repository-security-advisories"""

        from typing import List

        from ..models import BasicError, RepositoryAdvisory

        url = f"/repos/{owner}/{repo}/security-advisories"

        params = {
            "direction": direction,
            "sort": sort,
            "before": before,
            "after": after,
            "per_page": per_page,
            "state": state,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[RepositoryAdvisory],
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: RepositoryAdvisoryCreateType,
    ) -> Response[RepositoryAdvisory]: ...

    @overload
    def create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        summary: str,
        description: str,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: List[RepositoryAdvisoryCreatePropVulnerabilitiesItemsType],
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryCreatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        start_private_fork: Missing[bool] = UNSET,
    ) -> Response[RepositoryAdvisory]: ...

    def create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[RepositoryAdvisoryCreateType] = UNSET,
        **kwargs,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#create-a-repository-security-advisory"""

        from ..models import (
            BasicError,
            ValidationError,
            RepositoryAdvisory,
            RepositoryAdvisoryCreate,
        )

        url = f"/repos/{owner}/{repo}/security-advisories"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(RepositoryAdvisoryCreate, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: RepositoryAdvisoryCreateType,
    ) -> Response[RepositoryAdvisory]: ...

    @overload
    async def async_create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        summary: str,
        description: str,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: List[RepositoryAdvisoryCreatePropVulnerabilitiesItemsType],
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryCreatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        start_private_fork: Missing[bool] = UNSET,
    ) -> Response[RepositoryAdvisory]: ...

    async def async_create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[RepositoryAdvisoryCreateType] = UNSET,
        **kwargs,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#create-a-repository-security-advisory"""

        from ..models import (
            BasicError,
            ValidationError,
            RepositoryAdvisory,
            RepositoryAdvisoryCreate,
        )

        url = f"/repos/{owner}/{repo}/security-advisories"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(RepositoryAdvisoryCreate, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    def create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: PrivateVulnerabilityReportCreateType,
    ) -> Response[RepositoryAdvisory]: ...

    @overload
    def create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        summary: str,
        description: str,
        vulnerabilities: Missing[
            Union[
                List[PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsType], None
            ]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        start_private_fork: Missing[bool] = UNSET,
    ) -> Response[RepositoryAdvisory]: ...

    def create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[PrivateVulnerabilityReportCreateType] = UNSET,
        **kwargs,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#privately-report-a-security-vulnerability"""

        from ..models import (
            BasicError,
            ValidationError,
            RepositoryAdvisory,
            PrivateVulnerabilityReportCreate,
        )

        url = f"/repos/{owner}/{repo}/security-advisories/reports"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(PrivateVulnerabilityReportCreate, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: PrivateVulnerabilityReportCreateType,
    ) -> Response[RepositoryAdvisory]: ...

    @overload
    async def async_create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        summary: str,
        description: str,
        vulnerabilities: Missing[
            Union[
                List[PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsType], None
            ]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        start_private_fork: Missing[bool] = UNSET,
    ) -> Response[RepositoryAdvisory]: ...

    async def async_create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[PrivateVulnerabilityReportCreateType] = UNSET,
        **kwargs,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#privately-report-a-security-vulnerability"""

        from ..models import (
            BasicError,
            ValidationError,
            RepositoryAdvisory,
            PrivateVulnerabilityReportCreate,
        )

        url = f"/repos/{owner}/{repo}/security-advisories/reports"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(PrivateVulnerabilityReportCreate, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    def get_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#get-a-repository-security-advisory"""

        from ..models import BasicError, RepositoryAdvisory

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#get-a-repository-security-advisory"""

        from ..models import BasicError, RepositoryAdvisory

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: RepositoryAdvisoryUpdateType,
    ) -> Response[RepositoryAdvisory]: ...

    @overload
    def update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        summary: Missing[str] = UNSET,
        description: Missing[str] = UNSET,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: Missing[
            List[RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryUpdatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        state: Missing[Literal["published", "closed", "draft"]] = UNSET,
        collaborating_users: Missing[Union[List[str], None]] = UNSET,
        collaborating_teams: Missing[Union[List[str], None]] = UNSET,
    ) -> Response[RepositoryAdvisory]: ...

    def update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[RepositoryAdvisoryUpdateType] = UNSET,
        **kwargs,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#update-a-repository-security-advisory"""

        from ..models import (
            BasicError,
            ValidationError,
            RepositoryAdvisory,
            RepositoryAdvisoryUpdate,
        )

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(RepositoryAdvisoryUpdate, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: RepositoryAdvisoryUpdateType,
    ) -> Response[RepositoryAdvisory]: ...

    @overload
    async def async_update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        summary: Missing[str] = UNSET,
        description: Missing[str] = UNSET,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: Missing[
            List[RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryUpdatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        state: Missing[Literal["published", "closed", "draft"]] = UNSET,
        collaborating_users: Missing[Union[List[str], None]] = UNSET,
        collaborating_teams: Missing[Union[List[str], None]] = UNSET,
    ) -> Response[RepositoryAdvisory]: ...

    async def async_update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[RepositoryAdvisoryUpdateType] = UNSET,
        **kwargs,
    ) -> Response[RepositoryAdvisory]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#update-a-repository-security-advisory"""

        from ..models import (
            BasicError,
            ValidationError,
            RepositoryAdvisory,
            RepositoryAdvisoryUpdate,
        )

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(RepositoryAdvisoryUpdate, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    def create_repository_advisory_cve_request(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#request-a-cve-for-a-repository-security-advisory"""

        from ..models import (
            BasicError,
            ValidationError,
            AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
        )

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    async def async_create_repository_advisory_cve_request(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#request-a-cve-for-a-repository-security-advisory"""

        from ..models import (
            BasicError,
            ValidationError,
            AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
        )

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    def create_fork(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[FullRepository]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#create-a-temporary-private-fork"""

        from ..models import BasicError, FullRepository, ValidationError

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=FullRepository,
            error_models={
                "400": BasicError,
                "422": ValidationError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_create_fork(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[FullRepository]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/security-advisories/repository-advisories#create-a-temporary-private-fork"""

        from ..models import BasicError, FullRepository, ValidationError

        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=FullRepository,
            error_models={
                "400": BasicError,
                "422": ValidationError,
                "403": BasicError,
                "404": BasicError,
            },
        )
