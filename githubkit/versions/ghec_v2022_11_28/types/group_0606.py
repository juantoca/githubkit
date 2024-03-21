"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1Type(TypedDict):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1"""

    account: NotRequired[
        WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccountType
    ]
    billing_cycle: NotRequired[str]
    free_trial_ends_on: NotRequired[Union[str, None]]
    next_billing_date: Union[str, None]
    on_free_trial: NotRequired[bool]
    plan: NotRequired[
        WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlanType
    ]
    unit_count: NotRequired[int]


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccount"""

    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organization_billing_email: NotRequired[Union[str, None]]
    type: NotRequired[str]


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlan"""

    bullets: NotRequired[List[Union[str, None]]]
    description: NotRequired[str]
    has_free_trial: NotRequired[bool]
    id: NotRequired[int]
    monthly_price_in_cents: NotRequired[int]
    name: NotRequired[str]
    price_model: NotRequired[Literal["FREE", "FLAT_RATE", "PER_UNIT"]]
    unit_name: NotRequired[Union[str, None]]
    yearly_price_in_cents: NotRequired[int]


__all__ = (
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1Type",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccountType",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlanType",
)
