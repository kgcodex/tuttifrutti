from __future__ import annotations

from collections.abc import Callable
from typing import Any


class OptionalChain[T]:
    def __init__(self, obj: T | None) -> None:
        self._obj = obj

    def __repr__(self) -> str:
        return (
            f"OptionalChain("
            f"{self._obj.__class__.__name__ if self._obj is not None else None}"
            f")"
        )

    def __getattr__(self, attr: str) -> OptionalChain[Any]:
        if self._obj is None:
            return OptionalChain(None)

        if isinstance(self._obj, dict):
            return OptionalChain(self._obj.get(attr, None))

        return OptionalChain(getattr(self._obj, attr, None))

    def get(self) -> T | None:
        return self._obj

    def __getitem__(self, key: Any) -> OptionalChain[Any]:
        if self._obj is None:
            return OptionalChain(None)
        try:
            return OptionalChain(self._obj[key])  # type:ignore[index]
        except (KeyError, IndexError, TypeError):
            return OptionalChain(None)

    def or_else[K](self, default: K) -> T | K:
        return self._obj if self._obj is not None else default

    def map[R](self, func: Callable[[T], R]) -> OptionalChain[R]:
        if self._obj is None:
            return OptionalChain(None)
        return OptionalChain(func(self._obj))
