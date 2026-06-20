"""
WineIQ Analytics — Prediction History

Persists each prediction to data/predictions.csv. Uses a path
anchored to this file's location (not the process's current working
directory) so it works the same whether launched as
`streamlit run app/app.py` from the repo root or from inside app/.
"""

import os
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_PATH = os.path.join(BASE_DIR, "..", "..", "data", "predictions.csv")

COLUMNS = ["Timestamp", "Prediction", "Alcohol", "Sulphates"]


def save_prediction(prediction, alcohol, sulphates):

    row = pd.DataFrame(
        [
            {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Prediction": int(prediction),
                "Alcohol": alcohol,
                "Sulphates": sulphates,
            }
        ]
    )

    file_exists = os.path.isfile(HISTORY_PATH) and os.path.getsize(HISTORY_PATH) > 0

    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)

    row.to_csv(
        HISTORY_PATH,
        mode="a",
        header=not file_exists,
        index=False,
    )


def load_history():
    """Returns the prediction history as a DataFrame, or an empty one."""

    if not os.path.isfile(HISTORY_PATH) or os.path.getsize(HISTORY_PATH) == 0:
        return pd.DataFrame(columns=COLUMNS)

    return pd.read_csv(HISTORY_PATH)