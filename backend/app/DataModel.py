from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    review: str

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["Review"]

    #Esta función retorna un diccionario con los valores del modelo.
    def to_dict(self):
        return {
            "Review": self.review
        }
