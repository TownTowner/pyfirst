import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime as dt
from .Base import Base


class SysDept(Base):
    __tablename__ = "sys_dept"
    __mapper_args__ = {"eager_defaults": True}  # 避免异步映射冲突
    dept_id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    parent_id = sa.Column(sa.BigInteger, sa.ForeignKey("sys_dept.dept_id"))
    dept_name = sa.Column(sa.String(30))
    order_num = sa.Column(sa.Integer)
    create_time = sa.Column(sa.DateTime, nullable=False, default=dt.datetime.now)

    users = orm.relationship("SysUser", back_populates="dept")

    def __repr__(self):
        _userstr = ",".join([f"{u}" for u in self.users])
        return f"<SysDept(dept_id={self.dept_id}, dept_name={self.dept_name}, create_time={self.create_time}, users={_userstr})>"
