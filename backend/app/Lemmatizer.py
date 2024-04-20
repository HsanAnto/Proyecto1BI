from sklearn.base import BaseEstimator, TransformerMixin

class Lemmatizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X['words'] = X['words'].apply(self._lemmatize)
        return X
    
    def _lemmatize(self, words):
        return words