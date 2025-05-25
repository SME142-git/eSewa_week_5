from dash import dcc, Dash, html
import dash_bootstrap_components as dbc
from layouts.main_layout import create_layout
from callbacks.main_callback import register_callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

app.layout = create_layout()

register_callbacks(app)

server = app.server  # Required for Render