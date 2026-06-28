from importlib import import_module
from importlib.metadata import version
from typing import TYPE_CHECKING, Any

__version__ = version("tuttifrutti")

if TYPE_CHECKING:
    from .optional_chain import OptionalChain

__all__ = ["OptionalChain"]


def __getattr__(name: str) -> Any:
    if name == "OptionalChain":
        return import_module(".optional_chain", __name__).OptionalChain

    raise AttributeError(f"module '{__name__}' has not attribute {name}")
