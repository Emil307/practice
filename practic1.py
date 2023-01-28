try:
    v0 = int(input())
    v = int(input())
    t = int(input())

    def decorator(original_function):
        def wrapper():
            original_function(v0, v, t)
            print((v ** 2 - v0 ** 2) / (2 * original_function(v0, v, t)))
            print(original_function(v0, v, t))
        return wrapper

    def acceleration(v0, v, t):
        a = (v - v0) / t
        return a

    acceleration = decorator(acceleration)
    acceleration()
except ValueError:
    print('Нельзя вводить строки')
except ZeroDivisionError:
    print('Нельзя делить на ноль')
