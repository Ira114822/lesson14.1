# 5! = 5 * 4 * 3 * 2 * 1
# f(5!)

def factorial(number):
    if number <=1:
        return 1

    return number * factorial(number - 1)

def main():
    number = int(input("Input number: "))
    fac = factorial(number)

    msg = f"Result = {fac}"
    print(msg)

main()