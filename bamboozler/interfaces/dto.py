from typing import FrozenSet, Mapping

from attr import dataclass
from bamboozler.entities.reminder import Reminder, ReminderContainer


@dataclass(frozen=True)
class UpsertAllRequest:
    reminders: Mapping[ReminderContainer, FrozenSet[Reminder]]


@dataclass(frozen=True)
class UpsertReminderQuery:
    items: FrozenSet[Reminder]


@dataclass(frozen=True)
class UpsertReminderAnswer:
    items: FrozenSet[Reminder]


@dataclass(frozen=True)
class UpsertReminderContainerQuery:
    items: FrozenSet[ReminderContainer]


@dataclass(frozen=True)
class UpsertReminderContainerAnswer:
    items: FrozenSet[ReminderContainer]
