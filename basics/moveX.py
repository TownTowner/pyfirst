import os
import shutil
import logging
import subprocess as sp
import ctypes
import time
from datetime import datetime

# 配置参数
SOURCE_DIR = r"D:\Program Files\idm\download"  # 源目录路径
TARGET_DIR = r"E:\movies"  # 目标目录路径
KEYWORD = "X.COM"  # 文件名包含的关键字
LOG_FILE = r"D:\Programs\autoscripts\moveX\Logs\file_move.log"  # 日志文件路径
INTERVAL_SECONDS = 60  # 检查间隔（秒）


def set_hidden_attribute(file_path: str):
    """封装属性设置（含异常捕获）"""
    try:
        # 方法1：调用attrib命令
        # os.system(f'attrib +h "{file_path}"')  # 会出现cmd命令窗口一闪而过的情况
        # 方法2(推荐) 使用subprocess库（推荐）
        # startinfo = sp.STARTUPINFO()
        # startinfo.dwFlags |= sp.STARTF_USESHOWWINDOW
        # startinfo.wShowWindow = sp.SW_HIDE
        sp.run(
            ["attrib", "+h", file_path],
            check=True,
            creationflags=sp.CREATE_NO_WINDOW,
            # startupinfo=startinfo,
        )  # 不会出现cmd命令窗口
        # 方法3（可选）：使用ctypes API（注释掉上一行，取消注释以下两行）
        # FILE_ATTRIBUTE_HIDDEN = 0x02
        # ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
        logging.error(f"Failed to hide {file_path}: {str(e)}")
        # raise


def ensure_directory_exists(path):
    """确保目标目录存在"""
    if not os.path.exists(path):
        os.makedirs(path)


def move_files_with_keyword():
    """移动含关键字的文件并记录日志"""
    moved_files = []
    try:
        # 遍历源目录
        for filename in os.listdir(SOURCE_DIR):
            src_path = os.path.join(SOURCE_DIR, filename)
            # 筛选文件名包含关键字且为普通文件
            if KEYWORD.lower() in filename.lower() and os.path.isfile(src_path):
                # 步骤1：设置隐藏属性
                set_hidden_attribute(src_path)
                dest_path = os.path.join(TARGET_DIR, filename)

                shutil.move(src_path, dest_path)
                moved_files.append(filename)
                # 写入日志
                logging.info(f"Moved: {filename}")
    except Exception as e:
        logging.error(f"Error: {str(e)}")
    return moved_files


if __name__ == "__main__":
    ensure_directory_exists(TARGET_DIR)
    ensure_directory_exists(os.path.dirname(LOG_FILE))

    # 初始化日志
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
    )

    moved = move_files_with_keyword()
    cnt = len(moved)
    msg = f"Result: {cnt} file{'s' if cnt>0 else ''} was moved this time."
    if cnt > 0:
        logging.info(msg)
    print(msg)
    # time.sleep(INTERVAL_SECONDS)
