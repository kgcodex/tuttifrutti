<h1>
  <img src="https://raw.githubusercontent.com/kgcodex/tuttifrutti/main/logo.png" width="32" style="vertical-align: middle; border-radius: 8px;" />
  tuttifrutti
</h1>

<div align="center">
  <img src="https://raw.githubusercontent.com/kgcodex/tuttifrutti/main/banner.png" alt="preview" width="700" style="border-radius: 14px;" />
</div>

A collection of tiny, lightweight, and highly optimized Python utilities to make your everyday coding sweet and crisp. Fully typed, zero external dependencies, and built with lazy-loading for maximum performance.

<div align="center">
<a href="https://pypi.org/project/tuttifrutti/">
    <img src="https://img.shields.io/pypi/v/tuttifrutti.svg" alt="PyPI version">
</a>
<a href="https://pypi.org/project/tuttifrutti/">
    <img src="https://img.shields.io/pypi/pyversions/tuttifrutti.svg" alt="Python version">
</a>
<a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</a>
</div>

---

## Utilities

### 1. OptionalChain

Tired of guarding deeply nested dictionaries or object lookups with defensive if configurations? OptionalChain brings clean, safe JavaScript-style optional chaining (?.) directly to Python.

```py
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

ans: int | None = app_response.data.courses[0].price.map(lambda x: x // 12).get()
print(ans)  # Output: 166


def append_at_sign(username: str) -> str:
    return f"{'@'}{username}"


result = app_response.data.username.map(append_at_sign).get()
print(result)  # Output: None

```

More tiny utilities are actively cooking and coming soon!

## 📦 Features

- **⚡ Ultra Lightweight & Lazy-Loaded:** Submodules are only loaded into memory when explicitly called—keeping your application startup lightning fast.
- **🛡️ Fully Type-Safe:** Ships with explicit PEP 561 typing configurations (`py.typed`) to ensure strict compatibility with tools like `mypy` and modern IDE autocomplete structures.
- **🪶 Zero Dependencies:** Pure, clean standard-library enhancements.

---

## 🚀 Installation

Install `tuttifrutti` using your favorite Python package manager:

```bash
# Using pip
pip install tuttifrutti

# Using uv
uv add tuttifrutti
```
