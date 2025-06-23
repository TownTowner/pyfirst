import asyncio
import aiomysql


async def execute(host, password):
    print("开始", host)
    # 网络10操作：先去连接47.93.40.197,遇到10则自动切换任务,去连接47.93.40.198：6379
    async with aiomysql.connect(
        host=host, port=3306, user="root", password=password, db="mysql"
    ) as conn:
        print("连接成功", host)
        # 网络I0操作：遇到I0会自动切换任务
        async with conn.cursor() as cur:
            # 网络I0操作：遇到I0会自动切换任务
            await cur.execute("SELECT Host,User From user")
            # 网络I0操作：遇到I0会自动切换任务
            result = await cur.fetchall()
            print(result)
    print("结束", host)


async def main():
    await asyncio.gather(execute("127.0.0.1", "mysql"), execute("127.0.0.1", "mysql"))


if __name__ == "__main__":
    asyncio.run(main())
