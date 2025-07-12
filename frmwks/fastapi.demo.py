import asyncio
import uvicorn
from redis.asyncio import Redis, ConnectionPool
from fastapi import FastAPI

app = FastAPI()

# default connect kwargs: redis://localhost:6379
REDIS_POOL = ConnectionPool(password=None, max_connections=10)


@app.get("/")
def index():
    """HWI普通操作接口"""
    return {"message": "Hello world"}


@app.get("/red")
async def red():
    """异步操作接口"""
    print("请求来了")
    await asyncio.sleep(3)

    # 连接池获取一个连接
    redis = Redis(connection_pool=REDIS_POOL)
    # 设置值
    await redis.hmset("car", mapping={"key1": "1", "key2": "2", "key3": "3"})
    # 读取值
    result = await redis.hgetall("car")
    print(result)
    ## 连接归还连接池
    # await REDIS_POOL.release(conn)
    return result


if __name__ == "__main__":
    uvicorn.run("fastapidemo:app", host="127.0.0.1", port=5000, log_level="info")
