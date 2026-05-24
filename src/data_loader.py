import pandas as pd


def load_data(file_path):
    """
    Load a CSV file containing comments.
    """
    df = pd.read_csv(file_path)

    return df