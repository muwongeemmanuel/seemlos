"""from finalyearproject.models import Encounter
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
import dash_table as dt"""

from analysis.models import Encounter
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
import numpy as np
from datetime import datetime
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_table as dt



app = DjangoDash('dashboard',serve_locally = False, add_bootstrap_links=True)
app.css.append_css({
    "external_url": "static/css/style.css"
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

def onLoad_division_options():
    #Actions to perform upon initial page load

    division_options = (
        [{'label':year, 'value':year}
         for year in date_year]
    )
    return division_options

date_max = df['encounter_datetime'].max()
recent_year = date_max.year

recent_month1 = date_max.month
recent_month = calendar.month_name[recent_month1]


df_graph = df[['year','patient_gender']]
#df_graph = df_graph.set_index('year')
df_bargraph = df_graph['year'].value_counts().rename_axis('year').reset_index(name='Count')
"""fig1 = px.bar(df_bargraph, x="year", y="Count", title="Trend of patient growth through the years"
                 )
"""
df_bargraph1 = df_bargraph.sort_values(by=['year'])
fig1 = go.Figure()
fig1.add_trace(go.Bar(x=df_bargraph1['year'], y=df_bargraph1['Count'], name="Bar Chart"))
fig1.add_trace(go.Scatter(x=df_bargraph1['year'], y=df_bargraph1['Count'], name="Line Chart"))

fig1.update_layout(title_text=('Trend of patient growth through the years'),xaxis_title='Years', yaxis_title='No of patients')


df_graph = df[['year','patient_gender']]
#df_graph = df_graph.set_index('year')
df_bargraph = df_graph.groupby('year')['patient_gender'].value_counts().reset_index(name='Count')

#mask = df["day"] == day
fig2 = px.bar(df_bargraph, x="year", y="Count",
                 color="patient_gender", barmode="group", title="Comparison between male and female patients through the years")
"""fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df_bargraph['year'], y=df_bargraph['Count'], name="chart"))

fig2.update_layout(title_text=('Comparison between male and female patients through the years'),xaxis_title='Years', yaxis_title='No of patients')
"""

df_graph = df[['year','speciality']]
#df_graph = df_graph.set_index('year')
df_bargraph = df_graph.groupby('year')['speciality'].value_counts().reset_index(name='Count')

fig3 = px.bar(df_bargraph, x="year", y="Count",title="Comparison between the number of patients that visit the different specialities through the years.",
                 color="speciality")

"""fig3 = go.Figure()
fig3.add_trace(go.Bar(x=df_bargraph['year'], y=df_bargraph['Count'], name="chart",
    marker=dict(
        color='rgba(116, 205, 130, 0.6)',
        line=dict(color='rgba(116, 205, 130, 1.0)'))))

fig3.update_layout(title_text=('Comparison between the number of patients that visit the different specialities through the years.'),xaxis_title='Years', yaxis_title='No of patients')
    """




app.layout = html.Div([
      html.Div([
        html.H1('Work Force Statistics')
    ]),

   dbc.Row([



]),

dbc.Row(
    [
        dbc.Col(

         # summary table
        dcc.Graph(id='bar_graph', figure=fig1),md=6,


        ),

        dbc.Col(


        dcc.Graph(id='stacked_graph', figure=fig2),md=6,



        ),


    ]
),
dbc.Row(
    [
        dbc.Col(

         # summary table
        dcc.Graph(id='table_graph', figure=fig3),


        ),




    ]
),


dbc.Row(
    [
        dbc.Col(
            html.Div([
        html.Div([
            # Select Division Dropdown
            html.Div([
                html.Div('Select Year', className='three columns'),
                html.Div(dcc.Dropdown(id='division-selector',
                                      options=onLoad_division_options(),value=recent_year),
                         className='nine columns')
            ]),
               # Select Season Dropdown
            html.Div([
                html.Div('Select Month ', className='three columns'),
                html.Div(dcc.Dropdown(id='season-selector',value=recent_month),
                         className='nine columns')
            ]),

            # Select Team Dropdown
            html.Div([
                html.Div('Select Group', className='three columns'),
                html.Div([dcc.RadioItems(id='dropdown_color',
                options=[{'label': c, 'value': c} for c in ['Employee', 'Patient']],value='Employee'
            )])
            ]),




        ], className='six columns'),

    html.Div(className='six columns'),
    ], className='twleve columns'),md=6,

        ),
        dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Number of Employees', className='card-title'),
                        html.Div(id="output_employees"),
                    ]
                ),

            ],
            style={"background-color": "green","color": "white","align-content":"center","font-weight":"bold"},

        ),
        md=3,
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Number of Patients', className='card-title'),
                        html.Div(id="output_patients"),
                    ]
                ),

            ],
            style={"background-color": "green","color": "white","align-content":"center","font-weight":"bold"},

        ),
        md=3
    )

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
        ),md=6,
        ),
        dbc.Col(


        dcc.Graph(id='graph_2'),md=6,



        ),
        dbc.Col(

        html.Div([
        html.Div(id='table_container',  className='tableDiv'),

        dcc.Graph(id='table_container'),
                      ]),md=6,



        ),
        dbc.Col(

        html.Div([
        html.Div(id='pie_chart',  className='tableDiv'),

        dcc.Graph(id='pie_chart'),
                      ]),md=6,



        ),

    ]
),





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

@app.callback(
    Output(component_id='output_color', component_property='value'),
    [
        #Input(component_id='division-selector', component_property='value'),
        Input(component_id='dropdown_color', component_property='value'),

    ]

)
def callback_color(dropdown_color):
    'Change output message'
    return dropdown_color

def comparison_graph1(year,month,dropdown_color):
    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:13].index(month)
    #recent_month=calendar.month_name[:13].index(month)
    df_graph = df_graph[df_graph['month']==month]
    #df['year'] = df['encounter_datetime'].dt.year
    if dropdown_color =='Employee':
        df_graph_bar = df_graph['provider_name'].value_counts().rename_axis('provider_name').reset_index(name='Count')

        """fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph_bar['provider_name'], y=df_graph_bar['Count'], name="chart"))

        fig.update_layout(title_text=('Number of encounters made by each employee'),xaxis_title='Employee Name', yaxis_title='Encounters made in a month')
                    """
        fig = px.bar(df_graph_bar, x="provider_name", y="Count",title="Comparison between the number of patients that visit the different specialities through the years.",
                 color="Count")


        return fig

    elif dropdown_color =='Patient':
        df_graph['WeekDay'] = df_graph['encounter_datetime'].apply(lambda x: x.weekday())
        replace_map = {'WeekDay': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6:'Sunday'}}
        df_graph.replace(replace_map, inplace=True)

        #df_graph['day']=df_graph['encounter_datetime'].dt.weekday
        #day=calendar.day_name[:6]
        df_graph_bar = df_graph['WeekDay'].value_counts().rename_axis('WeekDay').reset_index(name='Count')


        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph['WeekDay'], y=df_graph_bar['Count'], name="chart"))

        fig.update_layout(title_text=('Number of patients per weekly day in the month'),xaxis_title='Weekdays', yaxis_title='No of patients')

        return fig

    else:
        """df_graph_bar = df_graph['speciality'].value_counts().rename_axis('speciality').reset_index(name='Count')

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph_bar['speciality'], y=df_graph_bar['Count'], name="chart"))

        fig.update_layout(title_text=('Bar Chart'),xaxis_title='Speciality', yaxis_title='Number of Employees')

        return fig"""
        return "This is it."



def comparison_graph2(year,month,dropdown_color):
    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:13].index(month)
    df_graph = df_graph[df_graph['month']==month]
    #df['year'] = df['encounter_datetime'].dt.year
    if dropdown_color =='Employee':
        df_graph_new = df_graph[['speciality','provider_name']]
        df_graph_bar = df_graph_new.groupby('speciality')['provider_name'].value_counts().reset_index(name='Count')

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_graph_bar['speciality'], y=df_graph_bar['Count'], name="chart"))

        fig.update_layout(title_text=('Number of employees that worked in a given speciality in a month'),xaxis_title='Speciality', yaxis_title='No of Employees')

        return fig

    elif dropdown_color =='Patient':
       df_graph_bar = df_graph['speciality'].value_counts().rename_axis('speciality').reset_index(name='Count')

       fig = go.Figure()
       fig.add_trace(go.Bar(x=df_graph_bar['speciality'], y=df_graph_bar['Count'], name="chart"))

       fig.update_layout(title_text=('Number of patients that visited a given speciality in the month'),xaxis_title='Speciality', yaxis_title='No of patients')

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

    figure = comparison_graph1(year,month,dropdown_color)

    return figure

@app.callback(
    Output(component_id='graph_2', component_property='figure'),
    [
        Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),
        Input(component_id='dropdown_color', component_property='value'),
    ]
)
def load_season_points_graph(year,month,dropdown_color):


    figure = []

    figure = comparison_graph2(year,month,dropdown_color)

    return figure


@app.callback(
    Output(component_id='output_employees', component_property='children'),
    [
        Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),

    ]
)
def load_season_points_graph(year,month):

    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:13].index(month)
    df_graph = df_graph[df_graph['month']==month]
    employess_available = df_graph['provider_name'].nunique()
    month_name = calendar.month_name[month]

    return " %s Employees in %s, %s." %(employess_available,month_name,year)

@app.callback(
    Output(component_id='output_patients', component_property='children'),
    [
        Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),

    ]
)
def load_season_points_graph(year,month):

    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:13].index(month)
    df_graph = df_graph[df_graph['month']==month]
    patients_available = df_graph['ecounter_id'].nunique()
    month_name = calendar.month_name[month]
    #month=calendar.month_name[:13].index(month)

    return " %s Patients in %s, %s." %(patients_available,month_name,year)


@app.callback(
    Output(component_id='table_container', component_property='figure'),
    [
        Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),
        Input(component_id='dropdown_color', component_property='value'),

    ]

    )

def display_table(year,month,dropdown_color):
    #df_temp = df[df['ASSIGNED_GROUP']==dpdown]
    if dropdown_color =='Employee':
        df_graph = df[df['year']==year]
        df_graph['month'] = df_graph['encounter_datetime'].dt.month
        month=calendar.month_name[:13].index(month)
        df_graph = df_graph[df_graph['month']==month]
        df_graph_bar = df_graph['speciality'].value_counts().rename_axis('speciality').reset_index(name='Count')
        fig = go.Figure(data=[go.Table(header=dict(values=list(df_graph_bar.columns),
                fill_color='paleturquoise',
                align='left'), cells=dict(values=[df_graph_bar.speciality, df_graph_bar.Count],
               fill_color='lavender',
               align='left'))])
        return fig
        """patients_available = df_graph['provider_name'].value_counts().to_frame()
        return html.Div([
            dt.DataTable(
                id='main-table',
                columns=[{'name': i, 'id': i} for i in patients_available.columns],
                data=patients_available[0:5].to_dict('rows'),
                style_table={
                    'maxHeight': '20%',
                    #'overflowY': 'scroll',
                    'width': '30%',
                    'minWidth': '10%',
                },
                style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                style_cell={'backgroundColor': 'rgb(50, 50, 50)','color': 'white','height': 'auto','width': 'auto'},#minWidth': '0px', 'maxWidth': '180px', 'whiteSpace': 'normal'},
                #style_cell={'minWidth': '130px', 'width': '150px', 'maxWidth': '180px'},
                style_data={'whiteSpace': 'auto','height': 'auto','width': 'auto'}

        )

        ])"""

@app.callback(
    Output(component_id='pie_chart', component_property='figure'),
    [ Input(component_id='division-selector', component_property='value'),
        Input(component_id='season-selector', component_property='value'),
        Input(component_id='dropdown_color', component_property='value'),])

def generate_chart(year,month,dropdown_color):
    #if dropdown_color =='Patient':
    df_graph = df[df['year']==year]
    df_graph['month'] = df_graph['encounter_datetime'].dt.month
    month=calendar.month_name[:13].index(month)
    df_graph = df_graph[df_graph['month']==month]
    df_graph_bar = df_graph['speciality'].value_counts().rename_axis('speciality').reset_index(name='Count')

    fig = px.pie(df_graph_bar, values="Count", names="speciality", hole=0.4)
    return fig





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
