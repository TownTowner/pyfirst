import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime as dt
from .Base import Base

# from .SysDept import SysDept


class SysUser(Base):
    __tablename__ = "sys_user"
    __mapper_args__ = {"eager_defaults": True}  # 避免异步映射冲突
    user_id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    dept_id = sa.Column(sa.BigInteger, sa.ForeignKey("sys_dept.dept_id"))
    user_name = sa.Column(sa.String(30), nullable=False)
    nick_name = sa.Column(sa.String(30), nullable=False)
    create_time = sa.Column(sa.DateTime, nullable=False, default=dt.datetime.now)

    dept = orm.relationship("SysDept", back_populates="users", lazy="selectin")

    def __repr__(self):
        return f"<SysUser(user_id={self.user_id}, nick_name={self.nick_name}, create_time={self.create_time})>"
