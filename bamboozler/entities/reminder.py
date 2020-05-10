from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class ReminderStatus(Enum):
    TODO = "TODO"
    DONE = "DONE"


@dataclass(frozen=True)
class Reminder:
    # pylint: disable=too-many-instance-attributes
    reminder_id: str
    title: str
    notes: Optional[str]
    status: ReminderStatus
    due_at: datetime
    completed_at: datetime
    links: List[str]
    created_at: datetime
