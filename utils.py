import pandas as pd
def load_nestle_data(csv_path):
    return pd.read_csv(csv_path, sep=";", parse_dates=["date"], decimal = ",")