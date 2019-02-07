n = input("Introduce a number:")
n = int(n)
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a+b

    print()
    return
fibonacci(n)
