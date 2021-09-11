def floordiv(dividend, divisor):
    """
    Функция целочисленного деления
    floordiv(-6, 4), floordiv(6, -4) возвращает -1
    floordiv(6, 4), floordiv(-6, -4) возвращает 1
    """
    if (dividend < 0) != (divisor < 0):
        sign = -1
    else:
        sign = 1
    quotient = (abs(dividend) // abs(divisor)) * sign
    return quotient


def modulo(dividend, divisor):
    """
    Функция взятия остатка от деления
    modulo(-6, 4), modulo(6, -4) возвращает -2
    modulo(-6, -4), modulo(-6, -4) возвращает 1
    """
    if (dividend < 0) != (divisor < 0):
        sign = -1
    else:
        sign = 1
    mod = (abs(dividend) % abs(divisor)) * sign
    return mod


print(floordiv(-6, 4), floordiv(6, -4), floordiv(6, 4), floordiv(-6, -4))
print(modulo(-6, 4), modulo(6, -4), modulo(6, 4), modulo(-6, -4))
