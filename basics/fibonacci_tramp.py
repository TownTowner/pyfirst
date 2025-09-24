import types


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_tail(n, acc=0):
    if n <= 1:
        return acc + n
    else:
        return fibonacci_tail(n - 1, acc + n)


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


def fibonacci_yield(n, acc=0):
    """
    生成器函数，用于计算第n个斐波那契数

    ### 为什么不直接用yield？
    如果直接使用 yield fibonacci_yield(n - 1, acc + n) ，函数会返回一个生成器对象本身，而不是生成器产生的值。
    这会导致需要额外的嵌套迭代才能获取实际结果。
    而使用 yield from 可以直接将子生成器的结果 yield 出来，避免了嵌套迭代的问题。

    ### 实际效果对比
    - 使用 yield from ：调用 list(fibonacci_yeild(5)) 会直接返回 [5] （计算第5个斐波那契数）
    - 如果使用 yield ：则会返回一个嵌套的生成器对象，需要额外处理才能获取最终结果
    """
    if n <= 1:
        yield acc + n
    else:
        yield from fibonacci_yield(n - 1, acc + n)


def trampoline(f):
    def wrapper(*args, **kwargs):
        cur_f = f
        while True:
            result = cur_f(*args, **kwargs)
            if callable(result):
                cur_f = result
            else:
                return result

    return wrapper


@trampoline
def fibonacci_tramp(n, acc=0):
    if n <= 1:
        return acc + n
    else:
        return fibonacci_tramp(n - 1, acc + n)


def main():
    cnt = 100
    # print(fibonacci(cnt))
    # print(fibonacci_tail(cnt))
    print(tramp(fibonacci_yield, cnt))
    print(fibonacci_tramp(cnt))


if __name__ == "__main__":
    main()
