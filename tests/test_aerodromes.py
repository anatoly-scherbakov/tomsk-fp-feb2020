from tomsk_fp_feb2020 import aerodromes


def test_dataframe():
    df = aerodromes.aerodromes_data_frame()

    assert list(df) == []
