from abc import ABC, abstractmethod

from bamboozler.interfaces import dto


class IReminderDatabase(ABC):
    # pylint: disable=too-few-public-methods
    # Other methods will follow soon
    @abstractmethod
    def create_reminder(
        self, query: dto.CreateReminderQuery
    ) -> dto.CreateReminderAnswer:
        pass
