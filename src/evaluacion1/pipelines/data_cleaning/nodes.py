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


def limpiar_rutas(df_rutas: pd.DataFrame) -> pd.DataFrame:
    
    # eliminar filas sin id
    df_rutas = df_rutas.dropna(subset=["id_ruta"])
    
    # convertir id a int
    df_rutas["id_ruta"] = df_rutas["id_ruta"].astype(int)
    
    # rellenar nulos numéricos
    df_rutas["distancia_km"] = df_rutas["distancia_km"].fillna(df_rutas["distancia_km"].mean())
    df_rutas["tiempo_estimado_hrs"] = df_rutas["tiempo_estimado_hrs"].fillna(df_rutas["tiempo_estimado_hrs"].mean())
    df_rutas["peaje_total"] = df_rutas["peaje_total"].fillna(df_rutas["peaje_total"].mean())
    
    # rellenar categóricos
    df_rutas["origen"] = df_rutas["origen"].fillna("desconocido")
    df_rutas["destino"] = df_rutas["destino"].fillna("desconocido")
    df_rutas["tipo_via"] = df_rutas["tipo_via"].fillna("desconocido")
    
    # limpiar strings
    df_rutas["origen"] = df_rutas["origen"].str.lower().str.strip()
    df_rutas["destino"] = df_rutas["destino"].str.lower().str.strip()
    df_rutas["tipo_via"] = df_rutas["tipo_via"].str.lower().str.strip()
    
    # eliminar duplicados
    df_rutas = df_rutas.drop_duplicates()
    
    return df_rutas


def limpiar_vehiculos(df_vehiculos: pd.DataFrame) -> pd.DataFrame:
    
    # eliminar filas sin id_vehiculo
    df_vehiculos = df_vehiculos.dropna(subset=["id_vehiculo"])
    
    # convertir id a entero
    df_vehiculos["id_vehiculo"] = df_vehiculos["id_vehiculo"].astype(int)
    
    # rellenar nulos numéricos con la media
    for col in ["capacidad_kg", "capacidad_m3", "año_fabricacion", "km_recorridos"]:
        df_vehiculos[col] = df_vehiculos[col].fillna(df_vehiculos[col].mean())
    
    # rellenar categóricos
    df_vehiculos["placa"] = df_vehiculos["placa"].fillna("desconocida")
    df_vehiculos["tipo"] = df_vehiculos["tipo"].fillna("desconocido")
    df_vehiculos["estado_vehiculo"] = df_vehiculos["estado_vehiculo"].fillna("desconocido")
    
    # limpiar strings
    for col in ["placa", "tipo", "estado_vehiculo"]:
        df_vehiculos[col] = df_vehiculos[col].str.lower().str.strip()
    
    # eliminar duplicados
    df_vehiculos = df_vehiculos.drop_duplicates()
    
    return df_vehiculos