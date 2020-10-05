import pandas as pd
train_data = pd.read_csv("train.csv")
# cleaning
train_data.Cabin = train_data.Cabin.str[0]
train_data  = train_data.fillna("unk")
for title in ["Cabin", "Embarked", "Pclass", "Sex"]:
    print(title)
    for option in train_data[title].unique():
        try:
            amount = len(train_data.loc[train_data[title] == option]["Survived"])  # 0 ve 1
            survive = sum(train_data.loc[train_data[title] == option]["Survived"])  # 1
            print(f"{option} number: {amount} survive_rate: {survive/amount}")
        except:
            print(option)