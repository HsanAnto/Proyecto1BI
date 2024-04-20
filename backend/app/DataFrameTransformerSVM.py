from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd

class DataFrameTransformerSVM(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X['datos'] = X['words'].apply(lambda x: ' '.join(x))
        X_data, y_data = X['datos'], X['Class']
        y_data = pd.get_dummies(y_data)

        tf_idf = TfidfVectorizer()
        X_tf_idf = tf_idf.fit_transform(X_data)
        X_tf_nv = X_tf_idf.todense()

        y_data_1d = y_data.idxmax(axis=1)
        X_train, X_test, Y_train, Y_test = train_test_split(X_tf_idf, y_data_1d, test_size=0.2, random_state=0, stratify=y_data_1d)

        return X_train, X_test, Y_train, Y_test