from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import unicodedata
class NoiseRemover(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.stop_words = set(stopwords.words('spanish'))
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X['words'] = X['words'].apply(self._remove_noise)
        return X
    
    def _remove_noise(self, words):
        words = [self._remove_non_ascii(w) for w in words]
        words = [w.lower() for w in words]
        words = [w for w in words if w not in string.punctuation]
        words = [w for w in words if w not in self.stop_words]
        words = [w for w in words if not w.isdigit()]
        return words
    
    def _remove_non_ascii(self, word):
        return unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')