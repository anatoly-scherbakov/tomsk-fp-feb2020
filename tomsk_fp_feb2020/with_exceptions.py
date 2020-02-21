from tomsk_fp_feb2020 import models


def validate_distance(flight: models.Flight) -> models.Flight:
    """Make sure the vehicle can cover the required distance."""
    max_flight_distance = flight.vehicle.max_flight_distance
    if flight.distance > max_flight_distance:
        raise ValueError(
            f'Flight distance {flight.distance} km is greater than max '
            f'distance {max_flight_distance} allowed for the vehicle '
            f'{flight.vehicle.name}.'
        )

    return flight


def validate_runways_material(flight: models.Flight) -> models.Flight:
    """Make sure vehicle can use the runways, based on their material."""
    return flight


def validate_runways_length(flight: models.Flight) -> models.Flight:
    """Make sure vehicle can use the runways, based on their length."""
    return flight


def validate_aerodromes_active(flight: models.Flight) -> models.Flight:
    """Make sure vehicle can use the aerodromes, based on their availability."""
    return flight
