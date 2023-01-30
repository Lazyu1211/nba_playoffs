from dash import Dash, html
import dash_bootstrap_components as dbc
from layout import create_layout

app = Dash(external_stylesheets=[dbc.themes.COSMO])
app.title = "NBA-Playoffs Top 25"
app._favicon = "/Users/junyuwu/nba_playoffs/assets/i.png" 
app.layout = create_layout(app)
if __name__ == "__main__":
    app.run_server(debug=True)  

#def main():
   # app = Dash(external_stylesheets=[dbc.themes.COSMO])
  #  app.title = "NBA-Playoffs Top 25"
  #  app._favicon = "/Users/junyuwu/nba_playoffs/assets/i.png" 
 #   app.layout = create_layout(app)
 #   app.run_server(debug=True)
#main()


