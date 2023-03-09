import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px

# para inicializar la aplicacion
app = dash.Dash()

# Leyendo un dataset de ejemplo
df = px.data.stocks()

def stock_prices():
    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x = df['date'],
                                y = df['AAPL'],
                                line = dict(color = 'firebrick', width = 4),
                                name = 'Google'
                                )
                     ])
    fig.update_layout(title = 'Precios en el tiempo',
                      xaxis_title = 'Fechas',
                      yaxis_title = 'Precios'
                      )
    return fig


app.layout = html.Div(id = 'parent',
                      children = [
                          html.H1(id = 'H1',
                                  children = 'Precios en el tiempo',
                                  style = {'textAlign':'center', 'marginTop':40,'marginBottom':40}),
                          dcc.Graph(id = 'line_plot',
                                    figure = stock_prices())
                      ])

if __name__ == '__main__':
    app.run_server(port=5000)