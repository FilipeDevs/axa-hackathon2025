import pandas as pd



def evaluate_fire_risk():
    data = pd.read_csv('./BXBRUSSL.txt', header = None)
    print(data)