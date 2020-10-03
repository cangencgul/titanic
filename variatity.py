import pandas as pd
train_data = pd.read_csv("train.csv")
for title in  train_data.columns:
    quantity = len(train_data[title].unique())
    print(title, quantity)