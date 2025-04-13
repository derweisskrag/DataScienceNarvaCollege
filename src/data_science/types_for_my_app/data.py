from typing import List, TypedDict


class Stop(TypedDict):
    aeg: str
    järjekord: int
    stop_name: str

class BusInfo(TypedDict):
    number: int
    destination: str

class BusSchedule(TypedDict):
    buss: BusInfo
    peatused: List[Stop]