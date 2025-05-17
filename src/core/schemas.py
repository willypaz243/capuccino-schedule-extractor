"""
This module defines various data structures using TypedDict for representing
different educational entities such as Days of the week, Schedules, Groups,
Subjects, Levels, and Careers. It also uses the Enum class to define constants
for days of the week. These structures are intended to model the organization
of academic schedules, subjects, and career paths in an educational institution.
"""

from datetime import datetime
from enum import Enum
from typing import List

from typing_extensions import TypedDict


class Day(Enum):
    JU = "JU"
    LU = "LU"
    MA = "MA"
    MI = "MI"
    SA = "SA"
    VI = "VI"


class Schedule(TypedDict):
    day: Day
    start: int
    end: int
    duration: int
    room: str
    teacher: str
    is_class: bool


class Group(TypedDict):
    code: str
    schedule: List[Schedule]
    teacher: str


class Subject(TypedDict):
    code: int
    name: str
    groups: List[Group]


class Level(TypedDict):
    code: str
    subjects: List[Subject]


class Career(TypedDict):
    made_in: str | None
    semester: str | None
    support: str | None
    code: int | None
    name: str | None
    url: str | None
    updatet_at: datetime | None
    levels: List[Level] | None


__all__ = ["Day", "Schedule", "Group", "Subject", "Level", "Career"]
