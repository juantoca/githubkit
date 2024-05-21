"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0119 import RepositoryRulesetConditionsType
from .group_0722 import (
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsType,
)


class WebhookRepositoryRulesetEditedPropChangesPropConditionsType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropConditions"""

    added: NotRequired[List[RepositoryRulesetConditionsType]]
    deleted: NotRequired[List[RepositoryRulesetConditionsType]]
    updated: NotRequired[
        List[
            WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsType
        ]
    ]


__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropConditionsType",)
