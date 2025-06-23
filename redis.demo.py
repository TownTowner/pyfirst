import asyncio
from redis.asyncio import Redis  # 使用新版本的导入方式


async def execute(address, password):
    print("开始执行", address)
    # 使用新版本的Redis客户端创建方式
    redis = Redis.from_url(address, password=password)
    print("ping:", await redis.ping())
    # print(await redis.connection.check_health())
    # 设置哈希值
    await redis.hmset("car", mapping={"key1": "1", "key2": "2", "key3": "3"})
    # 获取所有哈希值
    result = await redis.hgetall("car")
    print(result)
    await redis.aclose()
    print("结束", address)


if __name__ == "__main__":
    asyncio.run(execute("redis://127.0.0.1:6379", None))
