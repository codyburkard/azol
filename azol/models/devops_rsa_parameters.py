from dataclasses import dataclass

@dataclass
class DevOpsRSAParameters:
    p: bytes
    q: bytes
    d: bytes
    modulus: bytes
    dp: bytes
    dq: bytes
    exponent: bytes
    inverseq: bytes
