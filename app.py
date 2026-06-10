import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import os

print("Current working directory:")
print(os.getcwd())

app = dash.Dash(__name__)

# Load data with error handlingpython app.py
try:
    inflation = pd.read_csv("data/inflation.csv")
    gdp = pd.read_csv("data/gdp.csv")
    exchange = pd.read_csv("data/exchange_rates.csv")
    
    print("✅ Data loaded successfully!")
    print("Inflation columns:", inflation.columns.tolist())
    print("GDP columns:", gdp.columns.tolist())
    print("Exchange columns:", exchange.columns.tolist())
    
except Exception as e:
    print(f"❌ Error loading data: {e}")
    raise

# Create figures

inflation_fig = px.line(
    inflation,
    x="Year",
    y="Inflation",
    markers=True,
    title="Inflation Trend"
)

gdp_fig = px.bar(
    gdp,
    x="Year",
    y="GDPGrowth",
    title="GDP Growth"
)

exchange_fig = px.line(
    exchange,
    x="Year",
    y="USDUGX",
    markers=True,
    title="USD/UGX Exchange Rate"
)

print("Charts created successfully!")

exchange_fig = px.line(
    exchange,
    x="Year",
    y="USDUGX",
    markers=True,
    title="USD/UGX Exchange Rate"
)

app.layout = html.Div([

    html.H1(
        "🇺🇬 Uganda Economic Intelligence Dashboard",
        style={"textAlign": "center"}
    ),

    html.Div([

        html.Div([
            html.H3("Inflation"),
            html.H2("3.8%")
        ], className="card"),

        html.Div([
            html.H3("GDP Growth"),
            html.H2("6.3%")
        ], className="card"),

        html.Div([
            html.H3("USD/UGX"),
            html.H2("3675")
        ], className="card")

    ], className="cards"),

    dcc.Graph(figure=inflation_fig),
    dcc.Graph(figure=gdp_fig),
    dcc.Graph(figure=exchange_fig)

])

print("Charts created successfully!")

if __name__ == "__main__":
    app.run(debug=True)

# Dynamic cards (