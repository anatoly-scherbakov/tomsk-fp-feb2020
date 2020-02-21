import pathlib

import pandas as pd
import requests

import logging

logger = logging.getLogger(__name__)


REMOTE_URL = 'http://ourairports.com/data/airports.csv'
LOCAL_PATH = pathlib.Path(__file__).parent.parent.joinpath(
    'data/aerodromes.csv'
)


def download_aerodromes_database():
    """Download the Airports CSV file to local data/ directory."""
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
