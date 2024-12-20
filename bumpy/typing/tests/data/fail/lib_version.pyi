from bumpy.lib import BumpyVersion

version: BumpyVersion

BumpyVersion(b"1.8.0")  # E: incompatible type
version >= b"1.8.0"  # E: Unsupported operand types
