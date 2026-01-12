from typing import TypedDict, Optional

class PatientState(TypedDict):
    name: Optional[str]
    age: Optional[int]
    query: Optional[str]
    ward: Optional[str]
    message: Optional[str]

class PatientState(TypedDict):
    name: str | None
    age: int | None
    query: str | None
    ward: str | None
    completed: bool | None
