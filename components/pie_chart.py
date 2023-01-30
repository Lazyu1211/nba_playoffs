from dash import Dash, html, dcc
import plotly.express as px
from .utill import country
from .ids import *

def render(app):
    df = country()
    fig = px.pie(df, values = 'rank', names = 'country', title = 'Country')
    return html.Div(dcc.Graph(figure=fig), id=PIE_CHART)