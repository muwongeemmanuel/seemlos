from .models import TestTable
from django_pandas.managers import DataFrameManager
from django.db.models.query import QuerySet 
import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

patients = TestTable.objects.all()
df = patients.to_dataframe()
app = DjangoDash('barchart1', serve_locally=False)
def get_crypto_daily_line_chart():
    
    #df = get_daily_crypto(symbol)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['id'], y=df['age'], name="chart"))
    
    fig.update_layout(title_text=('Bar Chart'),xaxis_title='ID', yaxis_title='Age')
    fig.show()                 
    return fig

chart = dcc.Graph(figure=(get_crypto_daily_line_chart()))
app.layout = html.Div(children=[html.Div(chart)])
