# abs
print("abs:", abs(10))  # 输出 10，计算绝对值
print("abs:", abs(-10))  # 输出 10，计算绝对值
print("abs:", abs(10.5))  # 输出 10.5，计算绝对值
print("abs:", abs(-10.5))  # 输出 10.5，计算绝对值
print("abs:", abs(3 + 4j))  # 输出 5.0，计算复数的模


# all,any
nums1 = [1, 1, 1, 0, 1]
nums2 = [0, 0, 0, 0, 0]
nums3 = [1, 1, 1, 1, 1]
print(f"all:{ all(nums1)=}")  # 输出 False，至少有一个元素为假
print(f"all:{ all(nums2)=}")  # 输出 False，至少有一个元素为假
print(f"all:{ all(nums3)=}")  # 输出 True，所有元素都为真
print(f"any:{ any(nums1)=}")  # 输出 True，至少有一个元素为真
print(f"any:{ any(nums2)=}")  # 输出 False，所有元素都为假
print(f"any:{ any(nums3)=}")  # 输出 True，所有元素都为真


# ascii
print("ascii:", ascii("hello"))  # 输出 'hello'，将字符串转换为 ASCII 表示
print("ascii:", ascii("你好"))  # 输出 "'\u4f60\u597d'"，将字符串转换为 ASCII 表示
print("ascii:", ascii(123))  # 输出 123，不进行转换
print("ascii:", ascii(123.45))  # 输出 123.45，不进行转换
print("ascii:", ascii([1, 2, 3]))  # 输出 [1, 2, 3]，不进行转换
print("ascii:", ascii((1, 2, 3)))  # 输出 (1, 2, 3)，不进行转换
print("ascii:", ascii({"a": 1, "b": 2}))  # 输出 {'a': 1, 'b': 2}，不进行转换

# bin,oct,hex
print("bin:", bin(10))  # 输出 '0b1010'，将十进制数转换为二进制表示
print("oct:", oct(10))  # 输出 '0o12'，将十进制数转换为八进制表示
print("hex:", hex(10))  # 输出 '0xa'，将十进制数转换为十六进制表示
print("bin:", bin(0b1010))  # 输出 '0b1010'，将二进制数转换为二进制表示
print("oct:", oct(0o12))  # 输出 '0o12'，将八进制数转换为八进制表示
print("hex:", hex(0xA))  # 输出 '0xa'，将十六进制数转换为十六进制表示

# bool
print("bool:", bool(1))  # 输出 True，将非零值转换为布尔值 True
print("bool:", bool(0))  # 输出 False，将零值转换为布尔值 False
print("bool:", bool("hello"))  # 输出 True，将非空字符串转换为布尔值 True
print("bool:", bool(""))  # 输出 False，将空字符串转换为布尔值 False
print("bool:", bool([]))  # 输出 False，将空列表转换为布尔值 False
print("bool:", bool([1, 2, 3]))  # 输出 True，将非空列表转换为布尔值 True
print("bool:", bool(()))  # 输出 False，将空元组转换为布尔值 False
print("bool:", bool((1, 2, 3)))  # 输出 True，将非空元组转换为布尔值 True
print("bool:", bool({}))  # 输出 False，将空字典转换为布尔值 False
print("bool:", bool({"a": 1, "b": 2}))  # 输出 True，将非空字典转换为布尔值 True
print("bool:", bool(None))  # 输出 False，将 None 转换为布尔值 False

# float
print(f"float:{ float(10) = }")  # 输出 10.0，将整数转换为浮点数
print(f"float:{ float(10.5) = }")  # 输出 10.5，将浮点数转换为浮点数
print(f"float:{ float('10') = }")  # 输出 10.0，将字符串转换为浮点数

# int
print(f"int:{ int(10.5) = }")  # 输出 10，将浮点数转换为整数
print(f"int:{ int('10') = }")  # 输出 10，将字符串转换为整数
# print(f"int:{ int('10.5') = }")  # 输出 error: ValueError: invalid literal for int() with base 10: '10.5'
print(f"int:{ int('10', 10) = }")  # 输出 10，将字符串转换为整数，指定进制为 10
print(f"int:{ int('10', 8) = }")  # 输出 8，将字符串转换为整数，指定进制为 8
print(f"int:{ int('10', 16) = }")  # 输出 16，将字符串转换为整数，指定进制为 16

# str
print(f"str:{ str(10) = }")  # 输出 '10'，将整数转换为字符串
print(f"str:{ str(10.5) = }")  # 输出 '10.5'，将浮点数转换为字符串
print(f"str:{ str([1, 2, 3]) = }")  # 输出 '[1, 2, 3]'，将列表转换为字符串
print(f"str:{ str((1, 2, 3)) = }")  # 输出 '(1, 2, 3)'，将元组转换为字符串
print(f"str:{ str({'a': 1, 'b': 2}) = }")  # 输出 "{'a': 1, 'b': 2}"，将字典转换为字符串
print(f"str:{ str(None) = }")  # 输出 'None'，将 None 转换为字符串

# tuple
print(f"tuple:{ tuple([1, 2, 3]) = }")  # 输出 (1, 2, 3)，将列表转换为元组
print(f"tuple:{ tuple((1, 2, 3)) = }")  # 输出 (1, 2, 3)，将元组转换为元组
print(f"tuple:{ tuple({'a': 1, 'b': 2}) = }")  # 输出 ('a', 'b')，将字典转换为元组
print(
    f"tuple:{ tuple('hello') = }"
)  # 输出 ('h', 'e', 'l', 'l', 'o')，将字符串转换为元组
print(f"tuple:{ tuple(range(5)) = }")  # 输出 (0, 1, 2, 3, 4)，将 range 对象转换为元组


# callable
def func():
    pass


print("callable:", callable(func))  # 输出 True，函数是可调用的
print("callable:", callable(123))  # 输出 False，整数不是可调用的
print("callable:", callable("hello"))  # 输出 False，字符串不是可调用的
print("callable:", callable([1, 2, 3]))  # 输出 False，列表不是可调用的
print("callable:", callable((1, 2, 3)))  # 输出 False，元组不是可调用的
print("callable:", callable({"a": 1, "b": 2}))  # 输出 False，字典不是可调用的
print("callable:", callable(None))  # 输出 False，None 不是可调用的

# chr,ord
print(f"chr:{ chr(65) = }")  # 输出 'A'，将 ASCII 码转换为对应的字符
print(f"chr:{ chr(97) = }")  # 输出 'a'，将 ASCII 码转换为对应的字符

# complex
print(f"complex:{ complex(1, 2) = }")  # 输出 (1+2j)，创建一个复数
print(f"complex:{ complex('2+3j') = }")  # 输出 (2+3j)，创建一个复数
print(f"complex:{ complex(1, 2) + complex(3, 4) = }")  # 输出 (4+6j)，复数加法
print(f"complex:{ complex(1, 2) * complex(3, 4) = }")  # 输出 (-5+10j)，复数乘法
print(f"complex:{ complex(1, 2) / complex(3, 4) = }")  # 输出 (0.44+0.08j)，复数除法
print(f"complex:{ complex(1, 2) ** 2 = }")  # 输出 (-3+4j)，复数的平方

# dict
print(f"dict:{ dict(a=1, b=2) = }")  # 输出 {'a': 1, 'b': 2}，创建一个字典
# print(f"dict:{ dict(['a','b']) = }")  # 输出 error: ValueError: dictionary update sequence element #0 has length 1; 2 is required
print(f"dict:{ dict(['a1','b2']) = }")  # 输出 {'a': 1, 'b': 2}，创建一个字典
print(f"dict:{ dict(['aX','bY']) = }")  # 输出 {'a': 'X', 'b': 'Y'}，创建一个字典
# print(f"dict:{ dict(['aXx','bYY']) = }")  # 输出 error:ValueError: dictionary update sequence element #0 has length 3; 2 is required
print(f"dict:{ dict([('a', 1), ('b', 2)]) = }")  # 输出 {'a': 1, 'b': 2}，创建一个字典

# dir
# 输出 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'func', 'nums1', 'nums2', 'nums3'] ，
# 返回当前模块的属性列表
print(f"dir:{dir() = }")

# enumerate
# 输出 [(0, 'a'), (1, 'b'), (2, 'c')] ，返回一个枚举对象，包含索引和对应的值
print(f"enumerate:{ list(enumerate(['a', 'b', 'c'])) = }")
print(
    f"enumerate:{ list(enumerate(['a', 'b', 'c'],start=1)) = }"
)  # 输出 [(1, 'a'), (2, 'b'), (3, 'c')] ，返回一个枚举对象，包含索引和对应的值

# eval
print(f"eval:{ eval('1+2+3') = }")  # 输出 6 ，将字符串 '1+2+3' 作为表达式进行求值
print(f"eval:{ eval('1+2*3') = }")  # 输出 10 ，将字符串 '1+2*3' 作为表达式进行求值

# freezenset
print(
    f"freezenset:{ frozenset([1, 2, 3]) = }"
)  # 输出 frozenset({1, 2, 3}) ，创建一个不可变集合

# globals,locals
print(f"globals:{ globals() = }")  # 输出当前全局命名空间的字典
print(f"locals:{ locals() = }")  # 输出当前局部命名空间的字典


def func():
    a = 1
    b = "hello"
    print(f"func globals:{ globals() = }")  # 输出当前全局命名空间的字典
    print(f"func locals:{ locals() = }")  # 输出当前局部命名空间的字典
    print(f"func locals:{ locals()['a'] = }")  # 输出 1 ，获取局部变量 a 的值
    print(f"func locals:{ locals()['b'] = }")  # 输出 2 ，获取局部变量 b 的值


func()  # 调用函数 func()，输出局部命名空间的字典和局部变量的值

# hash
print(f"hash:{ hash(1) = }")  # 输出 1 ，返回整数 1 的哈希值
print(
    f"hash:{ hash('hello') = }"
)  # 输出 -3713666314749854759 ，返回字符串 'hello' 的哈希值
print(
    f"hash:{ hash((1, 2, 3)) = }"
)  # 输出 529344067295497451 ，返回元组 (1, 2, 3) 的哈希值
# print(f"hash:{ hash([1, 2, 3]) = }")  # 输出 error: TypeError: unhashable type: 'list' ，列表是不可哈希的

# help
help(print)  # 输出help(print)的帮助文档
print(f"help:{ help(print) = }")
# 先输出help(print)的帮助文档,
# 再输出 help: help(print) = None

print(f"help:{ help(print.__doc__) = }")
# 先输出：
# No Python documentation found for
# 'Prints the values to a stream, or to sys.stdout by default.
#     sep
#       string inserted between values, default a space.
#    end
#        string appended after the last value, default a newline.
#    file
#        a file-like object (stream); defaults to the current sys.stdout.
#    flush
#        whether to forcibly flush the stream.'.
# Use help() to get the interactive help utility.
# Use help(str) for help on the str class.
# 再输出 help: help(print.__doc__) = None

# id
ida = 1
idlist1 = [1, 2, 3]
idlist2 = idlist1
print(f"id:{ id(ida) = }")  # 输出 140703556037048 ，返回对象的唯一标识符
print(f"id:{ id(1) = }")  # 输出 140703556037048 ，返回对象的唯一标识符
print(f"id:{ id('hello') = }")  # 输出 2182512712640 ，返回对象的唯一标识符
print(f"id:{ id('hello') = }")  # 输出 2182512712640 ，返回对象的唯一标识符
print(f"id:{ id(idlist1) = }")  # 输出 2397783395648 ，返回对象的唯一标识符
print(f"id:{ id(idlist2) = }")  # 输出 2397783395648 ，返回对象的唯一标识符

# isinstance
print(
    f"isinstance:{ isinstance(1, int) = }"
)  # 输出 True ，判断对象是否是指定类型的实例
print(
    f"isinstance:{ isinstance(1, float) = }"
)  # 输出 False ，判断对象是否是指定类型的实例
print(
    f"isinstance:{ isinstance(1, str) = }"
)  # 输出 False ，判断对象是否是指定类型的实例
print(
    f"isinstance:{ isinstance(1, (int, float)) = }"
)  # 输出 True ，判断对象是否是指定类型的实例
print(
    f"isinstance:{ isinstance(1, (int, float, str)) = }"
)  # 输出 True ，判断对象是否是指定类型的实例 , this is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.


# issubclass
class A:
    pass


class B(A):
    pass


print(
    f"issubclass:{ issubclass(int, object) = }"
)  # 输出 True ，判断一个类是否是另一个类的子类

print(
    f"issubclass:{ issubclass(B, A) = }"
)  # 输出 True ，判断一个类是否是另一个类的子类

# iter,next
it = iter([1, 2, 3])  # 创建一个迭代器对象，包含列表 [1, 2, 3] 的元素
print(f"iter:{ next(it) = }")  # 输出 1 ，获取迭代器的下一个元素
print(f"iter:{ next(it) = }")  # 输出 2 ，获取迭代器的下一个元素
print(f"iter:{ next(it) = }")  # 输出 3 ，获取迭代器的下一个元素
# print(f"iter:{ next(it) = }")  # 输出 error: StopIteration ，迭代器中没有更多的元素，抛出 StopIteration 异常

# len
print(f"len:{ len([1, 2, 3]) = }")  # 输出 3 ，返回对象的长度
print(f"len:{ len('hello') = }")  # 输出 5 ，返回对象的长度
print(f"len:{ len({'a': 1, 'b': 2}) = }")  # 输出 2 ，返回对象的长度
print(f"len:{ len(range(1, 10)) = }")  # 输出 9 ，返回对象的长度

# list
print(f"list:{ list([1, 2, 3]) = }")  # 输出 [1, 2, 3] ，将可迭代对象转换为列表
print(
    f"list:{ list('hello') = }"
)  # 输出 ['h', 'e', 'l', 'l', 'o'] ，将字符串转换为列表
print(f"list:{ list({'a': 1, 'b': 2}) = }")  # 输出 ['a', 'b'] ，将字典的键转换为列表
print(
    f"list:{ list(range(1, 10)) = }"
)  # 输出 [1, 2, 3, 4, 5, 6, 7, 8, 9] ，将 range 对象转换为列表

# map
print(
    f"map:{ list(map(lambda x: x * 2, [1, 2, 3])) = }"
)  # 输出 [2, 4, 6] ，将函数应用于可迭代对象的每个元素，并返回一个新的迭代器

# pow
print(f"pow:{ pow(2, 3) = }")  # 输出 8 ，计算 2 的 3 次方
print(f"pow:{ pow(2, 3, 5) = }")  # 输出 3 ，计算 2 的 3 次方对 5 取模的结果
print(f"pow:{ pow(2, -3) = }")  # 输出 0.125 ，计算 2 的 -3 次方
print(f"pow:{ pow(2, -3, 5) = }")  # 输出 3 ，计算 2 的 -3 次方对 5 取模的结果

# print
plist = ["ming", "an", "lei"]
print(
    f"print:{ print(*plist,sep='//', end='\n') = }"
)  # 输出 ming//an//lei ，将列表中的元素以//分隔，并以换行符结束

# range
print(
    f"range:{ list(range(1, 10)) = }"
)  # 输出 [1, 2, 3, 4, 5, 6, 7, 8, 9] ，创建一个 range 对象，包含从 1 到 9 的整数
print(
    f"range:{ list(range(1, 10, 2)) = }"
)  # 输出 [1, 3, 5, 7, 9] ，创建一个 range 对象，包含从 1 到 9 的奇数
print(
    f"range:{ list(range(10, 0, -1)) = }"
)  # 输出 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] ，创建一个 range 对象，包含从 10 到 1 的整数

# reversed
rlist = [1, 2, 3, 4, 5]
print(
    f"reversed:{ list(reversed(rlist)) = }"
)  # 输出 [5, 4, 3, 2, 1] ，将可迭代对象反转
print(f"reversed:{ rlist[::-1] = }")  # 输出 [5, 4, 3, 2, 1] ，将可迭代对象反转

# round
print(
    f"round:{ round(351.23456, 2) = }"
)  # 输出 351.23 ，将浮点数 351.23456 四舍五入到小数点后两位
print(
    f"round:{ round(351.23456, 3) = }"
)  # 输出 351.235 ，将浮点数 351.23456 四舍五入到小数点后三位
print(
    f"round:{ round(351.23456, 0) = }"
)  # 输出 351.0 ，将浮点数 351.23456 四舍五入到整数
print(
    f"round:{ round(351.23456, -1) = }"
)  # 输出 350.0 ，将浮点数 351.23456 四舍五入到小数点前一位
print(
    f"round:{ round(351.23456, -2) = }"
)  # 输出 400.0 ，将浮点数 351.23456 四舍五入到小数点前两位

# set
slist = [1, 2, 3, 1, 2, 4]
print(
    f"set:{ set([1, 2, 3, 4, 5]) = }"
)  # 输出 {1, 2, 3, 4, 5} ，将可迭代对象转换为集合
print(f"set:{ set(slist) = }")  # 输出 {1, 2, 3, 4} ，将可迭代对象转换为集合
print(f"set:{ set('hello') = }")  # 输出 {'h', 'e', 'l', 'o'} ，将字符串转换为集合
print(f"set:{ set(('a', 'b', 'c')) = }")  # 输出 {'a', 'b', 'c'} ，将元组转换为集合
print(f"set:{ set({'a': 1, 'b': 2}) = }")  # 输出 {'a', 'b'} ，将字典的键转换为集合

# slice
print(
    f"slice:{ list(range(1, 10))[slice(1, 5)] = }"
)  # 输出 [2, 3, 4, 5] ，使用切片操作获取列表中的元素

# sorted
print(
    f"sorted:{ sorted([-1,10,0,7,1, 2, 3, 4, 5]) = }"
)  # 输出 [-1, 0, 1, 2, 3, 4, 5, 7, 10] ，将可迭代对象排序

# type
print(f"type:{ type(1) = }")  # 输出 <class 'int'> ，返回对象的类型
print(f"type:{ type(1.0) = }")  # 输出 <class 'float'> ，返回对象的类型
print(f"type:{ type('hello') = }")  # 输出 <class 'str'> ，返回对象的类型
print(f"type:{ type([1, 2, 3]) = }")  # 输出 <class 'list'> ，返回对象的类型
print(f"type:{ type((1, 2, 3)) = }")  # 输出 <class 'tuple'> ，返回对象的类型
print(f"type:{ type({'a': 1, 'b': 2}) = }")  # 输出 <class 'dict'> ，返回对象的类型
print(f"type:{ type(None) = }")  # 输出 <class 'NoneType'> ，返回对象的类型
print(f"type:{ type(True) = }")  # 输出 <class 'bool'> ，返回对象的类型
print(f"type:{ type(1 + 2j) = }")  # 输出 <class 'complex'> ，返回对象的类型

# zip
print(
    f"zip:{ list(zip([1, 2], ['a', 'b', 'c'])) = }"
)  # 输出 [(1, 'a'), (2, 'b')] ，使用最短的元素长度
# print(f"zip:{ list(zip([1, 2], ['a', 'b', 'c'],strict=True)) = }")  # 输出 error:ValueError: zip() argument 2 is longer than argument 1
print(
    f"zip:{ list(zip([1, 2, 3], ['a', 'b', 'c'])) = }"
)  # 输出 [(1, 'a'), (2, 'b'), (3, 'c')] ，将多个可迭代对象的元素组合成一个新的迭代器
print(
    f"zip:{ list(zip([1, 2, 3], ['a', 'b', 'c'], [True, False, True])) = }"
)  # 输出 [(1, 'a', True), (2, 'b', False), (3, 'c', True)] ，将多个可迭代对象的元素组合成一个新的迭代器
