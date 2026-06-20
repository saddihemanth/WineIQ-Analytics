
"""
WineIQ Analytics — Chart Builder

Centralised Plotly figure factory so every chart in the app shares
the same "Cellar at Midnight" theme: transparent backgrounds (so the
glass-card CSS shows through), Inter typography, and a bordeaux→gold
color scale.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Brand palette
WINE_GOLD_SCALE = ["#220c18", "#5c1a33", "#82213f", "#a6294c", "#c9a227", "#e2c25f"]
GOLD = "#e2c25f"
WINE = "#a6294c"
CREAM = "#f8efe0"
MUTED = "#ab93a0"

BASE_LAYOUT = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color=CREAM, size=13),
    title_font=dict(family="Playfair Display, serif", color=CREAM, size=18),
    margin=dict(l=10, r=10, t=55, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)"),
    hoverlabel=dict(bgcolor="#220c18", font_color=CREAM, bordercolor=GOLD),
)


def _style(fig):
    fig.update_layout(**BASE_LAYOUT)
    fig.update_xaxes(gridcolor="rgba(248,239,224,0.08)", zerolinecolor="rgba(248,239,224,0.08)")
    fig.update_yaxes(gridcolor="rgba(248,239,224,0.08)", zerolinecolor="rgba(248,239,224,0.08)")
    return fig


class ChartBuilder:

    @staticmethod
    def quality_distribution(df):
        fig = px.histogram(
            df,
            x="quality",
            color_discrete_sequence=[WINE],
            title="Wine Quality Distribution",
        )
        fig.update_traces(marker_line_color=GOLD, marker_line_width=1, opacity=0.9)
        return _style(fig)

    @staticmethod
    def alcohol_vs_quality(df):
        """Scatter of alcohol content vs. quality, colored by quality score."""
        fig = px.strip(
            df,
            x="quality",
            y="alcohol",
            color="quality",
            color_continuous_scale=WINE_GOLD_SCALE,
            title="Alcohol Content by Quality Score",
        )
        fig.update_traces(marker=dict(size=6, opacity=0.65, line=dict(width=0)))
        fig.update_layout(showlegend=False, coloraxis_showscale=False)
        return _style(fig)

    @staticmethod
    def correlation_heatmap(df):
        corr = df.corr(numeric_only=True)
        fig = px.imshow(
            corr,
            text_auto=".2f",
            aspect="auto",
            color_continuous_scale=WINE_GOLD_SCALE,
            title="Correlation Heatmap",
        )
        return _style(fig)

    @staticmethod
    def feature_importance(model, features):
        importance = model.feature_importances_

        feature_df = pd.DataFrame({"Feature": features, "Importance": importance})
        feature_df = feature_df.sort_values(by="Importance", ascending=True)

        fig = px.bar(
            feature_df,
            x="Importance",
            y="Feature",
            orientation="h",
            color="Importance",
            color_continuous_scale=WINE_GOLD_SCALE,
            title="Feature Importance",
        )
        fig.update_layout(coloraxis_showscale=False)
        return _style(fig)

    @staticmethod
    def model_comparison():
        names = ["Logistic Regression", "KNN", "Decision Tree", "Random Forest"]
        scores = [0.865, 0.881, 0.872, 0.903]

        fig = go.Figure(
            go.Bar(
                x=names,
                y=scores,
                marker=dict(
                    color=scores,
                    colorscale=WINE_GOLD_SCALE,
                    line=dict(color=GOLD, width=1),
                ),
                text=[f"{s:.1%}" for s in scores],
                textposition="outside",
                textfont=dict(color=CREAM),
            )
        )
        fig.update_layout(title="Model Comparison — Accuracy", yaxis_tickformat=".0%")
        return _style(fig)