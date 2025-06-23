import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


# coroutine function
async def main():
    print(f"started at {time.strftime('%x')}")
    ret = await asyncio.gather(say_after(1, "hello"), say_after(2, "world"))
    print(ret)
    print(f"finished at {time.strftime('%x')}")

    # 3. createtask
    print("create task")
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    done, pending = await asyncio.wait([task1, task2], timeout=None)
    for task in done:
        print(task.result())  # 打印任务的返回值，即say_after函数的返回值hell
    print("create task done")

    # 4. 异步迭代器
    print("async enumrator")
    await asyncEnumrator()
    print("async enumrator done")

    # 5. 异步上下文管理器
    print("async context manager")
    await asynccontextManager()
    print("async context manager done")


# 2. asyncio v3.10+版本中，@asyncio.coroutine这个装饰器已被移除,yeild from 也应被换为await
# @asyncio.coroutine
def func1():
    print(1)
    # 网络IO请求：下载一张图片
    # yield from asyncio.sleep(2)  # 遇到Io耗时操作，自动化切换到tasks中的其他任务
    print(2)


# @asyncio.coroutine
def func2():
    print(3)
    # yield from asyncio.sleep(2)  # 遇到ro耗时操作，自动化切换到tasks中的其他任务
    print(4)


# tasks = [asyncio.ensure_future(funcl()), asyncio.ensure_future(func2())]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))


# 4. 异步迭代器
class Reader(object):
    """自定义异步迭代器（同时也是异步可迭代对象）"""

    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 5:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val


# -async for- must be used in async function
async def asyncEnumrator():
    obj = Reader()
    async for item in obj:
        print(item)


class AsynccontextManager:
    def __init__(self):
        self.conn = "connectString"

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # 异步关闭数据库链接
        await asyncio.sleep(1)


async def asynccontextManager():
    async with AsynccontextManager() as f:
        result = await f.do_something()
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
