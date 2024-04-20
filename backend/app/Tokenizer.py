from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import word_tokenize


class Tokenizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X['words'] = X['Review'].apply(self._tokenize_text)
        return X
    
    def _tokenize_text(self, text):
        return word_tokenize(text)