# Customer Segmentation Analysis using Machine Learning

A Machine Learning-powered customer segmentation application built with **Python**, **Scikit-learn**, and **Streamlit**. The application classifies customers into distinct segments using the K-Means clustering algorithm, helping businesses better understand customer behavior and support data-driven marketing decisions.

---

## Live Demo

Coming Soon 🚀

---

## Features

- Customer segmentation using K-Means Clustering
- Interactive Streamlit web application
- Real-time customer segment prediction
- Automatic preprocessing of user inputs
- Feature scaling using a saved StandardScaler
- Prediction history
- Cluster descriptions with business insights
- PCA-based cluster visualization

---

## Dataset

**Customer Loyalty History Dataset**

The project uses customer demographic and loyalty information including:

- Salary
- Customer Lifetime Value (CLV)
- Gender
- Education
- Marital Status
- Loyalty Card
- Enrollment Type
- Enrollment Year
- Enrollment Month

---

## Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. One-Hot Encoding
5. Feature Scaling
6. K-Means Clustering
7. Cluster Evaluation
   - Elbow Method
   - Silhouette Score
8. Cluster Profiling
9. Model Serialization using Joblib
10. Streamlit Deployment

---

## Project Evolution

This repository contains two iterations of the project:

- **Version 1** documents the initial customer segmentation analysis, exploratory data analysis (EDA), feature engineering, clustering workflow, and customer profiling.
- **Version 2** builds on Version 1 by refining the workflow, serializing the trained model with Joblib, and integrating it into an interactive Streamlit web application for real-time customer segment prediction.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib

---

## Project Structure

```text
Customer-Segmentation-Analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── utils/
│   ├── preprocessing.py
│   └── segments.py
│
├── data/
│   └── Customer Loyalty History.csv
```

## Installation

```bash
git clone https://github.com/Bangaly-DS/Customer-Segmentation-Analysis.git

cd Customer-Segmentation-Analysis

pip install -r requirements.txt

streamlit run app.py
```

## Future Improvements

- Customer profile dashboards
- Downloadable prediction reports
- Advanced visualizations
- Model comparison with additional clustering algorithms

## Author

**Bangaly Sano**

GitHub: https://github.com/Bangaly-DS

LinkedIn: https://linkedin.com/in/sano-bangaly-064535146