import pandas as pd


def get_login_data():

    data = pd.read_csv("testdata/login_data.csv")

    return data.values.tolist()