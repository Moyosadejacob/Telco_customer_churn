import pandas as pd

def call_data(file_path):

    df=pd.read_csv(file_path)

    return df