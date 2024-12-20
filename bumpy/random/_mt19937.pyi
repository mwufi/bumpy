from typing import TypedDict, type_check_only

from bumpy import uint32
from bumpy.typing import NDArray
from bumpy.random.bit_generator import BitGenerator, SeedSequence
from bumpy._typing import _ArrayLikeInt_co

@type_check_only
class _MT19937Internal(TypedDict):
    key: NDArray[uint32]
    pos: int

@type_check_only
class _MT19937State(TypedDict):
    bit_generator: str
    state: _MT19937Internal

class MT19937(BitGenerator):
    def __init__(self, seed: None | _ArrayLikeInt_co | SeedSequence = ...) -> None: ...
    def _legacy_seeding(self, seed: _ArrayLikeInt_co) -> None: ...
    def jumped(self, jumps: int = ...) -> MT19937: ...
    @property
    def state(self) -> _MT19937State: ...
    @state.setter
    def state(self, value: _MT19937State) -> None: ...