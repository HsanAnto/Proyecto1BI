from app.DataModel import DataModel
from fastapi import FastAPI, File, UploadFile, Body, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel


from app.PredictionModel import Model


import pandas as pd

import json

app = FastAPI()

# Variable global para almacenar el DataFrame
df = None
reviews = []
model = Model()
reviews_classified = []

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

        return {"filename": file.filename, "reviews": reviews}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/predict/")
def make_predictions():
    if df is None:
        return JSONResponse(status_code=400, content={"error": "Primero debe cargar el archivo de reviews"})

    reviews_classified = model.make_predictions(df)
    return reviews_classified

@app.post("/predict/single/")
async def make_prediction(review: Request):
    try:
        body = await review.body()
        data = json.loads(body.decode("utf-8"))
        review_text = data.get("review", "")
        stars = model.make_single_prediction(review_text)
        return stars
    except Exception as e:
        return {"error": str(e)}

