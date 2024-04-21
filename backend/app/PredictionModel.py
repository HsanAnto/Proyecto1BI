from joblib import load

import pandas as pd
from sklearn.metrics import classification_report
import numpy as np
import string
import unicodedata
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Define stopwords list
DETERMINANTES = [
    "el", "la", "los", "las", "un", "una", "unos", "unas", "esta", "estas",
    "este", "estos", "esa", "esas", "ese", "esos", "aquel", "aquella", "aquellas",
    "aquellos", "mi", "tu", "su", "mis", "tus", "sus", "nuestro", "nuestra",
    "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras", "su",
    "sus", "cuyo", "cuya", "cuyos", "cuyas", "cuánto", "cuántos", "cuánta", "cuántas",
    "qué", "tan", "menos", "más", "algún", "alguna", "algunos", "algunas", "ningún",
    "ninguna", "ningunos", "ningunas",
]

PREPOSICIONES = [
    "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en",
    "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so",
    "sobre", "tras", "versus", "vía",
]

PRONOMBRES = [
    "yo", "tú", "vos", "vo", "él", "ella", "ello", "elle", "usted", "nosotros",
    "nosotras", "nosotres", "vosotros", "vosotras", "vosotres", "ellos", "ellas",
    "ustedes", "elles", "mí", "ti", "sí", "consigo",
]

CONJUNCIONES = [
    "y", "ni", "sino", "tanto", "como", "que", "pero", "mas", "empero", "mientras",
    "o", "bien", "ya",
]

default_stopwords = list(set(DETERMINANTES + PREPOSICIONES + PRONOMBRES + CONJUNCIONES))

# Define custom transformers
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

class Lemmatizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['words'] = X['words'].apply(self._lemmatize)
        return X

    def _lemmatize(self, words):
        # Implement your lemmatization logic here
        # For example, you could use NLTK's WordNetLemmatizer
        return words

class StopwordsRemover(BaseEstimator, TransformerMixin):
    def __init__(self, stopwords_list):
        self.stopwords_list = stopwords_list

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['words'] = X['words'].apply(self._remove_stopwords)
        return X

    def _remove_stopwords(self, words):
        return [w for w in words if w not in self.stopwords_list]

class DataFrameTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.tf_idf = TfidfVectorizer()

    def fit(self, X, y=None):
        # Fit TF-IDF vectorizer on training data
        self.tf_idf.fit(X['Review'])
        return self

    def transform(self, X):
        X_tf_idf = self.tf_idf.transform(X['Review'])
        return X_tf_idf

class Model:

    def __init__(self):
        self.model = load('./backend/assets/pipeline_definitivo.pkl')

    def make_predictions(self, data):
        result = self.model.predict(data)
        data['Class'] = result
        json_data = data.to_json(orient='records', force_ascii=False, indent=4)
        return json_data

    def make_single_prediction(self, txt):
        txt_df = pd.DataFrame({"Review": [txt]})
        result = self.model.predict(txt_df[["Review"]]).tolist()[0]
        return result
