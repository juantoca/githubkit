"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Optional


from githubkit.utils import exclude_unset

if TYPE_CHECKING:
    from typing import List

    from githubkit import GitHubCore
    from githubkit.response import Response

    from ..models import GitignoreTemplate


class GitignoreClient:
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

    def get_all_templates(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[str]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/gitignore/gitignore#get-all-gitignore-templates"""

        from typing import List

        url = "/gitignore/templates"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[str],
        )

    async def async_get_all_templates(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[str]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/gitignore/gitignore#get-all-gitignore-templates"""

        from typing import List

        url = "/gitignore/templates"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[str],
        )

    def get_template(
        self,
        name: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitignoreTemplate]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/gitignore/gitignore#get-a-gitignore-template"""

        from ..models import GitignoreTemplate

        url = f"/gitignore/templates/{name}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitignoreTemplate,
        )

    async def async_get_template(
        self,
        name: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitignoreTemplate]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/gitignore/gitignore#get-a-gitignore-template"""

        from ..models import GitignoreTemplate

        url = f"/gitignore/templates/{name}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitignoreTemplate,
        )
