

# Customer Segmentation using RFM Analysis and KMeans Clustering
---

## Project Overview

This project implements an end-to-end customer segmentation system using real-world e-commerce transaction data. The objective is to segment customers based on their purchasing behavior using RFM (Recency, Frequency, Monetary) analysis and KMeans clustering.

The output helps businesses identify valuable customers, at-risk customers, and inactive customers to improve marketing strategies and customer retention.

---

## Dataset Information

* Dataset: Online Retail II
* Source: UCI Machine Learning Repository
* Type: Real-world e-commerce transaction data
* Time Period: 2009–2011
* Records: ~1 million transactions
* Description: Contains invoice-level transaction data including product details, quantity, price, customer ID, and country.

---

## Problem Statement

Businesses need to understand customer behavior to improve targeting and retention. This project addresses:

* Identifying high-value customers
* Detecting churn-risk customers
* Understanding purchase behavior patterns
* Segmenting customers for targeted marketing

---

## Project Workflow

### 1. Data Loading

Loaded raw transactional dataset from Excel format.

### 2. Data Cleaning

* Removed missing Customer ID values
* Removed duplicate records
* Handled invalid transactions (negative quantity and zero price)

### 3. Exploratory Data Analysis (EDA)

* Sales trends over time
* Country-wise revenue analysis
* Customer purchase behavior
* Distribution of spending and order frequency

### 4. Feature Engineering (RFM)

Created customer-level features:

* Recency: Days since last purchase
* Frequency: Number of unique purchases
* Monetary: Total spending

### 5. Data Preprocessing

* Outlier handling using IQR method
* Log transformation to reduce skewness
* Standard scaling for normalization

### 6. Clustering Model

* Applied KMeans clustering
* Optimal number of clusters selected using Elbow Method and Silhouette Score

### 7. Customer Segmentation

Customers grouped into business segments:

* Champions
* Loyal Customers
* At Risk Customers
* Lost Customers

### 8. SQL Integration

* Stored final dataset in SQLite database
* Used SQL queries for segment-level analysis

### 9. Data Visualization

* Plotly-based visualizations for cluster interpretation
* RFM distribution analysis
* Segment-wise comparisons

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Plotly
* SQLite (SQL integration)
* Jupyter Notebook

---

## Repository Structure

```
Customer-Segmentation-Project/
│
├── Customer_Segmentation_Notebook.ipynb   # Main analysis notebook
├── customer_segments.db                   # SQLite database (final data)
├── customer_segments_final.csv            # Final dataset with segments
├── requirements.txt                       # Project dependencies
└── README.md                              # Project documentation
```

---

## Key Insights

* A small percentage of customers contribute most of the revenue
* Recency is a strong indicator of customer churn risk
* Frequency and Monetary define customer loyalty
* Customer segmentation enables targeted marketing strategies

---

## Project Outcome

* Built an end-to-end customer segmentation pipeline
* Transformed raw transactional data into actionable business insights
* Applied unsupervised machine learning (KMeans clustering)
* Created interpretable customer segments for business use
* Integrated SQL for structured data storage and querying

---


## Future Improvements

* Deploy using Streamlit for real-time prediction
* Experiment with DBSCAN or Hierarchical clustering
* Add Customer Lifetime Value (CLV) modeling
* Build interactive Power BI dashboard

---

## Dataset Credit

Online Retail II Dataset
UCI Machine Learning Repository
Licensed under CC BY 4.0


