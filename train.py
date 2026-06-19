"""
WineIQ Analytics
Model Training Pipeline

Author: Hemanth Reddy
"""

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


# ==========================================================
# CONFIGURATION
# ==========================================================

DATA_PATH = "data/winequality.csv"

MODEL_DIR = "models"

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "model.pkl"
)

SCALER_PATH = os.path.join(
    MODEL_DIR,
    "scaler.pkl"
)


# ==========================================================
# TRAINING CLASS
# ==========================================================

class WineModelTrainer:

    def __init__(self):

        self.df = None

        self.scaler = StandardScaler()

        self.best_model = None

        self.best_accuracy = 0

        self.best_model_name = ""


    # ------------------------------------------------------
    # LOAD DATA
    # ------------------------------------------------------

    def load_data(self):

        print("Loading dataset...")

        self.df = pd.read_csv(DATA_PATH)

        print(
            f"Dataset Loaded: {self.df.shape}"
        )


    # ------------------------------------------------------
    # PREPROCESS
    # ------------------------------------------------------

    def preprocess(self):

        print("Preprocessing...")

        self.df["quality_label"] = (
            self.df["quality"]
            .apply(lambda x: 1 if x >= 7 else 0)
        )

        X = self.df.drop(
            ["quality", "quality_label"],
            axis=1
        )

        y = self.df["quality_label"]

        return X, y


    # ------------------------------------------------------
    # TRAIN MODELS
    # ------------------------------------------------------

    def train_models(self, X, y):

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )
        )

        X_train_scaled = (
            self.scaler.fit_transform(
                X_train
            )
        )

        X_test_scaled = (
            self.scaler.transform(
                X_test
            )
        )

        models = {

            "Logistic Regression":
                LogisticRegression(
                    max_iter=1000
                ),

            "KNN":
                KNeighborsClassifier(),

            "Decision Tree":
                DecisionTreeClassifier(
                    random_state=42
                ),

            "Random Forest":
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=42
                )
        }

        print("\nModel Comparison")
        print("-" * 40)

        for name, model in models.items():

            model.fit(
                X_train_scaled,
                y_train
            )

            preds = model.predict(
                X_test_scaled
            )

            accuracy = accuracy_score(
                y_test,
                preds
            )

            print(
                f"{name}: {accuracy:.4f}"
            )

            if accuracy > self.best_accuracy:

                self.best_accuracy = accuracy

                self.best_model = model

                self.best_model_name = name

        print("\nBest Model:")
        print(
            self.best_model_name
        )

        print(
            f"Accuracy: {self.best_accuracy:.4f}"
        )


    # ------------------------------------------------------
    # SAVE ARTIFACTS
    # ------------------------------------------------------

    def save_artifacts(self):

        os.makedirs(
            MODEL_DIR,
            exist_ok=True
        )

        joblib.dump(
            self.best_model,
            MODEL_PATH
        )

        joblib.dump(
            self.scaler,
            SCALER_PATH
        )

        print(
            "\nModel Saved Successfully"
        )

        print(MODEL_PATH)

        print(SCALER_PATH)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    trainer = WineModelTrainer()

    trainer.load_data()

    X, y = trainer.preprocess()

    trainer.train_models(
        X,
        y
    )

    trainer.save_artifacts()
