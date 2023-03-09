import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div('Hola a todos!')

if __name__ == '__main__':
    app.run_server(port=5000)