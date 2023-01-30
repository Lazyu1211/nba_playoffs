from dash import Dash,html
import dash_bootstrap_components as dbc
from components import dropdown, bar_charts,scatter, imagesrc, pie_chart

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="🏀", className="header-emoji"),
        html.H1(
                "Playoffs TOP 25 Analytics", className="header-title"
                ),
        html.P(
                "Based on 2022 data set we can analyze Top 25 players of NBA playoffs.",
                className="header-description",
                ),
        html.Img(src=imagesrc.srcpath),
        dropdown.render(app)
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(bar_charts.render(app),lg=4),
            dbc.Col(scatter.render(app),lg=4),
            dbc.Col(pie_chart.render(app),lg=4)
        ],className="mt-4")
    ])