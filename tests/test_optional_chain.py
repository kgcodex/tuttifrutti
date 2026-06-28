from dataclasses import dataclass
from datetime import date
from typing import Any, Literal

from tuttifrutti import OptionalChain


@dataclass
class Course:
    name: str
    level: Literal["Basic", "Intermediate", "Advance"]
    price: int | None


@dataclass
class AppUser:
    name: str | None
    username: str | None
    age: int | None
    courses: list[Course] | None
    meta: dict[str, Any]


@dataclass
class AppResponse:
    data: OptionalChain[AppUser]
    status: int


course1 = Course(name="Python", level="Basic", price=2000)
course2 = Course(name="JS/TS", level="Intermediate", price=3400)
course3 = Course(name="Go", level="Advance", price=None)

app_user = AppUser(
    name="Kunal",
    username=None,
    age=10,
    courses=[course1, course2, course3],
    meta={
        "purchase_day": str(date.today()),
        "coupon": True,
    },
)
app_response = AppResponse(
    data=OptionalChain(app_user),
    status=200,
)


def test_optional_chain_success() -> None:
    ans = app_response.data.courses[0].name.get()
    assert ans == "Python"
