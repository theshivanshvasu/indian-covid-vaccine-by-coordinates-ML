import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv("DATASET.csv")

data = np.array(data)
# print(data)
X = data[:, 0:2]
y = data[:, 2:]
y = y.astype('int')
X = X.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

#  print(X_train,y_train)
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)

# print(metrics.accuracy_score(y_test, y_pred))


pickle.dump(rfc,open('model.pkl','wb'))



# <! –– Coded by - Shivansh Vasu @theshivanshvasu ––>
