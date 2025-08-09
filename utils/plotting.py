
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def line_equity(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['equity'], mode='lines', name='Equity'))
    if 'benchmark' in df.columns:
        fig.add_trace(go.Scatter(x=df['date'], y=df['benchmark'], mode='lines', name='Benchmark'))
    fig.update_layout(margin=dict(l=10,r=10,t=30,b=10), height=300, legend=dict(orientation='h'))
    return fig

def pie_alloc(df):
    fig = px.pie(df, names='sector', values='alloc', hole=0.45)
    fig.update_layout(margin=dict(l=10,r=10,t=30,b=10), height=300, legend=dict(orientation='h'))
    return fig

def bar_pl(df):
    tmp = df.copy()
    tmp = tmp.sort_values('unrealized_pl')
    fig = px.bar(tmp, x='symbol', y='unrealized_pl')
    fig.update_layout(margin=dict(l=10,r=10,t=30,b=10), height=300)
    return fig
