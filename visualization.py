import numpy as np
from scipy.interpolate import griddata
import plotly.graph_objects as go

def plot_iv_surface(options_df, y_axis_option, spot_price):
    options_df['impliedVolatility'] *= 100
    options_df.sort_values('strike', inplace=True)
    options_df['moneyness'] = options_df['strike'] / spot_price

    if y_axis_option == 'Strike Price ($)':
        Y = options_df['strike'].values
        y_label = 'Strike Price ($)'
    else:
        Y = options_df['moneyness'].values
        y_label = 'Moneyness (Strike / Spot)'

    X = options_df['timeToExpiration'].values
    Z = options_df['impliedVolatility'].values

    ti = np.linspace(X.min(), X.max(), 50)
    ki = np.linspace(Y.min(), Y.max(), 50)
    T, K = np.meshgrid(ti, ki)

    Zi = griddata((X, Y), Z, (T, K), method='linear')
    Zi = np.ma.array(Zi, mask=np.isnan(Zi))

    fig = go.Figure(data=[go.Surface(
        x=T, y=K, z=Zi,
        colorscale='Viridis',
        colorbar_title='Implied Volatility (%)'
    )])

    fig.update_layout(
        title=f'Implied Volatility Surface',
        scene=dict(
            xaxis_title='Time to Expiration (years)',
            yaxis_title=y_label,
            zaxis_title='Implied Volatility (%)'
        ),
        autosize=False,
        width=900,
        height=800,
        margin=dict(l=65, r=50, b=65, t=90)
    )
    return fig
