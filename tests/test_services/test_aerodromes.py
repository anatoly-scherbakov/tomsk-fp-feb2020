from tomsk_fp_feb2020 import aerodromes


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
