import sys

# sys.path.append(r"d:\Self\pyProjects\pyfirst")  # 添加到脚本开头

import asyncio
import datetime as dt

import aiomysql
import sqlalchemy as sa
import sqlalchemy.ext.asyncio as saio
import sqlalchemy.orm as orm
from entities import SysDept, SysUser


engine = saio.create_async_engine(
    "mysql+aiomysql://root:mysql@localhost:3306/reload_pudong_hy"
)
Base = orm.declarative_base()


def initDb():
    Base.metadata.create_all(engine)


def dropDb():
    Base.metadata.drop_all(engine)


async def insertData():
    async with saio.AsyncSession(engine) as setion:
        await setion.execute(sa.insert(SysUser).values(nick_name="admin"))
        await setion.commit()


async def selectData():
    async with saio.AsyncSession(engine) as setion:
        # totaly equal to below code, but below code is more readable
        # result = await setion.execute(sa.select(SysUser).filter(SysUser.user_id >0))
        # recommanded
        # result = await setion.execute(sa.select(SysUser).where(SysUser.user_id > 0))

        # result = await setion.execute(
        #     sa.select(SysUser.user_id, SysUser.nick_name, SysUser.dept).where(
        #         SysUser.user_id > 0
        #     )
        # )
        result = await setion.execute(
            sa.select(SysDept).options(orm.joinedload(SysDept.users))
        )
        users = result.unique().fetchall()
        # users = result.unique().scalars().all()
        print(users)


async def updateData():
    async with saio.AsyncSession(engine) as setion:
        await conn.execute(
            sa.update(SysUser).where(SysUser.user_id == 1).values(nick_name="admin1")
        )
        await conn.commit()


async def deleteData():
    async with saio.AsyncSession(engine) as setion:
        await setion.execute(sa.delete(SysUser).where(SysUser.user_id == 1))
        await setion.commit()


async def main():
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)  # 创建表

    # async with engine.begin() as conn:
    #     await conn.execute(sa.insert(SysUser).values(nick_name="admin"))  # 插入数据

    # async with saio.AsyncSession(engine) as conn:
    #     result = await conn.execute(sa.select(SysUser))  # 查询数据
    #     users = result.fetchall()
    #     print(users)  # 打印结果

    await selectData()  # 查询数据

    await engine.dispose()  # 关闭连接池


if __name__ == "__main__":
    asyncio.run(main())
