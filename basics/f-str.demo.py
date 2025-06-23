# :,_
n: int = 1000000000
print(f"{n:,}")
print(f"{n:_}")
print(f"{n:,d}")
print(f"{n:_d}")
print(f"{n:,f}")
print(f"{n:_f}")

# var
var: str = "hello world"
print(f"{var}")
print(f"{var:>20}:")  # 右对齐20个字符
print(f"{var:_>20}:")  # 右对齐20个字符
print(f"{var:<20}:")  # 左对齐20个字符
print(f"{var:#<20}:")  # 左对齐20个字符
print(f"{var:^20}:")  # 居中20个字符
print(f"{var:*^20}:")  # 居中20个字符，两边用*填充

print(f"{var!s}")  # =str(var)
print(f"{var!r}")  # =repr(var)

# datetime
from datetime import datetime, date, time, timedelta

now: datetime = datetime.now()
print(f"{now}")  # 输出完整的日期时间，格式为 YYYY-MM-DD HH:MM:SS.microseconds
print(f"{now:%y-%m-%d %H:%M:%S}")  # 输出简化年份的日期时间，格式为 yy-mm-dd HH:MM:SS
print(f"{now:%Y-%m-%d %H:%M:%S}")  # 输出完整年份的日期时间，格式为 YYYY-mm-dd HH:MM:SS
print(f"%c: {now:%c}")  # local version: 输出本地日期和时间的标准表示形式
print(f"%x: {now:%x}")  # 输出本地日期的标准表示形式，格式通常为 mm/dd/yy
print(f"%X: {now:%X}")  # 输出本地时间的标准表示形式，格式通常为 HH:MM:SS
print(f"%j: {now:%j}")  # 输出一年中的第几天，范围是 001 到 366
print(f"%U: {now:%U}")  # 输出一年中的第几周（以周日为一周的开始），范围是 00 到 53
print(f"%W: {now:%W}")  # 输出一年中的第几周（以周一为一周的开始），范围是 00 到 53
print(f"%V: {now:%V}")  # 输出 ISO 8601 标准的周数，范围是 01 到 53
print(f"%z: {now:%z}")  # 输出时区偏移量，格式为 ±HHMM  -> no output
print(f"%Z: {now:%Z}")  # 输出时区名称，例如 CST    -> no output
print(f"%F: {now:%F}")  # 输出完整日期，格式为 YYYY-MM-DD
print(f"%D: {now:%D}")  # 输出日期，格式为 mm/dd/yy
print(f"%T: {now:%T}")  # 输出时间，格式为 HH:MM:SS
print(f"%a: {now:%a}")  # 输出星期几的缩写，例如 Sat
print(f"%A: {now:%A}")  # 输出完整的星期几，例如 Saturday
print(f"%b: {now:%b}")  # 输出月份的缩写，例如 May
print(f"%B: {now:%B}")  # 输出完整的月份，例如 May
print(f"%m: {now:%m}")  # 输出月份，范围是 01 到 12
print(f"%d: {now:%d}")  # 输出日期，范围是 01 到 31
print(f"%H: {now:%H}")  # 输出小时（24 小时制），范围是 00 到 23
print(f"%I: {now:%I}")  # 输出小时（12 小时制），范围是 01 到 12
print(f"%p: {now:%p}")  # 输出上午或下午，例如 AM 或 PM
print(f"%M: {now:%M}")  # 输出分钟，范围是 00 到 59
print(f"%S: {now:%S}")  # 输出秒，范围是 00 到 59
print(f"%f: {now:%f}")  # 输出微秒，范围是 000000 到 999999

# format float number
f: float = 1233.5415926
print(f"float:{f:.0f}")  # 输出1234，保留0位小数
print(f"float:{f:.2f}")  # 输出1233.54，保留两位小数
print(f"float:{f:,.2f}")  # 输出1,233.54，保留两位小数
print(f"float:{f:.4f}")  # 输出1233.5416，保留四位小数
print(f"float:{f:.8f}")  # 输出1233.54159260，保留八位小数

# variable name print
a: int = 1
b: int = 2
string: str = "hello world"
print(f"{a=}")  # 输出 a=1
print(f"{b=}")  # 输出 b=2
print(f"{a + b = :d}")  # 输出 a + b = 3
print(f"{a + b = :f}")  # 输出 a + b = 3.000000
print(f"{a + b = :.2f}")  # 输出 a + b = 3.00
print(f"{string = }")  # 输出 string = 'hello world'
print(f"{string = :s}")  # 输出 string = hello world
