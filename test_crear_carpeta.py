import os


from src.prueba import crear_carpeta_devices


def test_crear_carpeta_devices():
    # Definir una ruta para las pruebas
    ruta_prueba = '/tmp'

    # Llamar a la función para crear la carpeta
    carpeta_creada = crear_carpeta_devices(ruta_prueba)

    # Verificar que la carpeta fue creada correctamente
    assert os.path.exists(carpeta_creada)
    assert os.path.isdir(carpeta_creada)

    # Limpiar después de las pruebas (eliminar la carpeta creada)
    os.rmdir(carpeta_creada)
