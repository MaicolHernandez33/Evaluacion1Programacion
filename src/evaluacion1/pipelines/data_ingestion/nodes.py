import pandas as pd

def explorar_envios(df_envios: pd.DataFrame) -> pd.DataFrame:
    
    print("Shape:", df_envios.shape)
    print("\nColumnas:", df_envios.columns)
    print("\nTipos de datos:")
    print(df_envios.dtypes)
    
    print("\nPrimeras filas:")
    print(df_envios.head())
    
    print("\nValores nulos:")
    print(df_envios.isnull().sum())
    
    return df_envios