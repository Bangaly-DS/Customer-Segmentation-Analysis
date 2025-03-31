# ✈️ Customer Segmentation Analysis  
Customer segmentation using K-means clustering on Airline Loyalty Program data

## 📌 Project Overview  
This project analyzes customer data from an **Airline Loyalty Program** to segment customers based on financial and behavioral attributes using **K-Means clustering**. The goal is to help businesses understand their customer base and improve targeted marketing strategies.  

---

## 📊 Dataset  
The dataset contains customer information, including:  
- **Customer Lifetime Value (CLV)**  
- **Salary**  
- **Loyalty Card Type**  
- **Marital Status**  

This data was cleaned, visualized, and analyzed before applying clustering techniques.  

---

## 🎯 Objective  
The aim of this project is to classify customers into meaningful **segments (clusters)** to optimize marketing campaigns and customer engagement strategies.  

---

## 📌 Steps in the Analysis  
### **1️⃣ Data Cleaning & Preprocessing**  
- Checked for **missing values** and handled them.  
- Detected and treated **outliers** in the dataset.  
- Converted categorical variables for better analysis.  

### **2️⃣ Exploratory Data Analysis (EDA)**  
- Visualized **gender, marital status, salary, and loyalty card type** distributions.  
- Used **correlation heatmaps** to identify relationships between features.  
- Analyzed **outliers in salary distribution**.  

### **3️⃣ Clustering Process**  
- Selected **CLV** and **Salary** as clustering features.  
- Standardized the data using **StandardScaler**.  
- Used the **Elbow Method** to determine the optimal number of clusters (**K=3**).  
- Applied **K-Means Clustering** and analyzed customer segments.  

### **4️⃣ Key Insights**  
- **Cluster 0 (Low CLV & Salary)** → Budget-conscious or occasional customers.  
- **Cluster 1 (Mid-range CLV & Salary)** → Regular customers with moderate spending.  
- **Cluster 2 (High CLV & Salary)** → High-value premium customers.  
- **Loyalty Card Type** was distributed unevenly across clusters, revealing customer preferences.  

---

## 📈 Results & Business Implications  
This segmentation helps businesses:  
✅ **Target Cluster 0** with discounts and promotions.  
✅ **Engage Cluster 1** with personalized offers.  
✅ **Retain Cluster 2** with loyalty rewards and premium services.  

---

## 🔧 How to Run the Code  
1️⃣ **Clone this repository:**  
```bash
git clone https://github.com/Bangaly-DS/Customer-Segmentation-Analysis.git
cd Customer-Segmentation-Analysis
