import plotly.express as px
import pandas as pd

def plot_data(data):
    df = data.filter(["Date", "Close"])
    fig = px.line(df, x = "Date", y = "Close")
    fig.show()