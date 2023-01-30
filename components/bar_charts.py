from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from .utill import get_data
from .ids import *

def render(app):
    df = get_data()
    @app.callback(
        Output(BAR_VOLUME,'children'),
        Input(DROPDOWN,'value')
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("player in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div("No Data Selected.", id=BAR_VOLUME)
        fig = px.bar(
                filtered_data,
                x="player",
                y="total_points_pre_game",
                title="Top 25 players Average points".format(dropdown[0]))
        return html.Div(dcc.Graph(figure=fig),id=BAR_VOLUME)
    return html.Div(id=BAR_VOLUME)
