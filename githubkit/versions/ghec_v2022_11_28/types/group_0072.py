"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0073 import (
    MarketplacePurchasePropMarketplacePurchaseType,
    MarketplacePurchasePropMarketplacePendingChangeType,
)


class MarketplacePurchaseType(TypedDict):
    """Marketplace Purchase

    Marketplace Purchase
    """

    url: str
    type: str
    id: int
    login: str
    organization_billing_email: NotRequired[str]
    email: NotRequired[Union[str, None]]
    marketplace_pending_change: NotRequired[
        Union[MarketplacePurchasePropMarketplacePendingChangeType, None]
    ]
    marketplace_purchase: MarketplacePurchasePropMarketplacePurchaseType


__all__ = ("MarketplacePurchaseType",)
