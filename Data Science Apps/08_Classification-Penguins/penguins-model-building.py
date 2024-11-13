import pandas   as pd
penguins = pd.read_csv('penguins_cleaned.csv')

# Drop rows with any missing values
df = penguins.copy()
target = 'species'
encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

target_map = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_map[val]

df['species'] = df['species'].apply(target_encode)

# Separating x and y
X = df.drop('species', axis=1)
Y = df['species']

# Building the model
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X, Y)

# Saving the model
import pickle
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))