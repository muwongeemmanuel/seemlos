from finalyearproject.models import Encounter
from django_pandas.managers import DataFrameManager
from django.db.models.query import QuerySet 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import dash
import pandas as pd
import calendar
import time
import numpy as np


app = DjangoDash('dashboard',serve_locally = False)
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

encounters = Encounter.objects.all()
df = encounters.to_dataframe()

df['encounter_datetime']= pd.to_datetime(df['encounter_datetime'])
df['year'] = df['encounter_datetime'].dt.year
#df['year'] = df['year'].unique()
#date_year = df['year'].values.tolist()
date_year1 = df['year'].unique()
date_year = np.sort(date_year1)


def onLoad_division_options():
    #Actions to perform upon initial page load

    division_options = (
        [{'label':year, 'value':year}
         for year in date_year]
    )
    return division_options


app.layout = html.Div([

    # Page Header
    html.Div([
        html.H1('Work Force Statistics')
    ]),

    # Dropdown Grid
    html.Div([
        html.Div([
            # Select Division Dropdown
            html.Div([
                html.Div('Select Year', className='three columns'),
                html.Div(dcc.Dropdown(id='division-selector',
                                      options=onLoad_division_options()),
                         className='nine columns')
            ]),
               # Select Season Dropdown
            html.Div([
                html.Div('Select Season', className='three columns'),
                html.Div(dcc.Dropdown(id='season-selector'),
                         className='nine columns')
            ]),
            
            # Select Team Dropdown
    
     
        ], className='six columns'),
    
    html.Div(className='six columns'),
    ], className='twleve columns'),
    # Season Summary Table and Graph
    html.Div([
         # summary table
        dcc.Graph(id='season-graph'),
          ], className='six columns')
        
])


@app.callback(
    Output(component_id='season-selector', component_property='options'),
    [
        Input(component_id='division-selector', component_property='value')
    ]
)
def populate_Date_selector(year):
    months = calendar.month_name
    return [
        {'label': month, 'value': month}
        for month in months
    ]

"""@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [
        dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    'Change output message'
    return "The selected color is %s." % dropdown_value"""

def comparison_graph(year,month):
    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:12].index(month)
    df_graph = df_graph[df_graph['month']==month]
    #df['year'] = df['encounter_datetime'].dt.year
    df_graph_bar = df_graph['provider_name'].value_counts().rename_axis('provider_name').reset_index(name='Count')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_graph_bar['provider_name'], y=df_graph_bar['Count'], name="chart"))
    
    fig.update_layout(title_text=('Bar Chart'),xaxis_title='ID', yaxis_title='Age')
                    
    return fig


@app.callback(
    Output(component_id='season-graph', component_property='figure'),
    [
        Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),
        
    ]
)
def load_season_points_graph(year, month):
    

    figure = [] 
    
    figure = comparison_graph(year,month)

    return figure










"""def get_seasons():
    #Actions to perform upon initial page load

    #df['month'] = df['encounter_datetime'].dt.month
    #date_month = df['month'].values.tolist()
    date_month = calendar.month_name
    return date_month
"""

"""
@app.callback(
    Output(component_id='division-selector', component_property='children')
)

def load_match_results():
    results = print('hello')
    return results
"""

"""app = DjangoDash('dashboard',serve_locally = False)
app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i, 'value': j} for i, j in [('L', 'large'),
                                                       ('M', 'medium'),
                                                       ('S', 'small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    'Change output message'
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    'Change output message'
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,dropdown_color)
"""