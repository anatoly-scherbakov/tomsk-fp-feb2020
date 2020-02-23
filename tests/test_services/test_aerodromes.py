from tomsk_fp_feb2020 import aerodromes, models


def test_dataframe():
    df = aerodromes.aerodromes_data_frame()

    assert list(df) == [
        'id',
        'ident',
        'type',
        'name',
        'latitude_deg',
        'longitude_deg',
        'elevation_ft',
        'continent',
        'iso_country',
        'iso_region',
        'municipality',
        'scheduled_service',
        'gps_code',
        'iata_code',
        'local_code',
        'home_link',
        'wikipedia_link',
        'keywords',
    ]


def test_get_aerodrome_by_iata_code():
    aerodrome = aerodromes.get_aerodrome_by_iata_code('BAX')
    assert aerodrome.name == 'Barnaul Airport'
    assert aerodrome.code == 'BAX'
    assert aerodrome.location == models.Location(
        latitude=53.36380004882813,
        longitude=83.53849792480469
    )
    assert aerodrome.is_active is True
