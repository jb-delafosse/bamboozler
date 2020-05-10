# pylint: disable=R0801
# TaskRessource look the same but it's good to use different DTOs
from datetime import datetime
from typing import List, Optional

from sqlalchemy import Enum

from attr import dataclass


class ReminderStatus(Enum):  # pylint: disable=too-few-public-methods
    TODO = "TODO"
    DONE = "DONE"


@dataclass(frozen=True)
class CreateReminderQuery:
    # pylint: disable=too-many-instance-attributes
    # 8 is not that much
    reminder_id: str
    title: str
    notes: Optional[str]
    status: ReminderStatus
    due_at: datetime
    completed_at: datetime
    links: List[str]
    created_at: datetime


@dataclass(frozen=True)
class CreateReminderAnswer:
    # pylint: disable=too-many-instance-attributes
    reminder_id: str
    title: str
    notes: Optional[str]
    status: ReminderStatus
    due_at: datetime
    completed_at: datetime
    links: List[str]
    created_at: datetime
