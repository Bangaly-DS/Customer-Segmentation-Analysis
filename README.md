# ✈️ Customer Segmentation Analysis using Machine Learning

> An end-to-end machine learning project that segments airline loyalty customers using **K-Means Clustering** to uncover meaningful customer groups and generate actionable business insights. This project is actively evolving from exploratory data analysis to a fully deployed web application for interactive customer segmentation.

---

## 📌 Project Status

| Stage | Status |
|--------|--------|
| 📥 Data Collection | ✅ Complete |
| 🧹 Data Cleaning & Preprocessing | ✅ Complete |
| 📊 Exploratory Data Analysis (EDA) | ✅ Complete |
| 🔍 Data Quality Assessment | ✅ Complete |
| ⚙️ Feature Engineering | ✅ Complete |
| 📏 Feature Scaling | ✅ Complete |
| 🤖 K-Means Clustering | ✅ Complete |
| 📈 Cluster Evaluation | ✅ Complete |
| 💡 Business Insights | ✅ Complete |
| 🚀 Model Improvements | 🚧 In Progress |
| 🌐 Web Application | ⏳ Planned |
| ☁️ Deployment | ⏳ Planned |

---

# 📖 Project Overview

Understanding customer behavior is essential for businesses seeking to improve customer satisfaction, increase retention, and optimize marketing strategies.

This project analyzes customer data from an **Airline Loyalty Program** to identify meaningful customer segments using **K-Means Clustering**, an unsupervised machine learning algorithm.

The analysis includes comprehensive data cleaning, exploratory data analysis, feature engineering, clustering, visualization, and business interpretation to transform raw customer data into actionable insights.

This repository represents an evolving end-to-end machine learning project. Future versions will extend the analysis by introducing a production-ready web application that allows users to perform customer segmentation interactively.

---

# 🎯 Project Objectives

- Clean and preprocess customer data.
- Assess overall data quality.
- Perform exploratory data analysis (EDA).
- Engineer relevant analytical features.
- Standardize selected features for clustering.
- Determine the optimal number of customer clusters.
- Build customer segments using K-Means Clustering.
- Interpret cluster characteristics from a business perspective.
- Provide actionable recommendations for marketing and customer retention.
- Deploy the solution as an interactive web application.

---

# 📊 Dataset

The dataset contains customer information from an Airline Loyalty Program.

### Features include:

- Customer Lifetime Value (CLV)
- Salary
- Loyalty Card Type
- Marital Status
- Gender
- Education
- Enrollment Information
- Flight Activity
- Other demographic and behavioral attributes

The dataset is used to identify groups of customers with similar characteristics and purchasing behavior.

---

# 🛠 Technologies Used

| Category | Tools |
|-----------|-------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Data Visualization | Matplotlib |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 🔄 Project Workflow

The project follows an end-to-end data science workflow:

1. Data Loading
2. Data Quality Assessment
3. Missing Value Investigation
4. Exploratory Data Analysis (EDA)
5. Outlier Detection
6. Feature Engineering
7. Feature Selection
8. Feature Scaling using StandardScaler
9. Optimal Cluster Selection (Elbow Method)
10. K-Means Clustering
11. Cluster Visualization
12. Cluster Profiling
13. Business Insights
14. Business Recommendations

---

# 📊 Exploratory Data Analysis

The exploratory analysis investigates:

- Missing values
- Duplicate records
- Data types
- Distribution of customer demographics
- Salary distribution
- Customer Lifetime Value distribution
- Loyalty Card distribution
- Marital Status
- Gender distribution
- Correlation between numerical variables
- Outlier detection

The goal is to understand customer characteristics before applying machine learning techniques.

---

# 🤖 Machine Learning

### Algorithm Used

- K-Means Clustering

### Feature Scaling

- StandardScaler

### Optimal Number of Clusters

The Elbow Method was used to determine the optimal value of **K**, resulting in:

**K = 3**

The model groups customers into three distinct customer segments.

---

# 📈 Results

The clustering model successfully identified three meaningful customer groups based primarily on:

- Customer Lifetime Value (CLV)
- Salary

Each cluster represents customers with different financial characteristics and purchasing potential.

---

# 💡 Key Business Insights

### 🟢 Cluster 0

- Lower salary
- Lower customer lifetime value
- Price-sensitive customers
- Suitable for promotional campaigns

---

### 🔵 Cluster 1

- Moderate salary
- Moderate customer lifetime value
- Loyal regular customers
- Ideal for personalized engagement

---

### 🟣 Cluster 2

- High salary
- High customer lifetime value
- Premium customers
- High retention priority
- Best suited for exclusive rewards and loyalty programs

---

# 📈 Business Recommendations

Based on the identified customer segments, businesses can:

- Offer discounts and promotional campaigns to budget-conscious customers.
- Deliver personalized marketing campaigns to regular customers.
- Prioritize premium services and loyalty rewards for high-value customers.
- Improve customer retention using targeted engagement strategies.
- Optimize marketing spending through customer segmentation.

---

# 📷 Project Visualizations

The repository includes visualizations such as:

- Dataset Overview
- Missing Value Analysis
- Salary Distribution
- Customer Lifetime Value Distribution
- Correlation Heatmap
- Outlier Detection
- Elbow Method
- Customer Clusters
- Cluster Distribution

> Screenshots of these visualizations are available in the **images/** directory.

---

# 📂 Repository Structure

```text
Customer-Segmentation-Analysis/
│
├── notebooks/
│   └── customer_segmentation_analysis.ipynb
│
├── data/
│   ├── Customer Segmentation.csv
│   └── README.md
│
├── images/
│   ├── dataset_overview.png
│   ├── missing_values.png
│   ├── salary_distribution.png
│   ├── correlation_heatmap.png
│   ├── elbow_method.png
│   ├── customer_clusters.png
│   └── cluster_distribution.png
│
├── app/                 # Planned
├── models/              # Planned
│
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

# 🚀 Future Roadmap

This project is actively being improved.

### Planned enhancements include:

- Improve feature engineering
- Compare K-Means with DBSCAN and Hierarchical Clustering
- Improve cluster profiling
- Build an interactive Streamlit web application
- Deploy the application to the cloud
- Allow users to upload customer data for segmentation
- Improve project documentation
- Add automated testing

---

# 💼 Skills Demonstrated

- Data Cleaning
- Data Quality Assessment
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Scaling
- Machine Learning
- Unsupervised Learning
- K-Means Clustering
- Model Evaluation
- Business Analytics
- Data Visualization
- Python Programming
- Git & GitHub

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Bangaly-DS/Customer-Segmentation-Analysis.git
```

Navigate into the project directory:

```bash
cd Customer-Segmentation-Analysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/customer_segmentation_analysis.ipynb
```

---

# 📌 Project Evolution

This project is being developed iteratively.

### ✅ Current Version

- Data preprocessing
- Exploratory Data Analysis
- K-Means Clustering
- Customer segmentation
- Business insights

### 🚧 Next Version

- Enhanced feature engineering
- Improved clustering workflow
- Additional clustering algorithm comparisons

### 🚀 Final Version

- Interactive web application
- Cloud deployment
- Production-ready customer segmentation tool

---

# 👨‍💻 Author

**Bangaly Sano**

📧 Email: sanobangaly@hotmail.com

🔗 LinkedIn: https://linkedin.com/in/sano-bangaly-064535146

💻 GitHub: https://github.com/Bangaly-DS

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. Feedback, suggestions, and contributions are always welcome.
