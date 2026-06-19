import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class ChartBuilder:

    @staticmethod
    def quality_distribution(df):

        fig = px.histogram(
            df,
            x="quality",
            title="Wine Quality Distribution",
            template="plotly_dark"
        )

        return fig

    @staticmethod
    def correlation_heatmap(df):

        corr = df.corr(
            numeric_only=True
        )

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Correlation Heatmap"
        )

        return fig

    @staticmethod
    def feature_importance(
        model,
        features
    ):

        importance = (
            model.feature_importances_
        )

        feature_df = pd.DataFrame(
            {
                "Feature": features,
                "Importance": importance
            }
        )

        feature_df = (
            feature_df
            .sort_values(
                by="Importance",
                ascending=False
            )
        )

        fig = px.bar(
            feature_df,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Feature Importance"
        )

        return fig

    @staticmethod
    def model_comparison():

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=[
                    "Logistic",
                    "KNN",
                    "Decision Tree",
                    "Random Forest"
                ],
                y=[
                    0.865,
                    0.881,
                    0.872,
                    0.903
                ]
            )
        )

        fig.update_layout(
            title="Model Comparison"
        )

        return fig