import streamlit as st
from datetime import timedelta
import pandas as pd
import numpy as np
from bs_model import bs_call_price, implied_volatility
from data_processing import fetch_option_data, fetch_spot_price
from visualization import plot_iv_surface

st.title('Implied Volatility Surface')

# Sidebar: Input parameters
st.sidebar.header('Model Parameters')
risk_free_rate = st.sidebar.number_input('Risk-Free Rate', value=0.015, format="%.4f")
dividend_yield = st.sidebar.number_input('Dividend Yield', value=0.013, format="%.4f")

st.sidebar.header('Visualization Parameters')
y_axis_option = st.sidebar.selectbox('Select Y-axis:', ('Strike Price ($)', 'Moneyness'))

st.sidebar.header('Ticker Symbol')
ticker_symbol = st.sidebar.text_input('Enter Ticker Symbol', value='SPY', max_chars=10).upper()

st.sidebar.header('Strike Price Filter Parameters')
min_strike_pct = st.sidebar.number_input(
    'Minimum Strike Price (% of Spot Price)',
    min_value=50.0,
    max_value=199.0,
    value=80.0,
    step=1.0,
    format="%.1f"
)

max_strike_pct = st.sidebar.number_input(
    'Maximum Strike Price (% of Spot Price)',
    min_value=51.0,
    max_value=200.0,
    value=120.0,
    step=1.0,
    format="%.1f"
)
if min_strike_pct >= max_strike_pct:
    st.sidebar.error('Min strike % must be less than max strike %.')
    st.stop()

# Fetch data
option_data, exp_dates, today = fetch_option_data(ticker_symbol)
if option_data is None:
    st.error(f"No option data available for {ticker_symbol}.")
    st.stop()

# Get spot price
spot_price = fetch_spot_price(ticker_symbol)
if spot_price is None:
    st.error(f"Failed to retrieve spot price for {ticker_symbol}.")
    st.stop()

# Filter options data
option_data = option_data[
    (option_data['strike'] >= spot_price * (min_strike_pct / 100)) &
    (option_data['strike'] <= spot_price * (max_strike_pct / 100))
]
option_data.reset_index(drop=True, inplace=True)

# Calculate implied volatility
with st.spinner('Calculating implied volatility...'):
    option_data['impliedVolatility'] = option_data.apply(
        lambda row: implied_volatility(
            row['mid'], spot_price, row['strike'], row['timeToExpiration'], risk_free_rate, dividend_yield
        ), axis=1
    )
option_data.dropna(subset=['impliedVolatility'], inplace=True)

# Plot the implied volatility surface
fig = plot_iv_surface(option_data, y_axis_option, spot_price)
st.plotly_chart(fig)

st.write("---")
st.markdown("Created by Jeevan s  |")