import dataclasses
import datetime
from enum import Enum
from typing import Set


@dataclasses.dataclass(frozen=True)
class Location:
    """Geographical location."""

    latitude: float
    longitude: float


class RunwayMaterial(str, Enum):
    """Composition of runway surface."""

    ASPHALT = 'asphalt'
    CONCRETE = 'concrete'
    GRASS = 'grass'
    ICE = 'ice'
    WATER = 'water'


@dataclasses.dataclass(frozen=True)
class Runway:
    """Surface for landing and takeoff."""

    material: RunwayMaterial

    length: int
    """Runway length, in meters"""


@dataclasses.dataclass(frozen=True)
class Aerodrome:
    """Aerodrome is a place where a plane can land and take off."""

    name: str
    location: Location
    runways: Set[Runway]
    is_active: bool


@dataclasses.dataclass(frozen=True)
class Vehicle:
    """Plane we fly on."""

    name: str

    minimum_runway_length: int
    """In meters."""

    allowed_runway_materials: Set[RunwayMaterial]


@dataclasses.dataclass(frozen=True)
class Flight:
    """A direct route from one point to another."""

    origin: Aerodrome
    destination: Aerodrome

    distance: float

    departure_time: datetime.datetime
