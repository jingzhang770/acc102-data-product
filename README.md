# acc102-data-product
# Listed Company Financial Health Analysis Tool

## 1. Problem & User

This tool helps retail investors and financial analysts quickly evaluate a company's financial health by analyzing key financial ratios and generating a comprehensive health score (0-100).

## 2. Data

- **Source**: WRDS (Wharton Research Data Services) - Compustat and CRSP databases
- **Access Date**: April 22, 2026
- **Key Fields**: 
  - Financial data: total assets (at), total liabilities (lt), shareholders' equity (teq), revenue (sale), net income (ni)
  - Stock data: monthly closing price (prc), monthly return (ret)
 
## 3. Methods

- **Data Acquisition**: SQL queries to WRDS Compustat (financial statements) and CRSP (stock prices)
- **Data Cleaning**: Remove missing values, rename columns, sort by year
- **Ratio Calculation**: Debt ratio, ROE, net profit margin, asset turnover, equity multiplier
- **Health Score Model**: Weighted scoring (35 pts debt ratio + 35 pts ROE + 30 pts net margin)
- **Visualization**: 6-in-1 trend charts (Matplotlib)
- **Export**: Excel file with all calculated ratios

## 4. Key Findings (Example: AAPL 2019-2024)

- Apple's debt ratio remained high (73%-86%), above the 60% warning level
- ROE showed strong performance (61%-197%), far exceeding the 15% excellent threshold
- Net profit margin stayed healthy (21%-26%), above 10% excellent line
- Health score remained stable at 75/100 (Excellent rating) across all 6 years
- Revenue grew from $260B (2019) to $391B (2024), net income from $55B to $94B

## 5. How to Run

```bash
# Install dependencies
pip install wrds pandas matplotlib openpyxl

# Run the Jupyter notebook
jupyter notebook "Analysis report on the financial health of listed companies.ipynb"

# When prompted, enter WRDS username and stock ticker (e.g., AAPL)












