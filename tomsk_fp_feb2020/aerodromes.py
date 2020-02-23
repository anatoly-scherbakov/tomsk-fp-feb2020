import logging
import os
import pathlib
from typing import Optional, TypedDict

import pandas as pd
import requests

from tomsk_fp_feb2020 import models

logger = logging.getLogger(__name__)


REMOTE_URL = 'http://ourairports.com/data/airports.csv'
LOCAL_PATH = pathlib.Path(__file__).parent.parent.joinpath(
    'data/aerodromes.csv'
)


class AerodromeRow(TypedDict):
    id: str
    ident: str
    type: str
    name: str
    latitude_deg: float
    longitude_deg: float
    elevation_ft: float
    continent: str
    iso_country: str
    iso_region: str
    municipality: str
    scheduled_service: str
    gps_code: str
    iata_code: str
    local_code: str
    home_link: str
    wikipedia_link: str
    keywords: str


def download_aerodromes_database() -> None:
    """Download the Airports CSV file to local data/ directory."""
    os.makedirs(LOCAL_PATH.parent, exist_ok=True)

    response = requests.get(REMOTE_URL, stream=True)

    with open(LOCAL_PATH, 'wb+') as output:
        for chunk in response.iter_content(chunk_size=1024):
            output.write(chunk)


def aerodromes_data_frame() -> pd.DataFrame:
    try:
        logger.info('Downloading aerodromes database from OurAirports...')
        return pd.read_csv(LOCAL_PATH)

    except FileNotFoundError:
        download_aerodromes_database()

        return aerodromes_data_frame()


def get_aerodrome_by_iata_code(code: str) -> Optional[models.Aerodrome]:
    """Find aerodrome by given code"""

    df = aerodromes_data_frame()
    df = df[
        df['iata_code'] == code
    ]

    rows = df.to_dict('records')

    if not rows:
        return None

    elif len(rows) > 1:
        raise ValueError('The code is ambiguous.')

    else:
        row: AerodromeRow
        (row, ) = rows

        location = models.Location(
            longitude=row['longitude_deg'],
            latitude=row['latitude_deg'],
        )

        return models.Aerodrome(
            name=row['name'],
            code=models.IATACode(row['iata_code']),
            location=location,
            is_active=True,
        )
