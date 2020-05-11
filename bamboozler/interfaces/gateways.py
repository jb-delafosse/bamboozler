from abc import ABC, abstractmethod
from typing import Callable

from bamboozler.interfaces import dto


class IReminderDatabase(ABC):
    @abstractmethod
    def upsert_multi_reminder_container(
        self, query: dto.UpsertReminderContainerQuery
    ) -> dto.UpsertReminderContainerAnswer:
        pass

    @abstractmethod
    def upsert_multi_reminder(
        self, query: dto.UpsertReminderQuery
    ) -> dto.UpsertReminderAnswer:
        pass


# The contract for a database gateway factory
ReminderDatabaseFactory = Callable[[], IReminderDatabase]

# The database gateway factory to use to get the good implementation of the ICustomerDatabase.
# It can be set in main or tests.
REMINDER_DATABASE_FACTORY: ReminderDatabaseFactory
