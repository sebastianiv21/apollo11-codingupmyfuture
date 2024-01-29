from typing import List, Dict

import os
import pandas as pd
import yaml


def generar_reportes(directorio: str, output_directory: str) -> None:
    """
    Analiza archivos de registro en formato YAML dentro de un directorio y genera informes.

    Parameters:
    - directorio (str): Ruta al directorio que contiene los archivos de registro (.log) en formato YAML.
    - output_directory (str): Ruta al directorio de salida donde se almacenarán los archivos en formato YAML.

    Returns:
    None

    Raises:
    - FileNotFoundError: Si el directorio proporcionado no existe.
    - yaml.YAMLError: Si hay un problema al leer o cargar el archivo YAML.

    Examples:
    >>> directorio_de_archivos = "/ruta/al/directorio"
    >>> directorio_de_salida = "/ruta/al/directorio_de_salida"
    >>> generar_reportes(directorio_de_archivos, directorio_de_salida)
    """
    try:
        # Verificar si el directorio existe
        if not os.path.exists(directorio):
            raise FileNotFoundError("El directorio proporcionado no existe.")

        # Crear el directorio de salida si no existe
        os.makedirs(output_directory, exist_ok=True)

        # Lista para almacenar los DataFrames de cada archivo .log
        dataframes: List[pd.DataFrame] = []

        # Iterar sobre cada archivo en el directorio
        for archivo in os.listdir(directorio):
            if archivo.endswith('.log'):
                ruta_archivo = os.path.join(directorio, archivo)

                # Leer el archivo YAML y convertirlo en DataFrame
                try:
                    with open(ruta_archivo, 'r') as file:
                        data = yaml.safe_load(file)
                        df = pd.json_normalize(data)
                        dataframes.append(df)
                except yaml.YAMLError as e:
                    print(f"Error al leer el archivo YAML {archivo}: {e}")

        # Concatenar todos los DataFrames en uno solo
        df_total = pd.concat(dataframes, ignore_index=True)

        # 1. Cantidad de eventos por estado para cada misión
        conteo_eventos_mision = df_total.groupby(
            ['mission', 'device_type']).size().reset_index(name='count')
        conteo_eventos_mision = conteo_eventos_mision.groupby(
            ['mission', 'device_type']).agg({'count': 'sum'}).reset_index()

        # Guardar el resultado en un archivo YAML
        archivo_salida_1 = os.path.join(output_directory, "1_eventos.log")
        with open(archivo_salida_1, 'w') as outfile:
            for mission, group in conteo_eventos_mision.groupby('mission'):
                mission_data: Dict[str, Dict[str, int]] = {mission: {}}
                for _, row in group.iterrows():
                    dispositivo = row['device_type']
                    cantidad = row['count']
                    mission_data[mission][dispositivo] = cantidad
                yaml.dump(mission_data, outfile, default_flow_style=False)
                outfile.write('\n')  # Separador entre misiones

        # 2. Dispositivo con mayor número de estados 'unknown' por misión
        max_unknown = df_total[df_total['device_status'] == 'unknown'].groupby(
            ['mission', 'device_type']).size().reset_index(name='count')
        dispositivo_max_unknown = max_unknown.loc[max_unknown.groupby('mission')[
            'count'].idxmax()]

        # Guardar el resultado en un archivo YAML
        archivo_salida_2 = os.path.join(output_directory, "2_desconexiones.log")
        with open(archivo_salida_2, 'w') as outfile:
            for mission, group in dispositivo_max_unknown.groupby('mission'):
                mission_data: Dict[str, Dict[str, int]] = {mission: {}}
                for _, row in group.iterrows():
                    dispositivo = row['device_type']
                    cantidad = row['count']
                    mission_data[mission][dispositivo] = cantidad
                yaml.dump(mission_data, outfile, default_flow_style=False)
                outfile.write('\n')  # Separador entre misiones

        '''
        # 3. Cantidad de dispositivos con estado 'killed'
        total_killed = df_total[df_total['device_status'] == 'killed'].shape[0]

        # Guardar el resultado en un archivo YAML
        archivo_salida_3 = os.path.join(output_directory, "reporte_3.yaml")
        with open(archivo_salida_3, 'w') as outfile:
            yaml.dump({"Cantidad de dispositivos con estado 'killed'": total_killed},
                      outfile, default_flow_style=False)
        '''

        # 3. Cantidad de dispositivos con estado 'killed'
        dispositivos_killed = df_total[df_total['device_status'] == 'killed']
        total_killed = dispositivos_killed.groupby(
            ['mission', 'device_type']).size().reset_index(name='count')

        # Guardar el resultado en un archivo YAML
        archivo_salida_3 = os.path.join(output_directory, "3_dispositivos_inoperables.log")
        with open(archivo_salida_3, 'w') as outfile:
            for mission, group in total_killed.groupby('mission'):
                mission_data: Dict[str, Dict[str, int]] = {mission: {}}
                for _, row in group.iterrows():
                    dispositivo = row['device_type']
                    cantidad = row['count']
                    mission_data[mission][dispositivo] = cantidad
                yaml.dump(mission_data, outfile, default_flow_style=False)
                outfile.write('\n')  # Separador entre misiones
            # Agregar el campo 'total_inoperables'
            total_inoperables = dispositivos_killed.shape[0]
            yaml.dump({"total_inoperables": total_inoperables},
                      outfile, default_flow_style=False)

        # 4. Porcentajes de datos generados para cada dispositivo y misión
        porcentajes = df_total.groupby(
            ['mission', 'device_type']).size() / len(df_total) * 100

        # Guardar el resultado en un archivo YAML
        archivo_salida_4 = os.path.join(output_directory, "4_porcentaje.log")
        with open(archivo_salida_4, 'w') as outfile:
            for mission, group in porcentajes.groupby('mission'):
                mission_data: Dict[str, Dict[str, str]] = {mission: {}}
                for _, row in group.reset_index().iterrows():
                    dispositivo = row['device_type']
                    # Obtener el porcentaje del primer (y único) valor
                    porcentaje = row[0]
                    mission_data[mission][dispositivo] = f'{porcentaje:.2f}%'
                yaml.dump(mission_data, outfile, default_flow_style=False)
                outfile.write('\n')  # Separador entre misiones

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

