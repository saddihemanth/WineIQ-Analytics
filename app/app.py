
"""
WineIQ Analytics
AI-Powered Wine Quality Intelligence Platform

Author: Hemanth Reddy
Version: 1.0
"""

# ==========================================================
# IMPORTS
# ==========================================================

import os
import joblib
import streamlit as st
import pandas as pd


from components.sidebar import Sidebar
from components.metrics import MetricsCard
from components.charts import ChartBuilder
from components.report_generator import generate_pdf
from components.history import save_prediction


# ==========================================================
# PAGE CONFIG
# ==========================================================
import streamlit as st


st.set_page_config(
    
    page_title="WineIQ Analytics",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PATH CONFIGURATION
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "winequality.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "scaler.pkl"
)

CSS_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "styles.css"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    with open(
        CSS_PATH,
        encoding="utf-8"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# ==========================================================
# CACHE DATA
# ==========================================================

@st.cache_data
def load_dataset():

    df = pd.read_csv(DATA_PATH)

    return df


# ==========================================================
# CACHE MODEL
# ==========================================================

@st.cache_resource
def load_artifacts():

    model = joblib.load(
        MODEL_PATH
    )

    scaler = joblib.load(
        SCALER_PATH
    )

    return model, scaler


# ==========================================================
# LOAD RESOURCES
# ==========================================================

df = load_dataset()

model, scaler = load_artifacts()


# ==========================================================
# HERO SECTION
# ==========================================================

def render_hero():

    st.markdown(
        """
        <div class="hero">
            <h1>🍷 WineIQ Analytics</h1>
            <p>
                AI-Powered Wine Quality Intelligence Platform
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# DASHBOARD PAGE
# ==========================================================

def dashboard_page():

    render_hero()
   

    st.markdown("---")

    MetricsCard.render(
        dataset_size=len(df),
        features=11,
        accuracy=0.903,
        model_name="Random Forest"
    )

    st.markdown("## 📊 Dataset Overview")

    col1, col2 = st.columns(
        [2, 1]
    )

    with col1:

        st.plotly_chart(
    ChartBuilder.quality_distribution(df),
    use_container_width=True,
    key="quality_distribution"
)

    with col2:

        st.markdown(
            """
            ### Project Summary

            WineIQ Analytics uses
            Machine Learning to classify
            wine quality based on
            physicochemical attributes.

            Features include:

            - Quality Prediction
            - Interactive Analytics
            - Model Insights
            - Feature Importance
            - Data Exploration
            """
        )

    st.markdown("---")

    st.markdown(
        "## 🔍 Sample Dataset"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.markdown("---")

    st.markdown(
        "## 📈 Quality Distribution"
    )

    st.plotly_chart(
    ChartBuilder.quality_distribution(df),
    use_container_width=True,
    key="quality_distribution_dashboard"
)

    st.markdown("---")

    st.markdown(
        "## 🔥 Correlation Heatmap"
    )

    st.plotly_chart(
    ChartBuilder.correlation_heatmap(df),
    use_container_width=True,
    key="correlation_heatmap_dashboard"
)


# ==========================================================
# PREDICTION PAGE
# ==========================================================

def prediction_page():

    render_hero()

    st.markdown("## 🎯 Wine Quality Prediction")

    st.write(
        "Enter wine chemical properties and let AI predict quality."
    )

    col1, col2 = st.columns(2)

    with col1:

        fixed_acidity = st.number_input(
            "Fixed Acidity",
            value=7.4
        )

        volatile_acidity = st.number_input(
            "Volatile Acidity",
            value=0.70
        )

        citric_acid = st.number_input(
            "Citric Acid",
            value=0.00
        )

        residual_sugar = st.number_input(
            "Residual Sugar",
            value=1.90
        )

        chlorides = st.number_input(
            "Chlorides",
            value=0.076
        )

        free_sulfur_dioxide = st.number_input(
            "Free Sulfur Dioxide",
            value=11.0
        )

    with col2:

        total_sulfur_dioxide = st.number_input(
            "Total Sulfur Dioxide",
            value=34.0
        )

        density = st.number_input(
            "Density",
            value=0.9978,
            format="%.4f"
        )

        pH = st.number_input(
            "pH",
            value=3.51
        )

        sulphates = st.number_input(
            "Sulphates",
            value=0.56
        )

        alcohol = st.number_input(
            "Alcohol",
            value=9.4
        )

    st.markdown("---")

    if st.button(
        "🚀 Predict Wine Quality"
    ):

        input_data = [[
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol
        ]]

        input_scaled = scaler.transform(
            input_data
        )

        prediction = model.predict(
            input_scaled
        )[0]

        save_prediction(
            prediction,
            alcohol,
            sulphates
        )

        st.markdown("---")

        if prediction == 1:

            st.success(
                """
                🍷 Premium Quality Wine

                The model predicts this wine
                belongs to the HIGH QUALITY class.
                """
            )

        else:

            st.error(
                """
                ⚠️ Standard Quality Wine

                The model predicts this wine
                belongs to the LOW QUALITY class.
                """
            )

        st.markdown("---")

        st.subheader(
            "Prediction Summary"
        )

        summary_df = pd.DataFrame(
            {
                "Feature": [
                    "Alcohol",
                    "Sulphates",
                    "pH",
                    "Density"
                ],
                "Value": [
                    alcohol,
                    sulphates,
                    pH,
                    density
                ]
            }
        )

        st.dataframe(
            summary_df,
            use_container_width=True
        )
        from app.components.report_generator import generate_pdf

        if st.button("Generate PDF Report"):
         pdf_file = generate_pdf(prediction)

         with open(pdf_file, "rb") as file:
            st.download_button("Download Report",file,
        file_name="wine_report.pdf"
        )
def history_page():
    st.title("📜 Prediction History")

    try:
        history = pd.read_csv("data/predictions.csv")

        st.metric(
            "Total Predictions",
            len(history)
        )

        st.dataframe(
            history,
            width="stretch"
        )

    except Exception as e:
        st.warning(
            "No prediction history found."
        )
# ==========================================================
# ANALYTICS PAGE
# ==========================================================

def analytics_page():

    render_hero()

    st.markdown(
        "## 📈 Advanced Analytics"
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Distribution",
            "Correlations",
            "Explorer"
        ]
    )

    # ------------------------------------------------------
    # DISTRIBUTION
    # ------------------------------------------------------

    with tab1:

        st.subheader(
            "Wine Quality Distribution"
        )

        st.plotly_chart(
    ChartBuilder.quality_distribution(df),
    use_container_width=True,
    key="quality_distribution_analytics"
)
        st.write(
            """
            This chart shows how wine
            samples are distributed
            across quality scores.
            """
        )

    # ------------------------------------------------------
    # CORRELATION
    # ------------------------------------------------------

    with tab2:

        st.subheader(
            "Correlation Analysis"
        )

        st.plotly_chart(
    ChartBuilder.correlation_heatmap(df),
    use_container_width=True,
    key="correlation_heatmap_analytics"
)

        st.write(
            """
            Strong positive and negative
            relationships can help identify
            influential wine properties.
            """
        )

    # ------------------------------------------------------
    # DATA EXPLORER
    # ------------------------------------------------------

    with tab3:

        st.subheader(
            "Interactive Dataset Explorer"
        )

        selected_columns = st.multiselect(
            "Select Columns",
            options=df.columns.tolist(),
            default=df.columns.tolist()[:5]
        )

        filtered_df = df[
            selected_columns
        ]

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

        st.download_button(
            label="⬇ Download Data",
            data=filtered_df.to_csv(
                index=False
            ),
            file_name="wine_data.csv",
            mime="text/csv"
        )

    st.markdown("---")

    st.subheader(
        "Dataset Statistics"
    )

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

# ==========================================================
# MODEL INSIGHTS PAGE
# ==========================================================

def model_insights_page():

    render_hero()

    st.markdown(
        "## 🧠 Model Intelligence Center"
    )

    st.write(
        """
        Explore model performance,
        feature importance,
        and training insights.
        """
    )

    st.markdown("---")

    c1, c2, c3, c4 = st.columns([3,1,1,1])

    c1.metric(
        "Best Model",
        "Random Forest"
    )

    c2.metric(
        "Accuracy",
        "90.3%"
    )

    c3.metric(
        "Features",
        "11"
    )

    c4.metric(
        "Samples",
        "1599"
    )

    st.markdown("---")

    st.subheader(
        "Feature Importance"
    )

    if hasattr(
        model,
        "feature_importances_"
    ):

        feature_names = [
            col
            for col in df.columns
            if col != "quality"
        ]

        st.plotly_chart(
    ChartBuilder.feature_importance(
        model,
        feature_names
    ),
    use_container_width=True,
    key="feature_importance_chart"
)

    else:

        st.warning(
            """
            Current model does not expose
            feature importance values.
            Use Random Forest or
            Decision Tree.
            """
        )

    st.markdown("---")

    st.subheader(
        "Model Comparison"
    )

    st.plotly_chart(
    ChartBuilder.model_comparison(),
    use_container_width=True,
    key="model_comparison_chart"
)

    st.markdown("---")

    st.subheader("📊 Business Insights & Recommendations")

    st.success("""
    🍷 Alcohol Content
    Higher alcohol levels are strongly associated with high-quality wines.
    Premium wines often contain balanced alcohol concentrations.
    """)

    st.success("""
    🧪 Sulphates
    Sulphates help preserve wine quality and improve overall stability.
    """)

    st.info("""
    📈 Data Analysis
    Correlation analysis indicates a positive relationship between alcohol content and wine quality.
    """)

    st.warning("""
    ⚠️ Quality Risks
    High volatile acidity can negatively impact taste, aroma, and overall wine quality.
    """)

    st.info("""
    🤖 AI Model Insight
    The machine learning model uses feature importance analysis to explain its predictions and identify key quality drivers.
    """)
    st.markdown("---")

    st.success("""
    ### 🏆 Key Takeaway
    Alcohol, Sulphates, and Citric Acid positively influence wine quality,
    while excessive Volatile Acidity and extreme pH values may reduce quality.
    """)


# ==========================================================
# ABOUT PAGE
# ==========================================================

def about_page():

    render_hero()

    st.markdown(
        "## 🚀 About WineIQ Analytics"
    )

    st.write(
        """
        WineIQ Analytics is an AI-powered
        wine intelligence platform built
        using Machine Learning and
        Streamlit.
        """
    )

    st.markdown("---")

    st.subheader(
        "Project Highlights"
    )

    st.markdown(
        """
        ✅ Machine Learning Pipeline

        ✅ Interactive Dashboard

        ✅ Real-Time Prediction

        ✅ Plotly Visualizations

        ✅ Model Explainability

        ✅ Production Deployment
        """
    )

    st.markdown("---")

    st.subheader(
        "Technology Stack"
    )

    tech_df = pd.DataFrame(
        {
            "Technology": [
                "Python",
                "Pandas",
                "NumPy",
                "Scikit-Learn",
                "Plotly",
                "Streamlit",
                "Joblib"
            ],
            "Purpose": [
                "Programming",
                "Data Analysis",
                "Numerical Computing",
                "Machine Learning",
                "Visualization",
                "Frontend",
                "Model Persistence"
            ]
        }
    )

    st.dataframe(
        tech_df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Architecture"
    )

    st.code(
        """
User
 ↓
Streamlit UI
 ↓
Prediction Engine
 ↓
Scaler
 ↓
ML Model
 ↓
Prediction Output
        """
    )

    st.markdown("---")

    st.subheader(
        "Author"
    )

    st.success(
        """
        Hemanth Reddy

        CSE (AI & ML)

        WineIQ Analytics
        """
    )
# ==========================================================
# FOOTER
# ==========================================================

def render_footer():

    st.markdown("---")

    st.markdown(
        """
        <div style='text-align:center;
                    padding:20px;'>

        <h4>🍷 WineIQ Analytics</h4>

        <p>
        AI-Powered Wine Intelligence Platform
        </p>

        <p>
        Built with ❤️ using
        Python • Streamlit • Scikit-Learn
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================================
# NAVIGATION
# ==========================================================

# ==========================================================
# MAIN APPLICATION ROUTING
# ==========================================================
def explainability_page():

    st.title("🔍 Model Explainability Dashboard")

    st.subheader("📈 Feature Importance Analysis")
    import pandas as pd

    feature_df = pd.DataFrame({
        "Feature": [
            "Alcohol",
            "Sulphates",
            "Citric Acid",
            "Volatile Acidity",
            "pH"
        ],
        "Contribution": [
            0.42,
            0.18,
            0.15,
            -0.12,
            -0.05
        ]
    })

    st.dataframe(
        feature_df,
        use_container_width=True
    )

    st.bar_chart(
        feature_df.set_index("Feature")
    )

    st.subheader("🔍 Key Findings")

    st.success("""
    🍷 Alcohol is the strongest predictor of wine quality.
    Higher alcohol levels are generally associated with premium wines.
    """)

    st.success("""
    🧪 Sulphates improve wine stability and overall quality.
    """)

    st.warning("""
    ⚠️ High Volatile Acidity can negatively affect taste and aroma.
    """)

    st.success("""
    🍋 Citric Acid contributes positively to wine quality.
    """)

    st.warning("""
    ⚠️ Extreme pH values may reduce wine stability and quality.
    """)
page = Sidebar.render()

if page == "Dashboard":

    dashboard_page()

elif page == "Prediction":

    prediction_page()

elif page == "History":

    history_page()

elif page == "Analytics":

    analytics_page()

elif page == "Model Insights":

    model_insights_page()

elif page == "Explainability":

    explainability_page()

elif page == "About":

    about_page()

render_footer()