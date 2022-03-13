
def name_age(x=input("What is your name?"), y=input("How old are you?")):
    print(f"Hello {x}. Your age is {y}.")
    return x + y


def swap_integers(num1, num2):
    x = num1
    y = num2
    num1 = y
    num2 = x
    print(num1, num2)
    return str(num1) + str(num2)


def check_numbers(num1, num2):
    return (num1 % 10 == 0 and num2 % 10 == 0) and num1 % 6 == 0 or num2 % 6 == 0       # einzeilige Lösung 8)


def sum_up(num1, num2):
    result = 0
    if num2 < num1 or num1 < 0 or num2 < 0:
        return 0
    for num in range(num1, num2 + 1):
        result += num
    return result


def circle_area(r1, r2, r3):
    c1 = 3.14 * (r1 ** 2)
    c2 = 3.14 * (r2 ** 2)
    c3 = 3.14 * (r3 ** 2)
    return c1 + c2 + c3


def check_string(text):
    text = text.lower()
    return text.startswith('a') or text.endswith('a')


def triangle(rows):
    for x in range(1, rows + 1):
        for y in range(1, x + 1):
            print('* ', end='')
        print(' ')


