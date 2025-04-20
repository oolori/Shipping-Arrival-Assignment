import pandas as pd

# Function to pull and load data from my directory.
def load_data(data_path):
    return pd.read_csv(data_path)