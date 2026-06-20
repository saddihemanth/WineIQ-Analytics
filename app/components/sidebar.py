"""
WineIQ Analytics — Sidebar Navigation
"""

import streamlit as st

# Icon prefix per page keeps st.sidebar.radio (no extra dependency)
# while the CSS pill-styling in styles.css turns it into a modern nav.
NAV_ITEMS = {
    "Dashboard": "📊 Dashboard",
    "Prediction": "🎯 Prediction",
    "History": "📜 History",
    "Analytics": "📈 Analytics",
    "Model Insights": "🧠 Model Insights",
    "Explainability": "🔍 Explainability",
    "About": "🚀 About",
}


class Sidebar:

    @staticmethod
    def render():

        st.sidebar.markdown(
            """
            <div class="sidebar-brand">
                <div class="crest">🍷</div>
                <h2>WineIQ Analytics</h2>
                <div class="sub">Wine Intelligence Platform</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.sidebar.markdown("---")

        selection = st.sidebar.radio(
            "Navigation",
            list(NAV_ITEMS.values()),
            key="main_navigation",
            label_visibility="collapsed",
        )

        # Map the decorated label back to the internal page key
        page = next(
            key for key, label in NAV_ITEMS.items() if label == selection
        )

        st.sidebar.markdown(
            """
            <div class="sidebar-info-card">
                <b>Version</b> 2.0 &nbsp;·&nbsp; <b>Model</b> Random Forest<br>
                AI-powered wine quality intelligence — trained on 1,599
                physicochemical wine samples.
            </div>
            """,
            unsafe_allow_html=True,
        )

        return page