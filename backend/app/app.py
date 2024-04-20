from backend.app import DataModel
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
from joblib import load
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


app = FastAPI()

# Variable global para almacenar el DataFrame
df = None
reviews = []

@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        return JSONResponse(status_code=400, content={"error": "El archivo debe ser de tipo CSV"})

    try:
        df = pd.read_csv(file.file)
        
        file.file.close()

        for index, row in df.iterrows():
            review = DataModel(review=row["Review"])
            reviews.append(review.to_dict())

        return {"filename": file.filename, "reviews": reviews}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/predict")
def make_predictions():
    if df is None:
        return JSONResponse(status_code=400, content={"error": "Primero debe cargar el archivo de reviews"})
    df.columns = dataModel.columns()
    model = load("../assets/mejor_modelo.joblib")
    result = model.predict(df)
    return result
