from dash import html, dcc
import dash_bootstrap_components as dbc
from data.load_data import DataLoader
from components.graph import stacked_bar_chart_all, pie_all, bar_chart_all, pie_year, bar_chart_year, line_year
from components.slider import year_slider


data = DataLoader().get_data()

def create_layout():
    return dbc.Container([
        html.H1('Spending Pattern DashBoard', style={'margin': '20px'}),
        html.H2('All spending:', style={'margin': '20px'}),

        dbc.Row([
            dbc.Col(pie_all, className='col-6'),
            dbc.Col(bar_chart_all, className='col-6', style={'padding': '30px'})

        ], className='my-3'),
        stacked_bar_chart_all,

        html.H2('On yearly basis:', style={'margin': '20px'}),

        dbc.Row([
            dbc.Col(pie_year, className='col-6'),
            dbc.Col(bar_chart_year, className='col-6', style={'padding': '30px'})

        ], className='my-3'),

        dbc.Alert('Slider', style={'text-align':'center'}),
        year_slider,

        line_year


    ])