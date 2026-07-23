import streamlit as st
import joblib
import pandas as pd

from datetime import date, datetime
from pathlib import Path

from utils.preprocessing import preprocess_input
from utils.segments import cluster_profiles


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Customer Segmentation Analysis",
    page_icon="📊",
    layout="wide",
)


# ==========================================================
# APPLICATION CONFIGURATION
# ==========================================================

APP_TITLE = "Customer Segmentation Analysis"

MODEL_PATH = Path("models/kmeans_model.pkl")
SCALER_PATH = Path("models/scaler.pkl")
FEATURE_COLUMNS_PATH = Path("models/feature_columns.pkl")

DEFAULT_ENROLLMENT_DATE = date(2018, 1, 1)
MIN_ENROLLMENT_DATE = date(2010, 1, 1)

GENDER_OPTIONS = [
    "Male",
    "Female",
]

EDUCATION_OPTIONS = [
    "Bachelor",
    "College",
    "Doctor",
    "High School or Below",
    "Master",
]

MARITAL_STATUS_OPTIONS = [
    "Divorced",
    "Married",
    "Single",
]

LOYALTY_CARD_OPTIONS = [
    "No",
    "Yes",
]

ENROLLMENT_TYPE_OPTIONS = [
    "2018 Promotion",
    "Standard",
]


# ==========================================================
# MODEL ARTIFACT LOADING
# ==========================================================

@st.cache_resource
def load_artifacts():
    """
    Load all serialized machine learning artifacts.

    Returns:
        tuple:
            - K-Means model
            - Feature scaler
            - Feature column names

    Raises:
        FileNotFoundError:
            If any required model artifact is missing.
    """

    required_files = [
        MODEL_PATH,
        SCALER_PATH,
        FEATURE_COLUMNS_PATH,
    ]

    missing_files = [
        str(file_path)
        for file_path in required_files
        if not file_path.exists()
    ]

    if missing_files:
        raise FileNotFoundError(
            "The following model artifact(s) could not be found:\n"
            + "\n".join(missing_files)
        )

    kmeans_model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    feature_columns = joblib.load(FEATURE_COLUMNS_PATH)

    return kmeans_model, scaler, feature_columns


# ==========================================================
# SESSION STATE
# ==========================================================

def initialize_session_state():
    """
    Initialize application session state variables.
    """

    if "prediction_history" not in st.session_state:
        st.session_state.prediction_history = []


# ==========================================================
# VALIDATION HELPERS
# ==========================================================

def validate_numeric(
    value: str,
    field_name: str,
    minimum: float = 0,
):
    """
    Validate a numeric text input.

    Args:
        value: Raw text input.
        field_name: Name displayed in validation messages.
        minimum: Minimum allowed numeric value.

    Returns:
        float | None:
            Validated numeric value or None if validation fails.
    """

    if not value or not value.strip():
        st.error(f"❌ {field_name} is required.")
        return None

    try:
        number = float(value)

    except ValueError:
        st.error(f"❌ {field_name} must be numeric.")
        return None

    if number < minimum:
        st.error(
            f"❌ {field_name} cannot be less than {minimum}."
        )
        return None

    return number


def calculate_confidence(distance: float) -> float:
    """
    Convert distance from the cluster center into a
    simple match-confidence score.

    Smaller distances indicate stronger cluster similarity.

    Args:
        distance: Distance from the assigned cluster center.

    Returns:
        Confidence score between 0 and 100.
    """

    confidence = max(0, 100 - (distance * 10))

    return round(confidence, 1)


def render_confidence_message(confidence: float):
    """
    Render a confidence indicator based on the match score.
    """

    if confidence >= 90:
        st.success("🟢 Very High Confidence")

    elif confidence >= 75:
        st.info("🔵 High Confidence")

    elif confidence >= 60:
        st.warning("🟡 Moderate Confidence")

    else:
        st.error("🔴 Low Confidence")


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title("📊 Customer Segmentation")

        st.markdown("---")

        st.subheader("🎯 About this Project")

        st.write(
            """
            This application uses a Machine Learning model with
            **K-Means Clustering** to classify customers into
            meaningful business segments based on demographic,
            financial, and enrollment information.
            """
        )

        st.markdown("---")

        st.subheader("⚙️ Model Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Clusters", "8")

        with col2:
            st.metric("Algorithm", "K-Means")

        col3, col4 = st.columns(2)

        with col3:
            st.metric("Framework", "Streamlit")

        with col4:
            st.metric("Language", "Python")

        st.markdown("---")

        st.subheader("📈 Business Goal")

        st.success(
            """
            Identify customer groups so businesses can:

            • Improve customer retention

            • Personalize marketing campaigns

            • Increase Customer Lifetime Value (CLV)

            • Allocate resources more effectively
            """
        )

        st.markdown("---")

        st.subheader("👨🏽‍💻 Developer")

        st.write("**Bangaly Sano**")

        st.caption(
            "Data Scientist & Machine Learning Engineer"
        )

        st.markdown(
            "[GitHub](https://github.com/Bangaly-DS)"
        )

        st.markdown(
            "[LinkedIn](https://linkedin.com/in/sano-bangaly-064535146)"
        )

        st.markdown("---")

        st.markdown("### 🚀 Application Status")

        st.success("Model Loaded Successfully")

        st.caption(
            "Ready for Customer Predictions"
        )


# ==========================================================
# MAIN PAGE INTRODUCTION
# ==========================================================

def render_introduction():
    """
    Render the application introduction.
    """

    st.subheader("🚀 Customer Segmentation Analysis")

    st.markdown(
        """
        This application uses an Unsupervised Machine Learning model to identify
        meaningful customer segments based on financial, demographic, loyalty, and enrollment characteristics.
        """
    )

    st.info(
        """
        💡 Enter customer information below to receive a segment prediction, cluster match score, and business recommendations.
        """
    )


# ==========================================================
# CUSTOMER INFORMATION FORM
# ==========================================================

def render_customer_form():
    """
    Render the customer information form.

    Returns:
        tuple:
            All submitted form values and submission state.
    """

    st.subheader("📝 Customer Information")

    with st.form(
        key="customer_form",
        clear_on_submit=False,
    ):

        col1, col2 = st.columns(2)

        # --------------------------------------------------
        # LEFT COLUMN
        # --------------------------------------------------

        with col1:

            salary_input = st.text_input(
                "Annual Salary",
                placeholder="Enter annual salary (e.g. 55000)",
                help="Enter the customer's annual salary.",
            )

            clv_input = st.text_input(
                "Customer Lifetime Value (CLV)",
                placeholder="Enter customer lifetime value",
                help="Enter the estimated lifetime value of the customer.",
            )

            gender = st.selectbox(
                "Gender",
                options=GENDER_OPTIONS,
            )

            education = st.selectbox(
                "Education",
                options=EDUCATION_OPTIONS,
            )

        # --------------------------------------------------
        # RIGHT COLUMN
        # --------------------------------------------------

        with col2:

            marital_status = st.selectbox(
                "Marital Status",
                options=MARITAL_STATUS_OPTIONS,
            )

            loyalty_card = st.selectbox(
                "Loyalty Card",
                options=LOYALTY_CARD_OPTIONS,
            )

            enrollment_type = st.selectbox(
                "Enrollment Type",
                options=ENROLLMENT_TYPE_OPTIONS,
            )

            enrollment_date = st.date_input(
                "Enrollment Date (2010–Present)",
                value=DEFAULT_ENROLLMENT_DATE,
                min_value=MIN_ENROLLMENT_DATE,
                max_value=date.today(),
                help="Select an enrollment date between January 1, 2010 and today.",
            )
        

        st.markdown("")

        submitted = st.form_submit_button(
            "🔍 Predict Customer",
            use_container_width=True,
        )

    return {
        "salary_input": salary_input,
        "clv_input": clv_input,
        "gender": gender,
        "education": education,
        "marital_status": marital_status,
        "loyalty_card": loyalty_card,
        "enrollment_type": enrollment_type,
        "enrollment_date": enrollment_date,
        "submitted": submitted,
    }


# ==========================================================
# INPUT VALIDATION
# ==========================================================

def validate_customer_inputs(form_data):
    """
    Validate all numeric customer inputs.

    Returns:
        tuple:
            Validated salary and CLV values.
    """

    salary = validate_numeric(
        value=form_data["salary_input"],
        field_name="Salary",
    )

    clv = validate_numeric(
        value=form_data["clv_input"],
        field_name="Customer Lifetime Value",
    )

    return salary, clv


# ==========================================================
# CUSTOMER PREDICTION
# ==========================================================

def predict_customer(
    salary,
    clv,
    form_data,
    feature_columns,
    scaler,
    kmeans_model,
):
    """
    Preprocess input data, scale features, and predict
    the customer's cluster.

    Returns:
        dict:
            Complete prediction results.
    """

    enrollment_date = form_data["enrollment_date"]

    processed_data = preprocess_input(
        salary=salary,
        clv=clv,
        enrollment_year=enrollment_date.year,
        enrollment_month=enrollment_date.month,
        gender=form_data["gender"],
        education=form_data["education"],
        marital_status=form_data["marital_status"],
        loyalty_card=form_data["loyalty_card"],
        enrollment_type=form_data["enrollment_type"],
        feature_columns=feature_columns,
    )

    scaled_data = scaler.transform(processed_data)

    prediction = kmeans_model.predict(scaled_data)

    cluster = int(prediction[0])

    distances = kmeans_model.transform(scaled_data)

    cluster_distance = float(
        distances[0][cluster]
    )

    confidence = calculate_confidence(
        cluster_distance
    )

    profile = cluster_profiles[cluster]

    return {
        "processed_data": processed_data,
        "scaled_data": scaled_data,
        "cluster": cluster,
        "cluster_distance": cluster_distance,
        "confidence": confidence,
        "profile": profile,
        "segment": profile["name"],
    }


# ==========================================================
# PREDICTION RESULT DISPLAY
# ==========================================================

def render_prediction_results(prediction_result):
    """
    Display the prediction results and business insights.
    """

    cluster = prediction_result["cluster"]
    cluster_distance = prediction_result["cluster_distance"]
    confidence = prediction_result["confidence"]
    profile = prediction_result["profile"]
    segment = prediction_result["segment"]

    # ------------------------------------------------------
    # SUCCESS MESSAGE
    # ------------------------------------------------------

    st.success(
        f"✅ Prediction completed successfully.\n\n"
        f"Customer belongs to the **{segment}** segment."
    )

    # ------------------------------------------------------
    # CONFIDENCE SCORE
    # ------------------------------------------------------

    st.metric(
        "Segment Match Score",
        f"{confidence}%",
    )

    render_confidence_message(
        confidence
    )

    # ------------------------------------------------------
    # PREDICTION RESULTS
    # ------------------------------------------------------

    st.subheader("🎯 Prediction Results")

    st.divider()

    metric1, metric2 = st.columns([3, 1])

    with metric1:

        st.metric(
            "Customer Segment",
            segment,
        )

    with metric2:

        st.metric(
            "Cluster ID",
            cluster,
        )

    st.metric(
        "Distance to Cluster Center",
        f"{cluster_distance:.2f}",
    )

    st.caption(
        "This is an approximate similarity score based on the customer's distance from the assigned cluster center."
    )

    # ------------------------------------------------------
    # BUSINESS INSIGHT
    # ------------------------------------------------------

    st.divider()

    st.info(
        f"📌 {profile['description']}"
    )

    st.subheader("📊 Business Insight")

    st.success(
        profile["business_insight"]
    )

    # ------------------------------------------------------
    # RECOMMENDED ACTIONS
    # ------------------------------------------------------

    st.markdown("### 💡 Recommended Actions")

    for recommendation in profile["recommendation"]:

        st.markdown(
            f"✅ {recommendation}"
        )


# ==========================================================
# TECHNICAL DETAILS
# ==========================================================

def render_technical_details(prediction_result):
    """
    Display processed and scaled input data.
    """

    processed_data = prediction_result["processed_data"]

    scaled_data = prediction_result["scaled_data"]

    with st.expander(
        "🔧 Show Technical Details"
    ):

        st.markdown(
            "### 🔍 Processed Input"
        )

        st.dataframe(
            processed_data,
            use_container_width=True,
        )

        st.markdown(
            "### ⚙️ Scaled Features"
        )

        scaled_df = pd.DataFrame(
            scaled_data,
            columns=processed_data.columns,
        )

        st.dataframe(
            scaled_df,
            use_container_width=True,
        )


# ==========================================================
# PREDICTION HISTORY
# ==========================================================

def save_prediction_to_history(prediction_result):
    """
    Save the latest prediction to session history.
    """

    st.session_state.prediction_history.append(
        {
            "Time": datetime.now().strftime(
                "%H:%M:%S"
            ),
            "Segment": prediction_result["segment"],
            "Cluster": prediction_result["cluster"],
            "Distance": round(
                prediction_result["cluster_distance"],
                2,
            ),
        }
    )


def render_prediction_history():
    """
    Render prediction history for the current session.
    """

    st.divider()

    st.subheader("🕘 Prediction History")

    history = st.session_state.prediction_history

    if not history:

        st.info(
            "No predictions have been made yet."
        )

        return

    history_df = pd.DataFrame(history)

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True,
    )


# ==========================================================
# FOOTER
# ==========================================================

def render_footer():
    """
    Render the application footer.
    """

    st.divider()

    st.markdown(
        """
        <div style="text-align:center;
                    font-size:14px;
                    color:#9AA0A6;">

        📊 <b>Customer Segmentation Analysis</b><br><br>

        Built by <b>Bangaly Sano</b><br><br>

        <a href="https://github.com/Bangaly-DS/Customer-Segmentation-Analysis"
           target="_blank">
            GitHub Repository
        </a>

        &nbsp; | &nbsp;

        <a href="https://www.linkedin.com/in/sano-bangaly-064535146"
           target="_blank">
            LinkedIn
        </a>

        <br><br>

        Python • Scikit-learn • Streamlit • K-Means

        <br><br>

        © 2026 All Rights Reserved

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# MAIN APPLICATION
# ==========================================================

def main():
    """
    Main application entry point.
    """

    initialize_session_state()

    # ------------------------------------------------------
    # LOAD MODEL ARTIFACTS
    # ------------------------------------------------------

    try:

        kmeans_model, scaler, feature_columns = (
            load_artifacts()
        )

    except FileNotFoundError as error:

        st.error(
            "❌ Model artifacts could not be loaded."
        )

        st.exception(error)

        st.stop()

    except Exception as error:

        st.error(
            "❌ An unexpected error occurred while "
            "loading the machine learning model."
        )

        st.exception(error)

        st.stop()

    # ------------------------------------------------------
    # SIDEBAR
    # ------------------------------------------------------

    render_sidebar()

    # ------------------------------------------------------
    # MAIN PAGE
    # ------------------------------------------------------

    render_introduction()

    # ------------------------------------------------------
    # CUSTOMER FORM
    # ------------------------------------------------------

    form_data = render_customer_form()

    # ------------------------------------------------------
    # PREDICTION PIPELINE
    # ------------------------------------------------------

    if form_data["submitted"]:

        salary, clv = validate_customer_inputs(
            form_data
        )

        if salary is not None and clv is not None:

            try:

                prediction_result = predict_customer(
                    salary=salary,
                    clv=clv,
                    form_data=form_data,
                    feature_columns=feature_columns,
                    scaler=scaler,
                    kmeans_model=kmeans_model,
                )

                save_prediction_to_history(
                    prediction_result
                )

                render_prediction_results(
                    prediction_result
                )

                render_technical_details(
                    prediction_result
                )

            except Exception as error:

                st.error(
                    "❌ An error occurred while processing "
                    "the customer prediction."
                )

                st.exception(error)

    # ------------------------------------------------------
    # PREDICTION HISTORY
    # ------------------------------------------------------

    render_prediction_history()

    # ------------------------------------------------------
    # FOOTER
    # ------------------------------------------------------

    render_footer()


# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    main()

