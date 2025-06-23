"""
entities模块的初始化文件，用于集中导入所有实体类
"""

from .SysUser import SysUser
from .SysDept import SysDept
from .Base import Base

__all__ = ["SysUser", "SysDept", "Base"]
