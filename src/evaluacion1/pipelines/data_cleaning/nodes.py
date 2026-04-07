import pandas as pd

def limpiar_envios(df_envios: pd.DataFrame) -> pd.DataFrame:
    
    # eliminar filas sin id_envio
    df_envios = df_envios.dropna(subset=["id_envio"])
    
    # convertir peso a numérico
    df_envios["peso_kg"] = pd.to_numeric(df_envios["peso_kg"], errors="coerce")
    
    # rellenar nulos en peso con la media
    df_envios["peso_kg"] = df_envios["peso_kg"].fillna(df_envios["peso_kg"].mean())
    
    # convertir fechas
    df_envios["fecha_envio"] = pd.to_datetime(df_envios["fecha_envio"], errors="coerce")
    df_envios["fecha_entrega"] = pd.to_datetime(df_envios["fecha_entrega"], errors="coerce")
    
    # normalizar texto
    df_envios["tipo_carga"] = df_envios["tipo_carga"].str.lower()
    df_envios["estado"] = df_envios["estado"].str.lower()
    
    return df_envios