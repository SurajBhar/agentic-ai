from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("langgraph-mini")
except PackageNotFoundError:  # running from source without installed metadata
    __version__ = "0.0.0"

__all__ = ["__version__"]
