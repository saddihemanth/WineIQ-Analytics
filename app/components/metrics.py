import streamlit as st


class MetricsCard:

    @staticmethod
    def render(
        dataset_size,
        features,
        accuracy,
        model_name
    ):

        c1, c2, c3, c4 = st.columns([1,1,3,1])

        c1.metric(
            "Dataset Size",
            dataset_size
        )

        c2.metric(
            "Features",
            features
        )

        c3.metric(
            "Best Model",
            model_name
        )

        c4.metric(
            "Accuracy",
            f"{accuracy:.2%}"
        )
