"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0358 import DiscussionType
from .group_0351 import EnterpriseWebhooksType
from .group_0352 import SimpleInstallationType
from .group_0354 import RepositoryWebhooksType
from .group_0355 import SimpleUserWebhooksType
from .group_0353 import OrganizationSimpleWebhooksType


class WebhookDiscussionClosedType(TypedDict):
    """discussion closed event"""

    action: Literal["closed"]
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookDiscussionClosedType",)
