__all__ = ["BumpyVersion"]

class BumpyVersion:
    vstring: str
    version: str
    major: int
    minor: int
    bugfix: int
    pre_release: str
    is_devversion: bool
    def __init__(self, vstring: str) -> None: ...
    def __lt__(self, other: str | BumpyVersion) -> bool: ...
    def __le__(self, other: str | BumpyVersion) -> bool: ...
    def __eq__(self, other: str | BumpyVersion) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: str | BumpyVersion) -> bool: ...  # type: ignore[override]
    def __gt__(self, other: str | BumpyVersion) -> bool: ...
    def __ge__(self, other: str | BumpyVersion) -> bool: ...
