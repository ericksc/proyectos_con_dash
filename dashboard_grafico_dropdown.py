import dash
import pandas as pd
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash()

df = px.data.stocks()

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1',
            children = 'Precios en el tiempo',
            style = {'textAlign':'center', 'marginTop':40,'marginBottom':40}),

    dcc.Dropdown( id = 'dropdown',
                  options = [
                      # punto 2
                      {'label':'Google', 'value':'GOOG' },
                      {'label': 'Apple', 'value':'AAPL'},
                      {'label': 'Amazon', 'value':'AMZN'},
                      {'label': 'Facebook', 'value':'FB'},
                      {'label': 'Netflix', 'value':'NFLX'},
                      {'label': 'Microsoft', 'value':'MSFT'},
                  ],
                  value = 'GOOG'),
    dcc.Graph(id = 'bar_plot')
])


@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    # punto 3
    fig = go.Figure([go.Scatter(x = df['date'], y = df['{}'.format(dropdown_value)], \
                                line = dict(color = 'firebrick', width = 4))
                     ])

    fig.update_layout(title='Precios en lo largo del tiempo',
                      xaxis_title='Fechas',
                      yaxis_title='Precios'
                      )
    return fig

if __name__ == '__main__':
    app.run_server(port=5000)