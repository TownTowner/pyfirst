import mysql.connector
import threading as th

db = mysql.connector.connect(
    host="localhost", user="root", password="mysql", database="reload_pudong_hy"
)
lock = th.Lock()


def update():
    print(f"update:{th.current_thread().name}")

    lock.acquire()  # 加锁
    cursor = db.cursor()
    # cursor.execute("SHOW TABLES")
    try:
        cursor.execute("update sys_user set nick_name = 'admin' where user_id = 1")
        db.commit()  # 提交事务

        print("Data updated successfully")
    except Exception as e:
        db.rollback()  # 回滚事务
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        lock.release()  # 释放锁


def read():
    print(f"read:{th.current_thread().name}")

    lock.acquire()  # 加锁
    cursor = db.cursor()
    cursor.execute("select * from sys_user where user_id = 1")
    result = cursor.fetchone()
    cursor.close()
    lock.release()  # 释放锁

    print(result)


if __name__ == "__main__":
    # update()
    t1 = th.Thread(target=update)
    t2 = th.Thread(target=read)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")

    db.close()
