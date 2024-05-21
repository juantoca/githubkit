"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict

from .group_0401 import SimpleInstallationType
from .group_0404 import SimpleUserWebhooksType
from .group_0402 import OrganizationSimpleWebhooksType
from .group_0431 import PersonalAccessTokenRequestType


class WebhookPersonalAccessTokenRequestCancelledType(TypedDict):
    """personal_access_token_request cancelled event"""

    action: Literal["cancelled"]
    personal_access_token_request: PersonalAccessTokenRequestType
    organization: OrganizationSimpleWebhooksType
    sender: SimpleUserWebhooksType
    installation: SimpleInstallationType


__all__ = ("WebhookPersonalAccessTokenRequestCancelledType",)
