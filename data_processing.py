import yfinance as yf
import pandas as pd
from datetime import timedelta

def fetch_option_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    today = pd.Timestamp('today').normalize()

    try:
        expirations = ticker.options
        exp_dates = [pd.Timestamp(exp) for exp in expirations if pd.Timestamp(exp) > today + timedelta(days=7)]
    except Exception as e:
        return None, None, None

    option_data = []

    for exp_date in exp_dates:
        try:
            opt_chain = ticker.option_chain(exp_date.strftime('%Y-%m-%d'))
            calls = opt_chain.calls
        except Exception:
            continue

        calls = calls[(calls['bid'] > 0) & (calls['ask'] > 0)]
        for _, row in calls.iterrows():
            option_data.append({
                'expirationDate': exp_date,
                'strike': row['strike'],
                'bid': row['bid'],
                'ask': row['ask'],
                'mid': (row['bid'] + row['ask']) / 2
            })

    option_df = pd.DataFrame(option_data)
    option_df['daysToExpiration'] = (option_df['expirationDate'] - today).dt.days
    option_df['timeToExpiration'] = option_df['daysToExpiration'] / 365
    return option_df, exp_dates, today

def fetch_spot_price(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    try:
        spot_history = ticker.history(period='5d')
        if not spot_history.empty:
            return spot_history['Close'].iloc[-1]
    except Exception:
        return None
