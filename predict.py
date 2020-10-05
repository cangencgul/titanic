import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# cleaning
train_data.Cabin = train_data.Cabin.str[0]
train_data = train_data[~((train_data.Cabin == "T") | (train_data.Embarked.isna()))]
train_data["FamilySize"] = train_data.SibSp + train_data.Parch
train_data.FamilySize = train_data.FamilySize.apply(lambda s: "alone" if s == 0 else("couple" if s == 1 else("small" if s <= 3 else "crowded")))
train_data.Age = train_data.Age.apply(lambda age: "young" if age < 18 else("elder" if age > 55 else("middle" if 18<=age<=55 else "unk")))
train_data = train_data.fillna("unk")

test_data.Cabin = test_data.Cabin.str[0]
test_data["FamilySize"] = test_data.SibSp + test_data.Parch
test_data.FamilySize = test_data.FamilySize.apply(lambda s: "alone" if s == 0 else("couple" if s == 1 else("small" if s <= 3 else "crowded")))
test_data.Age = test_data.Age.apply(lambda age: "young" if age < 18 else("elder" if age > 55 else("middle" if 18<=age<=55 else "unk")))
test_data = test_data.fillna("unk")

titles = ["Sex", "Pclass", "Cabin", "Embarked", "FamilySize", "Age"]
X = pd.get_dummies(train_data[titles])
X_test = pd.get_dummies(test_data[titles])
y = train_data["Survived"]

model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('lasttoday.csv', index=False)
print("Your submission was successfully saved!")