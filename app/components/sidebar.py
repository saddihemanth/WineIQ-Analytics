import streamlit as st


class Sidebar:

    @staticmethod
    def render():

        st.sidebar.markdown(
            """
            <div style='text-align:center'>
                <h1>🍷</h1>
                <h2>WineIQ Analytics</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.sidebar.markdown("---")

        page = st.sidebar.radio(
            "Navigation",
            [
                "Dashboard",
                "Prediction",
                "History",
                "Analytics",
                "Model Insights",
                "Explainability",
                "About"
            ],
            key="main_navigation"
        )

        st.sidebar.markdown("---")

        st.sidebar.info(
            """
            Version 1.0

            AI-Powered Wine Intelligence Platform
            """
        )

        return page
