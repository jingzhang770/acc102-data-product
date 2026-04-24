import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page configuration
st.set_page_config(page_title="Financial Health Analyzer", layout="wide")
st.title("📊 One-Click Financial Health Analysis Tool for Listed Companies")
st.markdown("---")

# Sidebar
st.sidebar.header("Company Selection")

# Get list of available CSV files
csv_files = [f.replace('_data.csv', '') for f in os.listdir('.') if f.endswith('_data.csv')]

if csv_files:
    ticker = st.sidebar.selectbox("Select Stock Ticker", csv_files)
else:
    st.sidebar.warning("No data files found")
    ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL").upper()

st.sidebar.markdown("---")
st.sidebar.info("📌 Data source: WRDS Compustat (2019-2024)")

# Function to calculate financial ratios
def calculate_ratios(df):
    df = df.copy()
    df['debt_ratio'] = df['total_liabilities'] / df['total_assets']
    df['ROE'] = df['net_income'] / df['total_equity']
    df['net_profit_margin'] = df['net_income'] / df['revenue']
    df['asset_turnover'] = df['revenue'] / df['total_assets']
    return df

# Function to calculate health score
def add_health_score(df):
    df = df.copy()
    scores = []
    for i in range(len(df)):
        row = df.iloc[i]
        score = 0
        
        # Debt ratio scoring (30%-60% is healthy)
        if 0.3 <= row['debt_ratio'] <= 0.6:
            score += 35
        elif row['debt_ratio'] < 0.3:
            score += 20
        else:
            score += 10
        
        # ROE scoring (>15% is excellent)
        if row['ROE'] > 0.15:
            score += 35
        elif row['ROE'] > 0.10:
            score += 25
        else:
            score += 15
        
        # Net profit margin scoring (>10% is excellent)
        if row['net_profit_margin'] > 0.10:
            score += 30
        else:
            score += 15
        
        scores.append(score)
    
    df['health_score'] = scores
    return df

# Function to create charts
def create_charts(df, ticker):
    years = df['year'].tolist()
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle(f'{ticker} Financial Health Analysis (2019-2024)', fontsize=14, fontweight='bold')
    
    # Chart 1: Debt Ratio
    axes[0,0].plot(years, df['debt_ratio'], 'bo-')
    axes[0,0].axhline(y=0.5, color='r', linestyle='--', label='Warning 50%')
    axes[0,0].fill_between(years, 0.3, 0.6, alpha=0.2, color='green')
    axes[0,0].set_title('Debt Ratio')
    axes[0,0].set_ylabel('Ratio')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # Chart 2: ROE
    axes[0,1].plot(years, df['ROE'], 'gs-')
    axes[0,1].axhline(y=0.15, color='r', linestyle='--', label='Excellent 15%')
    axes[0,1].set_title('Return on Equity (ROE)')
    axes[0,1].set_ylabel('Ratio')
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    
    # Chart 3: Net Profit Margin
    axes[0,2].plot(years, df['net_profit_margin'], 'ro-')
    axes[0,2].axhline(y=0.10, color='g', linestyle='--', label='Excellent 10%')
    axes[0,2].set_title('Net Profit Margin')
    axes[0,2].set_ylabel('Ratio')
    axes[0,2].legend()
    axes[0,2].grid(True, alpha=0.3)
    
    # Chart 4: Asset Turnover
    axes[1,0].plot(years, df['asset_turnover'], 'mD-')
    axes[1,0].axhline(y=0.8, color='r', linestyle='--', label='Baseline 0.8')
    axes[1,0].set_title('Asset Turnover')
    axes[1,0].set_ylabel('Turnover Rate')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # Chart 5: Health Score
    axes[1,1].plot(years, df['health_score'], 'ro-')
    axes[1,1].axhline(y=70, color='g', linestyle='--', label='Good 70')
    axes[1,1].axhline(y=50, color='orange', linestyle='--', label='Pass 50')
    axes[1,1].set_title('Comprehensive Health Score')
    axes[1,1].set_ylabel('Score')
    axes[1,1].set_ylim(0,100)
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    # Chart 6: Revenue vs Net Income
    x = range(len(years))
    width = 0.35
    axes[1,2].bar([i - width/2 for i in x], df['revenue']/1000, width, label='Revenue (Billions)', color='steelblue')
    axes[1,2].bar([i + width/2 for i in x], df['net_income']/1000, width, label='Net Income (Billions)', color='salmon')
    axes[1,2].set_title('Revenue vs Net Income')
    axes[1,2].set_xticks(x)
    axes[1,2].set_xticklabels(years)
    axes[1,2].set_ylabel('Amount (Billions USD)')
    axes[1,2].legend()
    axes[1,2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

# Main program
if st.sidebar.button("🚀 Run Analysis", type="primary"):
    with st.spinner(f"Loading data for {ticker}..."):
        try:
            csv_path = f'{ticker}_data.csv'
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                st.success(f"✅ Loaded data for {ticker}")
            else:
                st.error(f"❌ No data file found for {ticker}")
                st.stop()
            
            # Rename columns
            old_names = ['tic', 'fyear', 'at', 'lt', 'teq', 'sale', 'ni']
            new_names = ['ticker', 'year', 'total_assets', 'total_liabilities', 'total_equity', 'revenue', 'net_income']
            
            if all(col in df.columns for col in old_names):
                rename_dict = dict(zip(old_names, new_names))
                df = df.rename(columns=rename_dict)
            
            # Data cleaning
            df_clean = df.dropna()
            df_clean = df_clean.sort_values('year')
            
            # Calculate ratios and score
            df_ratios = calculate_ratios(df_clean)
            df_scored = add_health_score(df_ratios)
            
            # Display latest year data
            st.subheader(f"📈 Latest Year Data - {df_scored['year'].iloc[-1]}")
            
            col1, col2, col3 = st.columns(3)
            latest = df_scored.iloc[-1]
            
            with col1:
                st.metric("Revenue", f"${latest['revenue']:,.0f}M")
                st.metric("Net Income", f"${latest['net_income']:,.0f}M")
            with col2:
                st.metric("Debt Ratio", f"{latest['debt_ratio']:.1%}")
                st.metric("ROE", f"{latest['ROE']:.1%}")
            with col3:
                st.metric("Net Profit Margin", f"{latest['net_profit_margin']:.1%}")
                score = latest['health_score']
                if score >= 70:
                    st.success(f"Health Score: {score:.0f}/100 ✅")
                elif score >= 50:
                    st.warning(f"Health Score: {score:.0f}/100 ⚠️")
                else:
                    st.error(f"Health Score: {score:.0f}/100 ❌")
            
            # Display data table
            with st.expander("📊 View Complete Data Table"):
                st.dataframe(df_scored)
            
            # Display charts
            st.subheader("📉 Trend Analysis Charts")
            fig = create_charts(df_scored, ticker)
            st.pyplot(fig)
            
            # Comprehensive evaluation
            st.subheader("📋 Comprehensive Evaluation")
            if score >= 70:
                st.success("✅ Excellent - The company has a healthy financial condition with strong profitability and solvency")
            elif score >= 50:
                st.warning("⚠️ Average - Financial condition is moderate, recommend monitoring key indicators")
            else:
                st.error("❌ Caution - Financial condition requires attention, recommend in-depth analysis")
            
            # Download button
            excel_file = f'{ticker}_analysis_results.xlsx'
            df_scored.to_excel(excel_file, index=False)
            with open(excel_file, 'rb') as f:
                st.download_button(
                    label="📥 Download Excel Report",
                    data=f,
                    file_name=excel_file,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
