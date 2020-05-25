"""Calculo de PI usando la serie de Euler"""

import math


def aproximate_pi(proxim):
    """Obtiene PI dado un valor de aproximación"""

    sum = 0
    for valor in range(1, proxim):
        sum = sum + (1 / valor ** 2)

    pi = math.sqrt((sum*6))
    print(f"El valor de PI es: {pi}")


if __name__ == "__main__":
    aproximate_pi(100000000)
