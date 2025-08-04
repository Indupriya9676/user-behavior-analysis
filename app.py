import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/cleaned_logs/part-00000.csv", header=None, names=["timestamp", "user_id", "page"])
page_counts = df["page"].value_counts().reset_index()
page_counts.columns = ["page", "views"]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("User Behavior Dashboard"),
    dcc.Graph(figure=px.bar(page_counts, x="page", y="views", title="Most Visited Pages"))
])

if __name__ == '__main__':
    app.run_server(debug=True)
