from enum import Enum


class EventType(str, Enum):
    """
    Central registry of application events.
    """

    # Email Events
    EMAIL_RECEIVED = "email.received"
    EMAIL_UPDATED = "email.updated"
    EMAIL_DELETED = "email.deleted"
    EMAIL_SYNC_COMPLETED = "email.sync.completed"

    # Conversation Events
    CONVERSATION_CREATED = "conversation.created"
    CONVERSATION_UPDATED = "conversation.updated"
    CONVERSATION_COMPLETED = "conversation.completed"

    # AI Events
    AI_JOB_CREATED = "ai.job.created"
    AI_PROCESSING_STARTED = "ai.processing.started"
    AI_PROCESSING_COMPLETED = "ai.processing.completed"

    # Leave Tracker Events
    LEAVE_DETECTED = "leave.detected"
    LEAVE_CONFIRMED = "leave.confirmed"
    LEAVE_REJECTED = "leave.rejected"
    LEAVE_REPORT_GENERATED = "leave.report.generated"

    # Analytics Events
    ANALYTICS_UPDATED = "analytics.updated"
    REPORT_GENERATED = "report.generated"
