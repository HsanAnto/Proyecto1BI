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


class Review:
    def __init__(self, review_id, text):
        self.id = review_id
        self.text = text

    def to_dict(self):
        return {"id": self.id, "text": self.text}

app = FastAPI()

# Variable global para almacenar el DataFrame
df = None
reviews = []

@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    global df
    if file.content_type != "text/csv":
        return JSONResponse(status_code=400, content={"error": "El archivo debe ser de tipo CSV"})

    try:
        df = pd.read_csv(file.file)
        
        file.file.close()


        # Fit the pipeline
        train, test = train_test_split(df, test_size=0.2, random_state=9)


        #estos es los resultados del modelo
        x_test = test.drop(['Class'],axis=1)
        y_test = test['Class']

        model = load("assets/modelo.joblib")
        
        y_pred = model.predict(x_test)

        print(classification_report(y_test, y_pred))

        for index, row in df.iterrows():
            review = Review(review_id=index+1, text=row["Review"])
            reviews.append(review.to_dict())
        return {"filename": file.filename, "reviews": reviews}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
