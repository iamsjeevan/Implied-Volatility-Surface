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
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate

```
On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
### 3. Install the Required Dependencies
After activating the virtual environment, install the necessary libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
### 4. Run the Application
Once the dependencies are installed, you can start the Streamlit app by running:

```bash

streamlit run app.py
```
This will open the app in your web browser, where you can interact with the implied volatility surface.
## Usage

This Streamlit app visualizes the implied volatility surface for options based on the Black-Scholes model. To use the app, follow the steps below:

### 1. **Risk-Free Rate**:
Set the **Risk-Free Interest Rate** (e.g., `0.015` for 1.5%). This parameter is used in the Black-Scholes model to calculate the theoretical value of options.

### 2. **Dividend Yield**:
Set the **Dividend Yield** (e.g., `0.013` for 1.3%). This is the dividend rate expected by the underlying asset, which is used to adjust the option pricing model.

### 3. **Strike Price Filter**:
Filter options by the **Minimum** and **Maximum Strike Price** percentages relative to the **Spot Price**. For example, you can set the minimum strike price to `80%` and the maximum to `120%` of the current spot price of the underlying asset. This helps focus the analysis on options that are close to the current market price.

### 4. **Ticker Symbol**:
Enter the **Ticker Symbol** of the asset (e.g., `SPY` for the S&P 500 ETF). The app will fetch the relevant options data for this symbol from Yahoo Finance.

### 5. **Y-Axis Option**:
Choose the **Y-Axis Option**:
- **Strike Price ($)**: Visualize the volatility surface using the strike price of the options.
- **Moneyness**: Visualize the volatility surface using the moneyness of the options, which is calculated as the strike price divided by the spot price.

Once these parameters are set, the app fetches the relevant options data from Yahoo Finance, computes the implied volatility for each option using the Black-Scholes model, and then displays the results as a 3D surface plot. This plot represents how implied volatility varies with time to expiration and strike price (or moneyness).

The interactive chart allows you to explore the implied volatility surface for different assets and their options, helping you make informed decisions on option strategies.




