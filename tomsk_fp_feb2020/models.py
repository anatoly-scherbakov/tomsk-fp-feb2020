import dataclasses
import datetime
from enum import Enum
from typing import Set, NewType


# ICAO code of an aerodrome
IATACode = NewType('IATACode', str)

Meters = NewType('Meters', float)
Kilometers = NewType('Kilometers', float)


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

    name: str
    material: RunwayMaterial
    length: Meters


@dataclasses.dataclass(frozen=True)
class Aerodrome:
    """Aerodrome is a place where a plane can land and take off."""

    name: str
    code: IATACode
    location: Location
    runways: Set[Runway]
    is_active: bool


@dataclasses.dataclass(frozen=True)
class Vehicle:
    """Plane we fly on."""

    name: str

    minimum_runway_length: Meters

    max_flight_distance: Kilometers

    allowed_runway_materials: Set[RunwayMaterial]


@dataclasses.dataclass(frozen=True)
class Flight:
    """A direct route from one point to another."""

    origin: Aerodrome
    destination: Aerodrome

    distance: Kilometers

    vehicle: Vehicle

    departure_time: datetime.datetime
