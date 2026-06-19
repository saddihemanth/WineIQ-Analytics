import pandas as pd
from datetime import datetime

def save_prediction(prediction, alcohol, sulphates):

    df = pd.DataFrame([{
        "Timestamp": datetime.now(),
        "Prediction": prediction,
        "Alcohol": alcohol,
        "Sulphates": sulphates
    }])

    df.to_csv(
        "data/predictions.csv",
        mode="a",
        header=False,
        index=False
    )