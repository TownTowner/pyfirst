from defination import *


def greet_time(name):
    from datetime import datetime

    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "早上好"
    elif current_hour < 18:
        greeting = "下午好"
    else:
        greeting = "晚上好"

    print(f"{greeting}, {name}!")


# global 关键字用于在函数内部声明一个全局变量，这里修正为正确的全局变量声明
global_count = 0


def greet(name):
    global global_count  # 声明 global_count 为全局变量
    global_count += 1  # 每次调用函数时，global_count 加 1
    print(f"Hello, {name}! This is your {global_count}st/nd/rd/th visit.")


def empty_fun(): ...  # equals pass


# non-local 关键字用于在嵌套函数中声明一个非局部变量，这里修正为正确的非局部变量声明
def outer():
    count = 0  # 定义一个局部变量 count
    global_count = -1

    def inner():
        nonlocal count  # 声明 count 为非局部变量
        count += 1  # 每次调用 inner 函数时，count 加 1
        print(f"Count: {count}")

        def inner_inner():
            nonlocal global_count  # 声明 global_count 为非局部变量
            global_count += 1  # 每次调用 inner_inner 函数时，global_count 加 1
            print(f"outer Global Count: {global_count}")
            nonlocal count  # 声明 count 为非局部变量
            count += 1  # 每次调用 inner_inner 函数时，count 加 1
            print(f"Count: {count}")


def main():
    name = "tom"  # input("Enter your name:")
    greet(name)
    greet_time(name)

    c = C()
    d1, d2 = D(), D()
    e1, e2, e3 = E(), E(), E()
    c.get_count()
    d1.get_count()
    e1.get_count()
    C.get_count()

    # enum
    print([co for co in Color])  # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

    print(Grade.A)
    print(f"{Grade.B==80 = }")  # True
    print(f'{Grade.C=="C" = }')  # False
    print(Grade.A + Grade.B)  # 170

    print(Role.ADMIN)
    print(f'{Role.USER=="user" = }')  # True
    print(f'{Role.GUEST=="GUEST" = }')  # False
    print(Role.OTHER)

    # exception
    txt = "txt"
    try:
        print(float(txt))  # 抛出 ValueError 异常
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"捕获到异常：{e}")  # 捕获到异常：division by zero


def gen() -> int:
    return 1


if __name__ == "__main__":
    main()
