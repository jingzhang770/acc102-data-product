markdown
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
```
## 6. Product Link / Demo

```bash
- **Interactive Tool (Streamlit App)**: [One-Click Financial Health Analysis Tool](https://acc102-data-appuct-hybvd7svi6dnfyxhvvnemb.streamlit.app)
- **Demo Video**: [Watch on Bilibili](https://b23.tv/vBroZfW)
- **Source Code Repository**: [GitHub - jingzhang770/acc102-data-product](https://github.com/jingzhang770/acc102-data-product)
```
## 7. Key Insights from Microsoft (MSFT) Analysis

- Microsoft's debt ratio decreased from 64% in 2019 to 48% in 2024, showing improved financial stability
- ROE remained above 30% for all six years, far exceeding the 15% excellent threshold
- Net profit margin stayed consistently above 30%, reaching 36% in 2024
- Revenue grew from $126B (2019) to $245B (2024), net income from $39B to $88B
- Health score remained stable at 75/100 (Excellent rating) across all 6 years
- The company shows strong profitability, efficient asset utilization, and improving leverage

## 8. Limitations

- Analysis covers only 6 years (2019-2024); longer trends require more data
- Scoring model weights are simplified and not statistically validated
- Industry differences are not considered (e.g., tech companies typically have higher debt)
- Cash flow indicators (operating cash flow, free cash flow) are not included
- WRDS database requires institutional access

## 9. Future Improvements

- Add cash flow analysis (CFO, FCF)
- Compare results with industry averages
- Add predictive models (e.g., Altman Z-score)
- Support for non-US companies
- Add more years of historical data
- Allow users to upload their own CSV files

## 10. AI Disclosure
This project used AI tools to support the development process:
- ACC102Tutor_DS_V3.2：import matplotlib and configure font settings；sql query suggestions；generate financial analysis charts and report
- Deepseek：markdown suggestions；code correction and improvement
**Declaration**:AI tools were used only for coding assistance and documentation formatting.

## 11. References

- WRDS Compustat Database
- CRSP Stock Database
- Streamlit Community Cloud
- Python Libraries: pandas, matplotlib, openpyxl

## 12. Author

- **Name**: Jing Zhang
- **Course**: ACC102
- **Assignment**: Mini Assignment 
- **Track**: Track 4
- **Date**: April 2026







