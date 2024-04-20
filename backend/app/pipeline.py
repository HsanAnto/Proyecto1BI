import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
import Tokenizer
import NoiseRemover
import Lemmatizer
import StopwordRemover
import DataFrameTransformerSVM

# Definición de stopwords
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


# Definición del pipeline
pipeline = Pipeline([
    ('tokenizer', Tokenizer()),
    ('noise_remover', NoiseRemover()),
    ('lemmatizer', Lemmatizer()),
    ('stopwords_remover', StopwordRemover(stopwords_list=default_stopwords)),
    ('dataframe_transformerSVM', DataFrameTransformerSVM())])

