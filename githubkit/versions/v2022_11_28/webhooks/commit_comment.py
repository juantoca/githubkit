"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias


from ..models import WebhookCommitCommentCreated

Event: TypeAlias = WebhookCommitCommentCreated

CommitCommentEvent: TypeAlias = Event

action_types = WebhookCommitCommentCreated

commit_comment_action_types = action_types

__all__ = ("Event", "CommitCommentEvent", "action_types", "commit_comment_action_types")
