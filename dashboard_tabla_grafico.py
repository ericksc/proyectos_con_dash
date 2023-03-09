import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dash_table
from dash import html
from dash import dcc
import pandas as pd

from db_conn import leer_db, salvar_db

app = dash.Dash(__name__)

params = [
    'Weight', 'Torque', 'Width', 'Height',
    'Efficiency', 'Power', 'Displacement'
]

app.layout = html.Div([
    html.H1('Mi dashboard'),
    html.Div(id='status_leer'),
    html.Div(id='status_guardar'),
    # ponga aqui los botones!!!
    dbc.Button("Leer desde base de datos", color="primary", id='leer_db', n_clicks=0),
    dbc.Button("Guardar hacia base de datos", color="primary", id='guardar_db', n_clicks=0),
    dash_table.DataTable(
        id='table-editing-simple',
        columns=(
            [{'id': 'Model', 'name': 'Model'}] +
            [{'id': p, 'name': p} for p in params]
        ),
        data=[
            dict(Model=i, **{param: 0 for param in params})
            for i in range(1, 5)
        ],
        editable=True
    ),
    dcc.Graph(id='table-editing-simple-output')
])

# el callback para leer de db
@app.callback(Output('status_leer', 'children'),
              Output('table-editing-simple', 'data'),
              Output('table-editing-simple', 'columns'),
              Input('leer_db', 'n_clicks'),
              State('table-editing-simple', 'data'),
              State('table-editing-simple', 'columns')
              )
def leer(dato_del_boton, data, columns):
    if dato_del_boton > 0:
        df = leer_db(table_name='mis_datos')
        return f'Estoy leyendo de base de datos. click No={dato_del_boton}', \
               df.to_dict(orient='record'), [{'id':i, 'name':i} for i in df.columns.tolist()]
    else:
        return '', data, columns


# el callback para salvar en db
@app.callback(Output('status_guardar', 'children'),
              Input('guardar_db', 'n_clicks'),
              Input('table-editing-simple', 'data'),
              Input('table-editing-simple', 'columns')
              )
def salvar(dato_del_boton, rows, columns):
    if dato_del_boton > 0:
        df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
        ## llamar por comida!!
        salvar_db(df=df, table_name='mis_datos')
        return f'Estoy Salvando en base de datos. click No={dato_del_boton}'
    else:
        return ''

@app.callback(
    Output('table-editing-simple-output', 'figure'),
    Input('table-editing-simple', 'data'),
    Input('table-editing-simple', 'columns'))
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return {
        'data': [{
            'type': 'parcoords',
            'dimensions': [{
                'label': col['name'],
                'values': df[col['id']]
            } for col in columns]
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=5000)