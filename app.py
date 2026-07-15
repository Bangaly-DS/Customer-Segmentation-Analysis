import streamlit as st
import joblib
import pandas as pd
from utils.preprocessing import preprocess_input
from utils.segments import cluster_profiles


segment_profiles = cluster_profiles

segment_names = {
    key: value["name"]
    for key, value in segment_profiles.items()
}

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Customer Segmentation Analysis",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# Load model artifacts
# -----------------------------------
kmeans_model = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

# Show success message
st.success("✅ Model artifacts loaded successfully!")

# Inspect the loaded feature columns
# st.write(feature_columns)

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []


# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.title("📊 Customer Segmentation")

    st.markdown("---")

    st.subheader("🎯 About this Project")
    st.write(
        """
          This application uses a Machine Learning model with
          **K-Means Clustering** to classify customers into meaningful
          business segments based on demographic and enrollment information.
        """
    )

    st.markdown("---")

    st.subheader("⚙️ Model Information")

    c1, c2 = st.columns(2)

    with c1:
       st.metric("Clusters", "8")

    with c2:
       st.metric("Algorithm", "K-Means")

    c3, c4 = st.columns(2)

    with c3:
       st.metric("Framework", "Streamlit")

    with c4:
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
    st.caption("Data Scientist & Machine Learning Engineer")

    st.markdown(
        "[GitHub](https://github.com/Bangaly-DS)"
    )

    st.markdown(
        "[LinkedIn](https://linkedin.com/in/sano-bangaly-064535146)"
    )
    st.markdown("---")

    st.markdown("### 🚀 Application Status")

    st.success("Model Loaded Successfully")

    st.caption("Ready for Customer Predictions")





st.subheader("🚀 What's Coming Next")

st.markdown("""
    In the next stages, this application will allow you to:
            
    - Input customer information
    - Predict the customer's segment
    - Explore cluster characteristics
    - Visualize customer groups
    - Understand business insights behind each cluster
""")

# --------------------------------------
# Customer Information
# --------------------------------------

st.header("📝 Customer Information")
st.caption("Enter the customer's information below, then click **Predict Customer**.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    salary = st.number_input("💰 Salary", min_value=0.0)
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    education = st.selectbox(
        "🎓 Education",
        [
            "Bachelor",
            "College",
            "Doctor",
            "High School or Below",
            "Master"
        ]
    )
    marital_status = st.selectbox(
        "💍 Marital Status",
        ["Married", "Single"]
    )

with col2:
    clv = st.number_input("💎 Customer Lifetime Value (CLV)", min_value=0.0)

    enrollment_date = st.date_input(
        "📅 Enrollment Date"
    )

    loyalty_card = st.selectbox(
        "⭐ Loyalty Card",
        ["Nova", "Star"]
    )

    enrollment_type = st.selectbox(
        "📌 Enrollment Type",
        ["Standard", "2018 Promotion"]
    )

    enrollment_year = enrollment_date.year
    enrollment_month = enrollment_date.month


if st.button(
    "🔍︎ Predict Customer", use_container_width=True):

    # Preprocess the input
    processed_data = preprocess_input(
        salary=salary,
        clv=clv,
        enrollment_year=enrollment_year,
        enrollment_month=enrollment_month,
        gender=gender,
        education=education,
        marital_status=marital_status,
        loyalty_card=loyalty_card,
        enrollment_type=enrollment_type,
        feature_columns=feature_columns         
    )
    # Scale the data
    scaled_data = scaler.transform(processed_data)

    # Predict the cluster
    prediction = kmeans_model.predict(scaled_data)

    # Distance to every cluster center
    distances = kmeans_model.transform(scaled_data)

    # Distance to assign cluster
    cluster_distance = distances[0][prediction[0]]

    # Confidence Score (0-100%)
    confidence = max(0, 100 - cluster_distance * 10)
    confidence = round(confidence, 1)

    # Everything below happens only after clicking the button
    cluster = int(prediction[0])

    segment = segment_names.get(
        cluster,
        f"Cluster {cluster}"
    )

    st.success(f"✅ Prediction completed. Customer belongs to the '{segment}' segment.")

    st.metric(
        label="Prediction Confidence",
        value=f"{confidence}%"
    )
    
    if confidence >= 90:
        st.success("🟢 Very High Confidence")

    elif confidence >= 75:
        st.info("🔵 High Confidence")

    elif confidence >= 60:
        st.warning("🟡 Moderate Confidence")

    else:
        st.error("🔴 Low Confidence")        


    # ----------------------------------------
    # 🎯 Prediction
    # ----------------------------------------
    st.subheader("🎯 Prediction Results")
    
    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:
        st.metric(
            label="Customer Segment",
            value=segment
        )

    with col2:
        st.metric(
            label="Cluster ID",
            value=cluster
        )

    st.metric(
        label="Distance to Cluster Center",
        value=f"{cluster_distance:.2f}"
    )    

    st.caption(
        "Smaller values indicate the customer is more representative of the assigned segment."
    )
    
    from datetime import datetime

    st.session_state.prediction_history.append({
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Segment": segment,
        "Cluster": cluster,
        "Distance": round(cluster_distance, 2)
    })


    cluster = int(prediction[0])

    profile = cluster_profiles[cluster]

    segment = profile["name"]
    description = profile["description"]
    recommendations =  profile["recommendation"]

    st.divider()

    st.info(f"📌 {description}")

    st.subheader("📊 Business Insight")

    st.success(profile["business_insight"])

    st.markdown("### 💡 Recommended Actions")

    for action in recommendations:
        st.markdown(f"✅ {action}")

    # -----------------------------------------
    # Technical Details (Optional)
    # -----------------------------------------

    with st.expander("🔧 Show Technical Details"):
        st.markdown("### 🔍︎ Processed Input ")
        st.dataframe(processed_data, use_container_width=True)

        st.markdown("### ⚙️ Scaled Data")

        scaled_df = pd.DataFrame(
            scaled_data,
            columns=processed_data.columns
        )

        st.dataframe(
            scaled_df,
            use_container_width=True
        )

st.divider()

st.subheader("🕘 Prediction History")

if st.session_state.prediction_history:
    st.dataframe(
        st.session_state.prediction_history,
        use_container_width=True
    )
else:
    st.info("No predictions have been made yet.")        

st.divider()

st.markdown("""
    <div style="text-align:center; font-size:14px; color:#9AA0A6;">

    📊 <b>Customer Segmentation Analysis</b><br>

    Built by <b>Bangaly Sano</b><br><br>

    <a href="https://github.com/Bangaly-DS/Customer-Segmentation-Analysis" target="_blank">
    GitHub Repository
    </a> |
    <a href="https://www.linkedin.com/in/sano-bangaly-064535146" target="_blank">
    LinkedIn
    </a>

    <br><br>

    Python • Scikit-learn • Streamlit • K-Means

    <br><br>

    © 2026 All Rights Reserved

    </div>
    """, unsafe_allow_html=True)
