# Walmart Sales Data Pipeline & SQL Analytics

An end-to-end data engineering and business analytics project that automates retail dataset ingestion from Kaggle, performs data cleaning and feature engineering in Python, loads structured records into MySQL, and answers core business questions using advanced SQL window functions.

---

## 🛠️ Tech Stack & Tools
* **Programming & ETL:** Python (Pandas, SQLAlchemy, PyMySQL)
* **Database:** MySQL
* **Data Source:** Kaggle API (Walmart 10K Sales Dataset)
* **Development Environment:** VS Code, Virtualenv

---

## 📊 Pipeline Architecture & Workflow
1. **Automated Extraction:** Downloaded the dataset using the Kaggle API.
2. **Data Cleaning & Preprocessing:**
   * Removed currency symbols (`$`) from monetary fields and converted them to numerical data types.
   * Handled null values and standardized column casing.
3. **Feature Engineering:**
   * Calculated `total` (`unit_price * quantity`) and `profit` (`total * profit_margin`).
   * Parsed timestamps into `hour` and categorized sales into shifts (`Morning`, `Afternoon`, `Evening`).
4. **Database Ingestion:** Migrated the transformed dataset into MySQL using SQLAlchemy 2.0.
5. **Business Intelligence:** Authored optimized SQL queries using Common Table Expressions (CTEs) and `RANK() OVER (PARTITION BY ...)` to uncover branch-level insights.

---

## 💡 Key Business Questions Solved
* Identified the highest-rated product category for every store branch.
* Determined peak sales days (busiest transaction days) across branches.
* Analyzed branch payment preferences across credit card, cash, and digital wallets.
* Evaluated aggregate revenue and profitability across all product categories.
* Assessed shift-wise performance to isolate high-volume operational hours.

---

## 🚀 How to Run
1. Clone repository:
   ```bash
   git clone [https://github.com/SaloniSingh2004/walmart-sales-analysis.git](https://github.com/SaloniSingh2004/walmart-sales-analysis.git)
   cd walmart-sales-analysis