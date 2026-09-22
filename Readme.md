# Walmart Sales Analysis & Power BI Dashboard

An end-to-end retail data analytics project that uses Python, MySQL, SQL, and Power BI to clean, transform, analyze, and visualize Walmart sales data.

The project follows a complete analytics workflow:

**Raw Sales Data → Python Data Cleaning → MySQL → SQL Analysis → Power BI Dashboard → Business Insights**

---

## 📌 Project Overview

This project analyzes Walmart sales data to understand sales performance, profitability, customer purchasing behavior, branch-level performance, product categories, payment methods, and sales patterns across different time periods.

The project combines data preprocessing and feature engineering in Python with SQL-based business analysis and interactive Power BI dashboards.

The objective is to transform raw transactional data into structured information that can be used to answer practical business questions and support data-driven decision-making.

---

## 🎯 Objectives

The main objectives of this project are:

- Clean and prepare raw Walmart sales data for analysis.
- Standardize inconsistent column names and data types.
- Handle missing values and invalid data.
- Create calculated fields such as total sales and profit.
- Transform date and time information into useful analytical features.
- Store the processed dataset in MySQL.
- Use SQL to answer business-related analytical questions.
- Analyze sales and profitability across product categories and branches.
- Analyze customer payment preferences.
- Identify sales patterns across different time shifts.
- Build an interactive Power BI dashboard for visual analysis.
- Present business information through clear KPIs and visualizations.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data cleaning and preprocessing |
| Pandas | Data manipulation and transformation |
| SQLAlchemy | Python-to-MySQL database connectivity |
| PyMySQL | MySQL database connection |
| MySQL | Data storage and SQL analysis |
| SQL | Business analysis and querying |
| Power BI | Interactive dashboards and visualization |
| DAX | Power BI calculations and measures |
| Git | Version control |
| GitHub | Project repository and version management |
| VS Code | Development environment |

---

## 🔄 Project Workflow

```text
                    Walmart Sales Dataset
                            │
                            ▼
                    Python / Pandas
                            │
                Data Cleaning & Processing
                            │
                            ▼
                         MySQL
                            │
                    SQL Business Analysis
                            │
                            ▼
                       Power BI
                            │
              Interactive Dashboards
                            │
                            ▼
                   Business Insights


📂 Dataset

The project uses a Walmart sales dataset containing transactional information related to sales, products, branches, customers, payment methods, ratings, dates, and times.

The dataset contains fields used for analysis such as:

Invoice ID
Branch
City
Customer Type
Gender
Product Line
Unit Price
Quantity
Tax
Total
Date
Time
Payment Method
Cost of Goods Sold
Gross Margin Percentage
Gross Income
Rating

The raw dataset is processed before being used for SQL analysis and Power BI visualization.

🧹 Data Cleaning & Preprocessing

Python is used to prepare the raw dataset before loading it into MySQL.

The preprocessing pipeline performs the following operations:

1. Column Standardization

Column names are stripped of unnecessary spaces and converted into lowercase names using underscores.

Example:

Unit Price → unit_price
Product line → product_line
2. Currency Conversion

Currency symbols are removed from monetary fields and the values are converted into numerical data types.

3. Missing Value Handling

Rows containing missing values are removed from the working dataset.

4. Total Sales Calculation

A total field is calculated using:

total = unit_price × quantity
5. Profit Calculation

A profit field is created using:

profit = total × profit_margin
6. Date Transformation

The date field is converted into a proper datetime format for analysis.

7. Hour Extraction

The transaction time is converted into an hour value.

8. Shift Classification

Transactions are grouped into three time periods:

Morning
Afternoon
Evening

These transformations make the dataset easier to analyze in both SQL and Power BI.

🗄️ MySQL Database

After preprocessing, the transformed dataset is loaded into a MySQL database.

The database used in the project is:

walmart_db

The processed sales data is stored in:

walmart_sales

Python uses SQLAlchemy and PyMySQL to establish the connection between the data-processing pipeline and MySQL.

📊 SQL Analysis

The project contains SQL queries designed to answer practical business questions.

1. Highest-Rated Product Category by Branch

The analysis uses RANK() with partitioning to identify the highest-rated product category for each branch.

RANK() OVER (
    PARTITION BY branch
    ORDER BY AVG(rating) DESC
)

This allows category ratings to be compared separately within each branch.

2. Busiest Day for Each Branch

The transaction count is grouped by branch and day of the week.

The query ranks the days according to the number of transactions and identifies the busiest day for each branch.

3. Most Common Payment Method

Payment methods are grouped by branch and ranked according to transaction count.

This helps identify the most frequently used payment method at each branch.

4. Revenue and Profit by Product Category

The project calculates aggregate revenue and profit for each product category.

SUM(total) AS total_revenue
SUM(profit) AS total_profit

The categories are then ordered according to profitability.

5. Sales by Time Shift

Sales transactions are grouped into:

Morning
Afternoon
Evening

The analysis calculates transaction volume and revenue for each shift.

This provides a view of when sales activity is highest during the day.

📈 Power BI Dashboard

The processed sales data is visualized through an interactive Power BI dashboard.

The dashboard focuses on sales performance, operational analysis, and profitability.

Dashboard 1 — Walmart Sales Analysis

The sales analysis dashboard provides an overview of Walmart sales performance through interactive visualizations and business KPIs.

It allows sales information to be explored across different business dimensions such as branches, products, categories, payment methods, and time periods.

Dashboard 2 — Operational & Profitability Analysis

The second dashboard focuses on operational and profitability-related analysis.

It provides visual information that can be used to compare performance across different branches, categories, and operational dimensions.

🔍 Key Business Questions

The project is designed to answer questions such as:

Which product categories have the highest ratings in each branch?
Which days generate the highest number of transactions?
What payment method is most commonly used in each branch?
Which product categories generate the most revenue?
Which product categories generate the most profit?
How are sales distributed across different time shifts?
Which branches and categories show stronger sales performance?
How does operational activity vary throughout the day?
What patterns can be identified from the sales data?
📌 Key Analytical Areas
Sales Performance

Sales are analyzed across product categories, branches, and time periods to understand overall transaction and revenue patterns.

Profitability

Revenue and calculated profit are compared across product categories to understand their financial contribution.

Branch Analysis

Branch-level analysis is used to compare ratings, transaction patterns, payment preferences, and sales activity.

Payment Analysis

Payment methods are analyzed to identify the most frequently used payment option across branches.

Time-Based Analysis

Transaction time is converted into hour and shift-based features to analyze sales activity across Morning, Afternoon, and Evening periods.

📁 Repository Structure
walmart-sales-analysis/
│
├── Assets/
│   ├── Walmart_Sales_Analysis.png
│   └── Operational_Profitability_Analysis.png
│
├── Walmart Data Analysis.pbix
├── pipeline.py
├── queries.sql
├── requirements.txt
├── .gitignore
└── README.md
📄 File Description
pipeline.py

Python data-processing pipeline responsible for:

Loading the sales dataset.
Cleaning column names.
Converting monetary fields.
Handling missing values.
Creating total sales and profit fields.
Extracting transaction hours.
Creating sales shifts.
Loading the processed data into MySQL.
queries.sql

Contains SQL queries for:

Branch-level category rating analysis.
Busiest day analysis.
Payment method analysis.
Category revenue and profit analysis.
Shift-wise sales analysis.

The queries use SQL aggregation, CTEs, grouping, ranking, and window functions.

Walmart Data Analysis.pbix

Power BI project file containing the interactive sales analysis and operational/profitability dashboards.

Assets/

Contains dashboard screenshots used to display the Power BI visualizations directly in this README.

requirements.txt

Contains the Python dependencies used by the data-processing pipeline.

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/SaloniSingh2004/walmart-sales-analysis.git

Move into the project directory:

cd walmart-sales-analysis
2. Create a Virtual Environment
python -m venv venv

Activate the environment.

Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Set Up MySQL

Create the database:

CREATE DATABASE walmart_db;

Then make sure MySQL is running locally.

Update the database connection configuration in pipeline.py using your own local credentials.

Do not commit database passwords or other credentials to GitHub.

5. Prepare the Dataset

Place the Walmart sales CSV file in the project directory using the filename expected by the pipeline:

walmart.csv

The Python pipeline reads this file and performs the required preprocessing.

6. Run the Data Pipeline
python pipeline.py

The processed data will be loaded into the MySQL table:

walmart_sales
7. Run the SQL Analysis

Open:

queries.sql

in MySQL Workbench or another MySQL client.

Execute the queries after the walmart_sales table has been created.

8. Open the Power BI Dashboard

Open:

Walmart Data Analysis.pbix

in Microsoft Power BI Desktop.

Connect or refresh the dataset as required by your local setup.

📊 Dashboard Features

The Power BI dashboard is designed to provide an interactive view of Walmart sales data.

The analysis covers areas including:

Sales performance
Revenue
Profitability
Branch performance
Product category analysis
Transaction patterns
Payment methods
Time-based sales activity
Operational performance

The dashboard can be used to filter and explore different aspects of the sales dataset.

🧠 Analytical Techniques Used

The project applies several common data analytics techniques:

Data cleaning
Data preprocessing
Feature engineering
Aggregation
Group-by analysis
Time-based analysis
Ranking
Common Table Expressions (CTEs)
SQL window functions
Business KPI analysis
Interactive data visualization
🔐 Security Note

Database credentials should never be stored directly in source code or committed to a public repository.

For local development, credentials can be stored using environment variables.

Example:

DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=walmart_db

A .env file containing real credentials should be added to .gitignore.

📌 Future Improvements

Possible improvements to the project include:

Automating the data-refresh process.
Adding additional Power BI pages.
Adding more advanced DAX measures.
Adding year-over-year and month-over-month analysis.
Adding customer segmentation.
Adding forecasting for future sales.
Adding automated data-quality checks.
Connecting Power BI directly to a production database.
Deploying the dashboard through Power BI Service.
👩‍💻 Author

Saloni Singh

GitHub:
https://github.com/SaloniSingh2004