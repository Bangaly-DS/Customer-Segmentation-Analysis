# ✈️ Customer Segmentation Analysis using Machine Learning

> An end-to-end machine learning project that segments airline loyalty customers using **K-Means Clustering** to uncover meaningful customer groups and generate actionable business insights. This project is actively evolving toward a fully deployed interactive web application.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Project Overview

Customer segmentation enables businesses to understand their customers beyond demographics by identifying groups with similar behaviors and characteristics.

In this project, customer data from an **Airline Loyalty Program** is analyzed and segmented using **K-Means Clustering**. The workflow covers data preprocessing, exploratory data analysis, feature engineering, clustering, evaluation, and business interpretation to transform raw customer data into actionable insights.

This repository is an evolving machine learning project. Future updates will extend the analysis into a fully interactive web application where users can upload customer data and generate customer segments in real time.

---

# 🚀 Project Status

| Stage | Status |
|--------|--------|
| Data Cleaning & Preprocessing | ✅ Complete |
| Exploratory Data Analysis | ✅ Complete |
| Data Quality Assessment | ✅ Complete |
| Feature Engineering | ✅ Complete |
| Feature Scaling | ✅ Complete |
| K-Means Clustering | ✅ Complete |
| Cluster Evaluation | ✅ Complete |
| Business Insights | ✅ Complete |
| Enhanced Modeling | 🚧 In Progress |
| Web Application | ⏳ Planned |
| Deployment | ⏳ Planned |

---

# 🎯 Project Objectives

- Clean and prepare customer data.
- Assess overall data quality.
- Explore customer demographics and financial behavior.
- Engineer relevant analytical features.
- Standardize features for clustering.
- Determine the optimal number of customer segments.
- Build customer clusters using K-Means.
- Interpret customer segments from a business perspective.
- Generate actionable recommendations for marketing and customer retention.
- Deploy the solution as an interactive machine learning application.

---

# 📊 Dataset

The dataset contains customer information from an Airline Loyalty Program.

### Key Features

- Customer Lifetime Value (CLV)
- Salary
- Loyalty Card
- Gender
- Marital Status
- Education
- Enrollment Information
- Flight Activity
- Other demographic and behavioral attributes

The objective is to identify groups of customers with similar characteristics for targeted marketing and strategic decision-making.

---

# 🛠 Technologies Used

| Category | Tools |
|-----------|-------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 🔄 Project Workflow

1. Data Loading
2. Data Quality Assessment
3. Missing Value Investigation
4. Exploratory Data Analysis
5. Outlier Detection
6. Feature Engineering
7. Feature Selection
8. Feature Scaling using StandardScaler
9. Optimal Cluster Selection using the Elbow Method
10. K-Means Clustering
11. Cluster Evaluation
12. Cluster Profiling
13. Business Insights
14. Business Recommendations

---

# 🤖 Machine Learning

### Algorithm

- K-Means Clustering

### Feature Scaling

- StandardScaler

### Cluster Selection

The optimal number of clusters was determined using the **Elbow Method**, resulting in **K = 5**.

The resulting customer segments reveal distinct differences in customer lifetime value and financial characteristics.

---

# 📈 Key Visualizations

## Elbow Method

The Elbow Method was used to identify the optimal number of clusters by examining the Within-Cluster Sum of Squares (WCSS).

![Elbow Method](images/elbow_method.png)

---

## Cluster Characteristics Heatmap

Average numerical characteristics of each customer cluster.

![Cluster Characteristics](images/cluster_characteristics_heatmap.png)

---

## Average Customer Lifetime Value by Cluster

Comparison of the average Customer Lifetime Value across clusters.

![Average CLV](images/average_clv_by_cluster.png)

---

## Average Salary by Cluster

Comparison of the average salary of customers within each cluster.

![Average Salary](images/average_salary_by_cluster.png)

---

## Number of Customers in Each Cluster

Distribution of customers across all identified segments.

![Customers Per Cluster](images/customers_per_cluster.png)

---

# 💡 Business Insights

The clustering process identified five distinct customer groups with different financial characteristics and customer lifetime values.

Key observations include:

- Certain clusters contain significantly higher-value customers.
- Some customer groups generate lower lifetime value despite similar demographic characteristics.
- Salary alone does not fully explain customer value, highlighting the importance of multi-feature segmentation.
- Cluster sizes vary, providing opportunities for targeted marketing and customer retention strategies.

---

# 📈 Business Recommendations

Based on the identified customer segments, businesses can:

- Develop personalized marketing campaigns for each customer segment.
- Prioritize retention efforts for high-value customers.
- Design loyalty programs tailored to premium customer groups.
- Offer promotional campaigns to increase engagement among lower-value customers.
- Improve marketing efficiency by targeting customers according to their segment characteristics.

---

# 📂 Repository Structure

```text
Customer-Segmentation-Analysis/
│
├── notebooks/
│   └── customer_segmentation_analysis.ipynb
│
├── data/
│   └── Customer Segmentation.csv
│
├── images/
│   ├── average_clv_by_cluster.png
│   ├── average_salary_by_cluster.png
│   ├── cluster_characteristics_heatmap.png
│   ├── elbow_method.png
│   └── customers_per_cluster.png
│
├── app/                 # Planned
├── models/              # Planned
│
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

# 🚀 Future Roadmap

The project will continue evolving through the following milestones:

### Version 2

- Improve feature engineering.
- Compare K-Means with additional clustering algorithms.
- Improve cluster profiling.
- Optimize model performance.

### Version 3

- Develop an interactive Streamlit web application.
- Enable customer data upload for segmentation.
- Deploy the application to the cloud.
- Improve documentation and testing.
- Build a production-ready customer segmentation tool.

---

# 💼 Skills Demonstrated

- Data Cleaning
- Data Quality Assessment
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Scaling
- Unsupervised Machine Learning
- K-Means Clustering
- Cluster Evaluation
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

Navigate to the project directory:

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

Open the notebook:

```text
notebooks/customer_segmentation_analysis.ipynb
```

---

# 📌 Project Evolution

This project is being developed iteratively.

### ✅ Current Release

- Data preprocessing
- Exploratory Data Analysis
- Feature Engineering
- K-Means Clustering
- Customer Segmentation
- Business Insights

### 🚧 Next Release

- Enhanced clustering workflow
- Improved feature engineering
- Additional algorithm comparison

### 🚀 Final Goal

A fully deployed machine learning web application that enables users to upload customer data, generate customer segments, and visualize insights interactively.

---

# 👨‍💻 Author

**Bangaly Sano**

📧 **Email:** sanobangaly@hotmail.com

🔗 **LinkedIn:** https://linkedin.com/in/sano-bangaly-064535146

💻 **GitHub:** https://github.com/Bangaly-DS

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. Feedback, suggestions, and contributions are always welcome.