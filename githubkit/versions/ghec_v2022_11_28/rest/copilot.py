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
    from typing import List

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..types import (
        OrgsOrgCopilotBillingSelectedTeamsPostBodyType,
        OrgsOrgCopilotBillingSelectedUsersPostBodyType,
        OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType,
        OrgsOrgCopilotBillingSelectedUsersDeleteBodyType,
    )
    from ..models import (
        CopilotSeatDetails,
        CopilotUsageMetrics,
        CopilotOrganizationDetails,
        OrgsOrgCopilotBillingSeatsGetResponse200,
        OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
        OrgsOrgCopilotBillingSelectedUsersPostResponse201,
        OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
        OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
        EnterprisesEnterpriseCopilotBillingSeatsGetResponse200,
    )


class CopilotClient:
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

    def list_copilot_seats_for_enterprise(
        self,
        enterprise: str,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[EnterprisesEnterpriseCopilotBillingSeatsGetResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#list-all-copilot-seat-assignments-for-an-enterprise"""

        from ..models import (
            BasicError,
            EnterprisesEnterpriseCopilotBillingSeatsGetResponse200,
        )

        url = f"/enterprises/{enterprise}/copilot/billing/seats"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=EnterprisesEnterpriseCopilotBillingSeatsGetResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_copilot_seats_for_enterprise(
        self,
        enterprise: str,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[EnterprisesEnterpriseCopilotBillingSeatsGetResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#list-all-copilot-seat-assignments-for-an-enterprise"""

        from ..models import (
            BasicError,
            EnterprisesEnterpriseCopilotBillingSeatsGetResponse200,
        )

        url = f"/enterprises/{enterprise}/copilot/billing/seats"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=EnterprisesEnterpriseCopilotBillingSeatsGetResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def usage_metrics_for_enterprise(
        self,
        enterprise: str,
        since: Missing[str] = UNSET,
        until: Missing[str] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CopilotUsageMetrics]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-usage#get-a-summary-of-copilot-usage-for-enterprise-members"""

        from typing import List

        from ..models import BasicError, CopilotUsageMetrics

        url = f"/enterprises/{enterprise}/copilot/usage"

        params = {
            "since": since,
            "until": until,
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CopilotUsageMetrics],
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_usage_metrics_for_enterprise(
        self,
        enterprise: str,
        since: Missing[str] = UNSET,
        until: Missing[str] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CopilotUsageMetrics]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-usage#get-a-summary-of-copilot-usage-for-enterprise-members"""

        from typing import List

        from ..models import BasicError, CopilotUsageMetrics

        url = f"/enterprises/{enterprise}/copilot/usage"

        params = {
            "since": since,
            "until": until,
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CopilotUsageMetrics],
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_copilot_organization_details(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CopilotOrganizationDetails]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#get-copilot-seat-information-and-settings-for-an-organization"""

        from ..models import BasicError, CopilotOrganizationDetails

        url = f"/orgs/{org}/copilot/billing"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotOrganizationDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_copilot_organization_details(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CopilotOrganizationDetails]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#get-copilot-seat-information-and-settings-for-an-organization"""

        from ..models import BasicError, CopilotOrganizationDetails

        url = f"/orgs/{org}/copilot/billing"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotOrganizationDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def list_copilot_seats(
        self,
        org: str,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[OrgsOrgCopilotBillingSeatsGetResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#list-all-copilot-seat-assignments-for-an-organization"""

        from ..models import BasicError, OrgsOrgCopilotBillingSeatsGetResponse200

        url = f"/orgs/{org}/copilot/billing/seats"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSeatsGetResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_copilot_seats(
        self,
        org: str,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[OrgsOrgCopilotBillingSeatsGetResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#list-all-copilot-seat-assignments-for-an-organization"""

        from ..models import BasicError, OrgsOrgCopilotBillingSeatsGetResponse200

        url = f"/orgs/{org}/copilot/billing/seats"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSeatsGetResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def add_copilot_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsPostBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]: ...

    @overload
    def add_copilot_seats_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]: ...

    def add_copilot_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#add-teams-to-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedTeamsPostBody,
            OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
        )

        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedTeamsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_add_copilot_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsPostBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]: ...

    @overload
    async def async_add_copilot_seats_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]: ...

    async def async_add_copilot_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#add-teams-to-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedTeamsPostBody,
            OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
        )

        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedTeamsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]: ...

    @overload
    def cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]: ...

    def cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#remove-teams-from-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedTeamsDeleteBody,
            OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
        )

        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedTeamsDeleteBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]: ...

    @overload
    async def async_cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]: ...

    async def async_cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#remove-teams-from-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedTeamsDeleteBody,
            OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
        )

        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedTeamsDeleteBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def add_copilot_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersPostBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]: ...

    @overload
    def add_copilot_seats_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]: ...

    def add_copilot_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#add-users-to-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedUsersPostBody,
            OrgsOrgCopilotBillingSelectedUsersPostResponse201,
        )

        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedUsersPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_add_copilot_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersPostBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]: ...

    @overload
    async def async_add_copilot_seats_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]: ...

    async def async_add_copilot_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#add-users-to-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedUsersPostBody,
            OrgsOrgCopilotBillingSelectedUsersPostResponse201,
        )

        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedUsersPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersDeleteBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]: ...

    @overload
    def cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]: ...

    def cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersDeleteBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#remove-users-from-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedUsersDeleteBody,
            OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
        )

        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedUsersDeleteBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersDeleteBodyType,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]: ...

    @overload
    async def async_cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]: ...

    async def async_cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersDeleteBodyType] = UNSET,
        **kwargs,
    ) -> Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#remove-users-from-the-copilot-subscription-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCopilotBillingSelectedUsersDeleteBody,
            OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
        )

        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCopilotBillingSelectedUsersDeleteBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def usage_metrics_for_org(
        self,
        org: str,
        since: Missing[str] = UNSET,
        until: Missing[str] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CopilotUsageMetrics]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-usage#get-a-summary-of-copilot-usage-for-organization-members"""

        from typing import List

        from ..models import BasicError, CopilotUsageMetrics

        url = f"/orgs/{org}/copilot/usage"

        params = {
            "since": since,
            "until": until,
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CopilotUsageMetrics],
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_usage_metrics_for_org(
        self,
        org: str,
        since: Missing[str] = UNSET,
        until: Missing[str] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CopilotUsageMetrics]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-usage#get-a-summary-of-copilot-usage-for-organization-members"""

        from typing import List

        from ..models import BasicError, CopilotUsageMetrics

        url = f"/orgs/{org}/copilot/usage"

        params = {
            "since": since,
            "until": until,
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CopilotUsageMetrics],
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_copilot_seat_details_for_user(
        self,
        org: str,
        username: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CopilotSeatDetails]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#get-copilot-seat-assignment-details-for-a-user"""

        from ..models import BasicError, CopilotSeatDetails

        url = f"/orgs/{org}/members/{username}/copilot"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotSeatDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_copilot_seat_details_for_user(
        self,
        org: str,
        username: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CopilotSeatDetails]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/copilot/copilot-user-management#get-copilot-seat-assignment-details-for-a-user"""

        from ..models import BasicError, CopilotSeatDetails

        url = f"/orgs/{org}/members/{username}/copilot"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotSeatDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )
