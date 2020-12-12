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
from datetime import datetime
import dash_bootstrap_components as dbc
import plotly.express as px


app = DjangoDash('dashboard',serve_locally = False, add_bootstrap_links=True)
"""app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})"""

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

def onLoad_division_options():
    #Actions to perform upon initial page load

    division_options = (
        [{'label':year, 'value':year}
         for year in date_year]
    )
    return division_options


app.layout = html.Div([
      html.Div([
        html.H1('Work Force Statistics')
    ]),

   dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title'
                            ),
                        html.P(id='card_text_1', children=['Sample text.']),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title'),
                        html.P('Sample text.'),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title'),
                        html.P('Sample text.'),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title'),
                        html.P('Sample text.'),
                    ]
                ),
            ]
        ),
        md=3
    )
]),

   
dbc.Row(
    [
        dbc.Col(
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
            html.Div([
                html.Div('Select Group', className='three columns'),
                html.Div([dcc.RadioItems(id='dropdown_color',
                options=[{'label': c, 'value': c} for c in ['Employee', 'Patient']]
            )])
            ]),

            
    
     
        ], className='six columns'),
    
    html.Div(className='six columns'),
    ], className='twleve columns'),

        ),
        
    ]
),


dbc.Row(
    [
        dbc.Col(
            
            html.Div([
        html.Div(id='output_color'),
         # summary table
        dcc.Graph(id='season-graph'),
          ]
        ),
        ),
        dbc.Col(
            html.Div([
        html.H4('Speciality'),

        dcc.Graph(id='graph_2'),
                     ] 
                     ),
            
        ),
        
    ]
),

    
        
])

"""app.layout = html.Div([content])

content = html.Div(
    [
        html.H2('Analytics Dashboard Template', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row
    ],
    style=CONTENT_STYLE
)

"""

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

@app.callback(
    Output(component_id='output_color', component_property='value'),
    [
        #Input(component_id='division-selector', component_property='value'),
        Input(component_id='dropdown_color', component_property='value')
    ]
    
)
def callback_color(dropdown_color):
    'Change output message'
    return dropdown_color

def comparison_graph(year,month,dropdown_color):
    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:12].index(month)
    df_graph = df_graph[df_graph['month']==month]
    #df['year'] = df['encounter_datetime'].dt.year
    if dropdown_color =='Employee':
        df_graph_bar = df_graph['provider_name'].value_counts().rename_axis('provider_name').reset_index(name='Count')

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph_bar['provider_name'], y=df_graph_bar['Count'], name="chart"))
        
        fig.update_layout(title_text=('Bar Chart'),xaxis_title='Employee Name', yaxis_title='Encounters made in a month')
                        
        return fig
    
    elif dropdown_color =='Patient':
        df_graph['WeekDay'] = df_graph['encounter_datetime'].apply(lambda x: x.weekday())
        replace_map = {'WeekDay': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday'}}
        df_graph.replace(replace_map, inplace=True)
        
        #df_graph['day']=df_graph['encounter_datetime'].dt.weekday
        #day=calendar.day_name[:6]
        df_graph_bar = df_graph['WeekDay'].value_counts().rename_axis('WeekDay').reset_index(name='Count')
    
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph['WeekDay'], y=df_graph_bar['Count'], name="chart"))
        
        fig.update_layout(title_text=('Bar Chart'),xaxis_title='Speciality', yaxis_title='Number of Employees')
                        
        return fig

    else:
        """df_graph_bar = df_graph['speciality'].value_counts().rename_axis('speciality').reset_index(name='Count')
    
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph_bar['speciality'], y=df_graph_bar['Count'], name="chart"))
        
        fig.update_layout(title_text=('Bar Chart'),xaxis_title='Speciality', yaxis_title='Number of Employees')
                        
        return fig"""
        return "This is it."
    


@app.callback(
    Output(component_id='season-graph', component_property='figure'),
    [
        Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),
        Input(component_id='dropdown_color', component_property='value'),
    ]
)
def load_season_points_graph(year,month,dropdown_color):
    

    figure = [] 
    
    figure = comparison_graph(year,month,dropdown_color)

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