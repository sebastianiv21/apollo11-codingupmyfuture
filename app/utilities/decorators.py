import time
import threading


def periodic_task(interval):
    """
    Decorador para ejecutar una función de forma periódica en un hilo separado.

    Args:
        interval (int): El intervalo de tiempo en segundos entre cada ejecución.

    Returns:
        decorator: El decorador que ejecuta la función de forma periódica.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                func(*args, **kwargs)
                time.sleep(interval)

        threading.Thread(target=wrapper, daemon=True).start()
        return wrapper

    return decorator
