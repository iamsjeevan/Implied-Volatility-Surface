# Implied Volatility Surface

This is a **Streamlit** application that visualizes the implied volatility surface of options for a given stock or ETF. The app fetches live options data from Yahoo Finance using the `yfinance` library, calculates implied volatility using the Black-Scholes model, and visualizes the volatility surface in an interactive 3D plot using `Plotly`.

## Features

- Fetch live options data for any stock or ETF from Yahoo Finance.
- Calculate the implied volatility of options based on the Black-Scholes model.
- Visualize the implied volatility surface as a 3D graph.
- Customizable parameters for **Risk-Free Rate** and **Dividend Yield**.
- Filter options by **Strike Price** based on the percentage of the spot price.
- Choose between plotting the implied volatility surface with respect to **Strike Price** or **Moneyness**.

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/iamsjeevan/Implied-Volatility-Surface.git
cd Implied-Volatility-Surface
```
### 2. Set up a Virtual Environment
It's recommended to create a virtual environment to manage dependencies. You can do this by running the following:
