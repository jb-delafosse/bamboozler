from typing import FrozenSet

from bamboozler.entities.reminder import Reminder
from bamboozler.interfaces import gateways
from bamboozler.interfaces.dto import (
    UpsertAllRequest,
    UpsertReminderContainerQuery,
    UpsertReminderQuery,
)


class UseCaseReminder:
    """
    Describe the way to create a task in the external Task App

    Everything is done in the context of a ReminderContainer
    """

    def __init__(self) -> None:
        self._db = gateways.REMINDER_DATABASE_FACTORY()

    def upsert_all(self, upsert_reminder_request: UpsertAllRequest) -> None:
        # upsert the containers
        containers = frozenset(upsert_reminder_request.reminders.keys())
        self._db.upsert_multi_reminder_container(
            UpsertReminderContainerQuery(items=containers)
        )

        # upsert the reminders
        all_reminders: FrozenSet[Reminder] = frozenset().union(  # type: ignore
            *tuple(upsert_reminder_request.reminders.values())  # type: ignore
        )
        self._db.upsert_multi_reminder(UpsertReminderQuery(all_reminders))
