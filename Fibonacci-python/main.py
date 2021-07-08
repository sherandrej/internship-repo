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
    counter = num - 2
    while counter > 0:
        fib1, fib2 = fib2, fib1 + fib2
        counter -= 1
    return fib2


if __name__ == '__main__':
    while True:
        fib_num = check_input()
        if fib_num != None:
            result = fibonacci(fib_num)
            print("your num =", str(fib_num))
            print("Fib num result =", str(result))
        else:
            print("Please try again")
