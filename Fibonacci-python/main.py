#!/usr/bin/python3

def check_input():
    error = "Error input. Number must be positive INT or 0"
    try:
        number = int(input("Input number: "))
        if number < 0:
            print(error)
        return number
    except Exception as ex:
        print(ex, '\n', error)
        return None


def fibonacci(num):
    fib1, fib2 = 0, 1
    n = num - 2
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


if __name__ == '__main__':
    while True:
        fib_num = check_input()
        if fib_num != None:
            res = fibonacci(fib_num)
            print("your num =", str(fib_num))
            print("Fib num result =", str(res))
        else:
            print("Please try again")
