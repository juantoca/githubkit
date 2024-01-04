"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0Type(
    TypedDict
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropAccountType
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropPlanType
    unit_count: int


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0Type",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropAccountType",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof0PropPlanType",
)
