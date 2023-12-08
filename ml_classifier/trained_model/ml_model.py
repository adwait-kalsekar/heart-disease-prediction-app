import numpy as np
import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

df = pd.read_csv("ml_classifier/trained_model/heart-disease.csv")

X = df.drop("target", axis = 1)
y = df.target

np.random.seed(111)
final_model = LogisticRegression(solver='liblinear', penalty='l2', C=0.23357214690901212)
final_model.fit(X, y)

joblib.dump(final_model, 'ml_classifier/trained_model/final_model.pkl')
joblib.dump(list(X.columns), 'ml_classifier/trained_model/col_names.pkl')