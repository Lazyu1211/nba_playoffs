from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import os
from .utill import get_data
from .ids import *

def render(app):
    df = get_data()
    player = df["player"].to_list()
    all_players = [{"label":i, "value":i} for i in player]
    return  html.Div(
    [
        dcc.Dropdown(
            options = all_players,
            placeholder="Choose a player",
            className="mb-3",
            value="LeBron James",
            id = DROPDOWN,
            multi=False,
        ),
    ])