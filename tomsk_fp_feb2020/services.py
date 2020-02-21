from typing import NewType

from tomsk_fp_feb2020 import models
import geopy.distance


Kilometers = NewType('Kilometers', float)


def location_to_point(location: models.Location) -> geopy.Point:
    """Convert our internal data structure to Geopy point."""
    return geopy.Point(
        latitude=location.latitude,
        longitude=location.longitude,
    )


def measure_distance(
    origin: models.Location,
    destination: models.Location,
) -> Kilometers:
    """Calculate distance between geographical points, in kilometers."""
    return Kilometers(geopy.distance.distance(
        location_to_point(origin),
        location_to_point(destination)
    ).kilometers)
