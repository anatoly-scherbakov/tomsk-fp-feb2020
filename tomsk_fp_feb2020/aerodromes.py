import pathlib

import pandas as pd
import requests


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


def aerodromes_data_frame():
    return pd.read_csv(LOCAL_PATH)
