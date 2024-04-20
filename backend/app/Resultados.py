import pipeline
import pandas as pd

# Load the data
df = pd.read_csv('/content/tipo2_entrenamiento_estudiantes.csv')

# Fit the pipeline
X_train, X_test, Y_train, Y_test = pipeline.fit_transform(df)
