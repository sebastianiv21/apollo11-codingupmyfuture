import argparse


def es_numero_positivo(valor: int) -> int:
    """
    Función definida por el usuario para validar si el valor es un número positivo

    Args:
        valor (int): valor a validar

    Raises:
        argparse.ArgumentTypeError: si el valor no es un número positivo
        argparse.ArgumentTypeError: si el valor no es un número

    Returns:
        int: valor validado
    """
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            raise argparse.ArgumentTypeError(f"{valor} no es un número positivo")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{valor} no es un número")
