from dataclasses import dataclass


@dataclass
class Contiguity:
    state1no: int
    nome1: str
    state2no: int
    nome2: str

@dataclass
class Country:
    StateAbb:str
    CCode:int
    StateNme:str