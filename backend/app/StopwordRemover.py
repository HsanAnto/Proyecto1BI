from sklearn.base import BaseEstimator, TransformerMixin

class StopwordRemover(BaseEstimator, TransformerMixin):
    def __init__(self, stopwords_list):
        self.stopwords_list = stopwords_list
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X['words'] = X['words'].apply(self._remove_stopwords)
        return X
    
    def _remove_stopwords(self, words):
        return [w for w in words if w not in self.stopwords_list]