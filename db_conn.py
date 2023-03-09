from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///db.sqlite', echo=False)

def leer_db(table_name):
    return pd.read_sql(sql=f'select * from {table_name}', con=engine)

def salvar_db(df, table_name):
    df.to_sql(table_name, engine, index=False, if_exists='replace')

if __name__ == '__main__':
    my_df = pd.DataFrame([
        {'a': 1, 'b': 1},
        {'a': 2, 'b': 2},
        {'a': 3, 'b': 3},
    ])
    # salvar hacia base de datos
    salvar_db(df=my_df, table_name='mi_tabla')

    # leer desde base de datos
    leer_db = leer_db(table_name='mi_tabla')
    print(leer_db)