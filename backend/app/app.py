from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd

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
        for index, row in df.iterrows():
            review = Review(review_id=index+1, text=row["Review"])
            reviews.append(review.to_dict())
        return {"filename": file.filename, "reviews": reviews}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
