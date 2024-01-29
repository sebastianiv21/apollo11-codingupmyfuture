"""para definir configuración transversal que pueden ser usados 
en las diferentes pruebas unitarias.

todas las pruebas unitarias normalmente se hacen con funciones y asserts
"""
import pytest


@pytest.fixture(scope="session")
def app():
    # truco para crear atributos dinamicos
    class App:
        pass

    app = App()
    # app.funcion_suma = suma
    # app.funcion_resta = resta
    # app.texto_util = TextoUtil

    return app
