

### re.split()

```python
def split(pattern, string, maxsplit=0, flags=0):
    """Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list."""
    return _compile(pattern, flags).split(string, maxsplit)

print(re.split(',', 'a,b,c'))
结果:
['a', 'b', 'c']
print(re.split(',', 'a,b,c'))
结果:
['a', ',', 'b', ',', 'c']
```



### 链式调用属性

在学习廖雪峰Python教程中，学习到定制类__getattr__，具体用法见

廖雪峰教程。

利用完全动态的`__getattr__`，我们可以写出一个链式调用：

```python
class Chain(object):
 
    def __init__(self, path=''):
        self._path = path
 
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
 
    def __str__(self):
        return self._path
```



试试：

```python
>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
```

这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！ 

在调用时`Chain().status.user.timeline.list`中每一个"."就是一次调用`__getattr__`方法。所以就可以理解为什么在输入时要使用xx.xx的格式



### 链式调用方法

其实只要每一次调用方法后，返回的数据类型不变，那么就可以实现链式调用。比如在django中：

```python
>>> Task.objects.all() # 返回的是一个QuerySet对象
<QuerySet [<Task: Task object>, <Task: Task object>, <Task: Task object>, <Task: Task object>]>
>>> Task.objects.filter(completed=1).filter(id=7)
<QuerySet [<Task: Task object>]>
# 因为每次调用filter()后返回的结果都是QuerySet类型，故可以链式调用filter()方法
>>> Task.objects.first()
<Task: Task object> # 返回一个Task对象
```

但是对于list，就很难使用链式调用

```python
>>> l = [1, 2, 3]
>>> l.append(4) # 无返回值，故无法实现链式调用
```





### 一个类继承list，那么打印其对象时也会是[]

```python
class seq(list):
    pass


s = seq([1, 2, 3])
print(s)
结果:
[1, 2, 3]
l = []
l.append(s)
print(l)
[[1, 2, 3]]
```

```python
class seq(list):
    def __str__(self):
        return 'a'


s = seq([1, 2, 3])
print(s)
结果：
'a'
l = []
l.append(s)
print(l)
结果:
[[1, 2, 3]]
```

相当于是list的`__str__`方法和`__repr__`方法产生了打印列表能显示[]的效果。



### 类里面执行语句

```python
class A:
    print(1)  
结果:
1
```

```python
class A:
    print(__name__)
结果:
__main__
```

```python
class A:
    print(A.__name__)
结果:
NameError: name 'A' is not defined
```

```python
class A:
    print(__dict__)
结果:
NameError: name '__dict__' is not defined
```





### 动态添加属性和方法及\_\_slots\_\_

------

正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

```python
class Student(object):
    pass
```

然后，尝试给实例绑定一个属性：

```python
>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael
```

还可以尝试给实例绑定一个方法：

```python
>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25
```

但是，给一个实例绑定的方法，对另一个实例是不起作用的：

```python
>>> s2 = Student() # 创建新的实例
>>> s2.set_age(25) # 尝试调用方法
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
```

为了给所有实例都绑定方法，可以给class绑定方法：

```python
>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score
```

给class绑定方法后，所有实例均可调用：

```python
>>> s.set_score(100)
>>> s.score
100
>>> s2.set_score(99)
>>> s2.score
99
```

通常情况下，上面的`set_score`方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

#### 使用\_\_slots\_\_

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加`name`和`age`属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

然后，我们试试：

```python
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```

由于`'score'`没有被放到`__slots__`中，所以不能绑定`score`属性，试图绑定`score`将得到`AttributeError`的错误。

使用`__slots__`要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

```python
>>> class GraduateStudent(Student):
...     pass
...
>>> g = GraduateStudent()
>>> g.score = 9999
```

除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。                     

​																	——廖雪峰python教程

 

### while只是跳出离当前最近的一次循环

```python
n = 5
while n > 0:
    while True:
        break
    print(1)
    n -= 1
结果:
1
1
1
1
1
```



### 在不知道需要使用几次循环的情况下可以使用while语句



### 输出字符串中对称的子字符串的最大长度

![699524491](/home/andy/Desktop/Notes/699524491.jpg)

```python
# 这里先只考虑偶数个字符串的对称情况
# 初稿 循环写的有点混乱，可读性较差
def count_sym(s):
    length = len(s)
    list_s = []
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            count = 2
            key = 2 * i + 1
            while i - 1 >= 0 and key - i + 1 <= length - 1:
                i = i - 1
                if s[i] != s[key - i]:
                    break
                count += 2
            list_s.append(count)
    return max(list_s)
```



```python
# 代码重构后，使代码可读性增强，更加清晰
def count_sym(s):
    length = len(s)
    list_s = []
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            count = 2
            total = i + (i + 1)
            while True:
                i = i - 1
                if i < 0 or total - i == length or s[i] != s[total - i]:
                    break
                count += 2
            list_s.append(count)
    return max(list_s)
```



### \_\_new\_\_方法

> __new__() 函数只能用于从object继承的新式类。
>
>  
>
> 先看下object类中对__new__()方法的定义：
>
> ```python
> class object:
>   @staticmethod # known case of __new__
>   def __new__(cls, *more): # known special case of object.__new__
>     """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
>     pass
> ```
>
> 
>
> object将__new__()方法定义为静态方法，并且至少需要传递一个参数cls，cls表示需要实例化的类，此参数在实例化时由Python解释器自动提供。
>
> 我们来看下下面类中对__new__()方法的实现：
>
> ```python
> class Demo(object):
>   def __init__(self):
>     print '__init__() called...'
>  
>   def __new__(cls, *args, **kwargs):
>     print '__new__() - {cls}'.format(cls=cls）
>     return object.__new__(cls, *args, **kwargs)
>  
> if __name__ == '__main__':
>   de = Demo()
> ```
>
> 
>
> 输出：
>
> 发现实例化对象的时候，调用__init__()初始化之前，先调用了__new__()方法
>
> __new__()必须要有返回值，返回实例化出来的实例，需要注意的是，可以return父类__new__()出来的实例，也可以直接将object的__new__()出来的实例返回。
>
> __init__()有一个参数self，该self参数就是__new__()返回的实例，__init__()在__new__()的基础上可以完成一些其它初始化的动作，__init__()不需要返回值。
>
> 若__new__()没有正确返回当前类cls的实例，那__init__()将不会被调用，即使是父类的实例也不行。
>
> 我们可以将类比作制造商，__new__()方法就是前期的原材料购买环节，__init__()方法就是在有原材料的基础上，加工，初始化商品环节。
>
> 实际应用过程中，我们可以这么使用：
>
> ```python
> class LxmlDocument(object_ref):
>   cache = weakref.WeakKeyDictionary()
>   __slots__ = ['__weakref__']
>  
>   def __new__(cls, response, parser=etree.HTMLParser):
>     cache = cls.cache.setdefault(response, {})
>     if parser not in cache:
>       obj = object_ref.__new__(cls)
>       cache[parser] = _factory(response, parser)
>     return cache[parser]
> ```
>
> 
>
> 该类中的__new__()方法的使用，就是再进行初始化之前，检查缓存中是否存在该对象，如果存在则将缓存存放对象直接返回，如果不存在，则将对象放至缓存中，供下次使用。
>
>  
>
> 再来个单例的，通过重载__new__实现单例：
>
> ```python
> class Singleton(object):
>     def __new__(cls, *args, **kwargs):
>         if not hasattr(cls, '_instance'):
>             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
>         return cls._instanc
> ```



```python
class seq(list):
    pass


a = seq.__new__(seq)
b = list.__new__(seq)
print(a)
print(type(a))
print(b)
print(type(b))
结果:
[]
<class '__main__.seq'>
[]
<class '__main__.seq'>
# 但是
c = object.__new__(seq)
结果:
TypeError: object.__new__(seq) is not safe, use seq.__new__()
```

所以直接类名.\_\_new\_\_(类名)和父类名.\_\_new\_\_(类名都可以创建出实例。



### python中\_\_all\_\_的用法

>## 用 \_\_all\_\_ 暴露接口
>
>Python 可以在模块级别暴露接口：
>
>```python
>__all__ = ["foo", "bar"]
>```
>
>很多时候这么做还是很有好处的……
>
>### 提供了哪些是公开接口的约定
>
>不像 Ruby 或者 Java，Python 没有语言原生的可见性控制，而是靠一套需要大家自觉遵守的”约定“下工作。比如下划线开头的应该对外部不可见。同样，`__all__` 也是对于模块公开接口的一种约定，比起下划线，`__all__` 提供了暴露接口用的”白名单“。一些不以下划线开头的变量（比如从其他地方 `import` 到当前模块的成员）可以同样被排除出去。
>
>```python
>import os
>import sys
>
>__all__ = ["process_xxx"]  # 排除了 `os` 和 `sys`
>
>
>def process_xxx():
>    pass  # omit
>```
>
>### 控制 from xxx import * 的行为
>
>代码中当然是不提倡用 `from xxx import *` 的写法的，但是在 console 调试的时候图个方便还是很常见的。如果一个模块 `spam` 没有定义 `__all__`，执行 `from spam import *` 的时候会将 `spam` 中非下划线开头的成员都导入当前命名空间中，这样当然就有可能弄脏当前命名空间。如果显式声明了 `__all__`，`import *` 就只会导入 `__all__` 列出的成员。如果 `__all__` 定义有误，列出的成员不存在，还会明确地抛出异常，而不是默默忽略。
>
>### 为 lint 工具提供辅助
>
>编写一个库的时候，经常会在 `__init__.py` 中暴露整个包的 API，而这些 API 的实现可能是在包中其他模块中定义的。如果我们仅仅这样写：
>
>```python
>from foo.bar import Spam, Egg
>```
>
>一些代码检查工具，如 `pyflakes` 就会报错，认为 `Spam` 和 `Egg` 是 `import` 了又没被使用的变量。当然一个可行的方法是把这个警告压掉：
>
>```python
>from foo.bar import Spam, Egg  # noqa
>```
>
>但是更好的方法是显式定义 `__all__`，这样代码检查工具会理解这层意思，就不再报 `unused variables` 的警告：
>
>```python
>from foo.bar import Spam, Egg
>
>__all__ = ["Spam", "Egg"]
>```
>
>需要注意的是大部分情况下 `__all__` 都是一个 `list`，而不是 `tuple` 或者其他序列类型。如果写了其他类型的 `__all__`，如无意外 `pyflakes` 等 lint 工具会无法识别出。
>
>### 定义 \_\_all\_\_ 需要注意的地方
>
>- 如上所述，`__all__` 应该是 `list` 类型的
>- 不应该动态生成 `__all__`，比如使用列表解析式。`__all__` 的作用就是定义公开接口，如果不以字面量的形式显式写出来，就失去意义了。
>- 即使有了 `__all__` 也不应该在非临时代码中使用 `from xxx import *` 语法，或者用元编程手段模拟 Ruby 的自动 `import`。Python 不像 Ruby，没有 `Module` 这种成员，模块就是命名空间隔离的执行者。如果打破了这一层，而且引入诸多动态因素，生产环境跑的代码就充满了不确定性，调试也会非常困难。
>- 按照 PEP8 建议的风格，`__all__` 应该写在所有 `import` 语句下面，和函数、常量等模块成员定义的上面。
>
>如果一个模块需要暴露的接口改动频繁，`__all__` 可以这样定义：
>
>```python
>__all__ = [
>    "foo",
>    "bar",
>    "egg",
>]
>```
>
>最后多出来的逗号在 Python 中是允许的，也是符合 PEP8 风格的。这样修改一个接口的暴露就只修改一行，方便版本控制的时候看 `diff`。



### 导入问题

```python
test.py
def b():
    print('hello')

print(1)
```

```python
1.py
import test

结果:
1
```

```python
2.py
from test import b

结果:
1
```

`from test import b`这种情况也会运行test.py这个模块，运行后输出1.



如果把test.py改为

```python
test.py
import os
__all__ = ['b']
def b():
    print('hello')
a = 1
```

```python
3.py
from test import *
# 那么除了b之外的os和a都不能调用
print(a)
结果:
NameError: name 'a' is not defined
```

```python
4.py
import test
print(test.os)
print(test.a)
print(test.b)
结果:
<module 'os' from '/usr/lib/python3.6/os.py'>
1
<function b at 0x7fae870340d0>
# 均可调用
```



### bytes类字符串的方法和字符串的方法基本相同

但是比如split方法，在切割bytes类型的字符串时也需要用bytes类字符串切割符

```python
b = b'aabj,s,b'
print(b.split(b','))
结果:
[b'aabj', b's', b'b']
```



### Python 字典(Dictionary) fromkeys()方法

>------
>
>#### 描述
>
>Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。是字典的一个静态方法。
>
>#### 语法
>
>fromkeys()方法语法：
>
>```
>dict.fromkeys(seq[, value])
>```
>
>#### 参数
>
>- seq -- 字典键值列表。
>- value -- 可选参数, 设置键序列（seq）的值。
>
>#### 返回值
>
>该方法返回一个新字典。
>
>#### 实例
>
>以下实例展示了 fromkeys()函数的使用方法：
>
>#### 实例(Python 2.0+)
>
>```python
>#!/usr/bin/python
># -*- coding: UTF-8 -*-
>
>seq = ('Google', 'Runoob', 'Taobao')
>
>d1 = dict.fromkeys(seq)
>print("新字典为 : %s" % str(d1))
>
>d2 = dict.fromkeys(seq, 10)
>print("新字典为 : %s" % str(d2))
>```
>
>
>
>以上实例输出结果为：
>
>```
>新字典为 : {'Google': None, 'Taobao': None, 'Runoob': None}
>新字典为 : {'Google': 10, 'Taobao': 10, 'Runoob': 10}
>```



### 字典的方法

字典总共有get，update，setdefault，copy，pop，popitem，keys，values，items，fromkeys，clear这些方法。



### os.path.abspath(path)方法

如果传递的path参数不会以/开头，则会将当前的路径与所给的path进行路径拼接，即`os.path.join(os.getcwd(), path)`，但如果传递的path是以/开头，则直接返回该path。

```python
print(os.path.abspath('a'))
print(os.path.abspath('/a'))
结果:
/home/andy/PythonProjects/training/a
/a
```



### os.path.getsize

如果不存在，则报错，比如`FileNotFoundError: [Errno 2] No such file or directory: '1'`，存在则返回文件的大小。



### random.choice() 方法

```python
def choice(self, seq):
    """Choose a random element from a non-empty sequence."""
    try:
        i = self._randbelow(len(seq))
    except ValueError:
        raise IndexError('Cannot choose from an empty sequence') from None
    return seq[i]
```

在一个非空序列中随机选取一个元素

```python
import random
print(random.choice([1, 2, 3, 4]))
结果:
3
# 每次的结果都可能不一样，在1,2,3,4中随机选一个数
```



### random.choices()方法

```python
def choices(self, population, weights=None, *, cum_weights=None, k=1):
    """Return a k sized list of population elements chosen with replacement.

    If the relative weights or cumulative weights are not specified,
    the selections are made with equal probability.

    """
```

从一个序列中随机选取k个元素（有放回），并将k个元素生以list形式返回。k默认为1。

```python
import random
print(random.choices([1, 2, 3, 4], k=5))
结果:
[4, 1, 3, 4, 2]
```



### random.sample()方法

```python
def sample(self, population, k):
    """Chooses k unique random elements from a population sequence or set.

    Returns a new list containing elements from the population while
    leaving the original population unchanged. 
```

```python
print(random.sample([1, 2, 3, 4, 5], k=3))
结果:
[3, 5, 2]
print(random.sample([1, 2, 3, 4, 5], k=6))
结果:
ValueError: Sample larger than population or is negative
```

`random.sample(self, population, k)`相当与在总体中随机抽样。

如果取样数为负数或者大于总体数，则返回ValueError: Sample larger than population or is negative



### random.randint()方法

```python
def randint(self, a, b):
    """Return random integer in range [a, b], including both end points.
    """

    return self.randrange(a, b + 1)
```

```python
print(random.randint(1, 2))
结果:
1
# 1和2都有可能，在闭区间[1,2]里随机选择
```



### 字符串可以强转为列表

```python
s = 'sasdsad'
print(list(s))
结果:
['s', 'a', 's', 'd', 's', 'a', 'd']
```



### 灰度测试

> #### 什么是灰度发布？
>
> 灰度发布，又名金丝雀发布，或者灰度测试，是指在黑与白之间能够平滑过渡的一种发布方式。在其上可以进行A/B testing，即让一部分用户继续用产品特性A，一部分用户开始用产品特性B，如果用户对B没有什么反对意见，那么逐步扩大范围，把所有用户都迁移到B上面来。
>
> 灰度发布是对某一产品的发布逐步扩大使用群体范围，也叫灰度放量。灰度发布可以保证整体系统的稳定，在初始灰度的时候就可以发现、调整问题，以保证其影响度。
>
> 灰度期：灰度发布开始到结束期间的这一段时间，称为灰度期。
>
> #### 灰度发布的意义
>
> 灰度发布能及早获得用户的意见反馈，完善产品功能，提升产品质量，让用户参与产品测试，加强与用户互动，降低产品升级所影响的用户范围。
>
> #### 灰度发布步骤
>
> 1. 定义目标
> 2. 选定策略：包括用户规模、发布频率、功能覆盖度、回滚策略、运营策略、新旧系统部署策略等
> 3. 筛选用户：包括用户特征、用户数量、用户常用功能、用户范围等
> 4. 部署系统：部署新系统、部署用户行为分析系统（web analytics）、设定分流规则、运营数据分析、分流规则微调
> 5. 发布总结：用户行为分析报告、用户问卷调查、社会化媒体意见收集、形成产品功能改进列表
> 6. 产品完善
> 7. 新一轮灰度发布或完整发布



### python的的数据类型以及(值传递和引用传递）

> 一：python有两种数据类型：
>
> 1. 可变数据类型(mutable object)：列表可以通过引用其元素，改变对象自身(in-place change), 这种数据类型，称之为可变数据类型，词典也是这样的数据类型
> 2. 不可变数据类型(immutable object)：像数字和字符串，不能改变对象本身，只能改变引用的指向，称之为不可变数据类型，元组(tuple)尽管可以调用引用元素，但不可以赋值，因为不能改变对象本身，所以也是不可变数据类型 
>    is关键字：要想知道是否指向同一个对象，可以使用python中的is关键字，其是判断两个引用所指的对象是否相同 
>    ‘==’ 
>    二：值传递和引用传递 
>    关于值传递和引用传递，综合目前各种的说法，可以得出这样的结论：可变对象为引用传递，不可变对象为值传递。但是python中一切事物均视为对象，个人觉得值传递和对象传递只不过是对象引用的两种表现。如果是可变对象的引用(比如字典、列表)，就能修改对象的原始值，相当于通过传引用来传递对象，不可变对象(如数字、字符、元组)，就不能通过直接修改原始对象，相当于是通过传值传递对象。 
>    具体的表现就是当赋值(引用)列表或者字典时，如果改变引用的值，就修改了原始的对象
>
> ```
>     >>> a=[1,2,3,4]
>     >>> b=a  #列表引用
>     >>> id(a) 
>     56454360
>     >>> id(b) #a,b的内存地址一样，说明这里是内存地址拷贝，可以理解为指针指向
>     56454360
>     >>> b.append(5) #改变b的值，可以发现原始对象a的值也同样改版
>     >>> b
>     [1, 2, 3, 4, 5]
>     >>> a
>     [1, 2, 3, 4, 5]1234567891011
> ```
>
> 而对于不可变对象
>
> ```
>     >>> i=1  
>     >>> i1=i #传递不可变对象数字
>     >>> i
>     1
>     >>> i1
>     1
>     >>> id(i)
>     23479136
>     >>> id(i1) #此时两者内存地址相同，可以理解为指针指向
>     23479136
>     >>> i1=2 #改变i1的值1234567891011
> ```
>
> 通过上面的例子，个人觉得对于可变对象的引用第一个例子中，对于b的改变仅仅是改变了它的元素，b依然是[1,2,3,4]这个列表的引用，所以不管是append还是pop都不会改变原始对象。而例2中当改变不可变对象i1时，i1和i就完全没有关系了，此时i1和i已经是两个对象的引用，也就是说i1=2相当于已经创建了一个新的值为2的对象。理解可能会有偏差，欢迎大家指正。 
> <http://www.cnblogs.com/ShaunChen/p/5656971.htm> 
> <http://www.cnblogs.com/ShaunChen/p/5658770.html> 
> <https://blog.csdn.net/gumengkai/article/details/52261130>



### list的加法

```python
l = [1, 2, 3]
print(id(l))
l = l + [4, 5]
print(l)
print(id(l))
结果:
140343618320520
[1, 2, 3, 4, 5]
140343618382408
```

**所以使用l = l + [4, 5]这种形式会产生一个新的内存地址**

```python
l = [1, 2, 3]
l = l + (4, 5)
结果:
TypeError: can only concatenate list (not "tuple") to list
```

而且列表的加法相加的对象也是列表，不然会报错TypeError。

**但是l += [4, 5]效果与l.extend([4, 5])一样，不同于l = l + [4, 5]**

```python
l = [1, 2, 3]
print(id(l))
l += [4, 5]
print(l)
print(id(l))
结果:
140606230427784
[1, 2, 3, 4, 5]
140606230427784
# l的内存地址并未发生改变
```

```python
l = [1, 2, 3]
print(id(l))
l += (4, 5)
print(l)
print(id(l))
结果:
139970644400264
[1, 2, 3, 4, 5]
139970644400264
# l += （4, 5) 说明+=后面可以跟可迭代对象，包括列表、元组、字典、集合。
```



列表还有一种增加序列的方法list.extend()方法，不改变原列表内存地址的情况下增加序列,而且传入的只要是可迭代对象就行，所以列表、元组、字典、集合都可以传递。

```python
def extend(self, iterable):  # real signature unknown; restored from __doc__
    """ L.extend(iterable) -> None -- extend list by appending elements from the iterable """
    pass
```

```python
l = [1, 2, 3]
print(id(l))
l.extend([4, 5])
print(l)
print(id(l))
结果:
140149160720520
[1, 2, 3, 4, 5]
140149160720520
# 内存地址相同
```



### 值传递和引用传递的区别

python的值传递不会改变传入参数的值，而引用传递传入的是一个地址，有点类似C的指针，在运行完毕之后会改变传入地址所指的值。

```python
def change(l):
    l += [1, 2]
    l = [5, 6]
    print(l)
l = [0, 3, 6]
change(l) # 打印 [5, 6]
print(l) # 打印 [0, 3, 6, 1, 2]  l所指向的列表的元素增加了
```

```python
# 空列表是否可以作为函数参数的默认值 不可以
def a(i, l=[]):
    l.append(i)
    print(l)


a(10) # [10]
a(12, [4, 5])  # [4, 5, 12]
a(20) # [10, 20]
# 调用a时，当没有传递l参数时，每次a函数使用的默认值l都是引用同一个内存地址
```

```python
def test():
    fs = []
    for n in range(6):
        def func(m):
            return m * n

        fs.append(func)
    return fs
# 闭包引用的同一个代码块

print([f(3) for f in test()])
结果:
[15, 15, 15, 15, 15, 15]
```





### 类方法类和对象均能调用，但是不管是类还是对象调用，cls都代表类，类方法一般来说使用类名调用。



### 写一个生成器，每次读取一行

```python
def read_gen(path):
    with open(path, 'r') as f:
        while True:
            content = f.readline()
            if not content:
                return
            yield content


r = read_gen('2.py')
print(next(r))
print(next(r))
结果:

    
StopIteration
# 第一行是回车符\n 第二行为空，所以读取第二次的时候函数就结束了，故StopIteration
```



### 实现一个python字符串的split方法后如何测试

```python
# 1.正常功能测试 比如能不能切割字符串
# 2.功能细节测试，比如切割符的长度不为1能否实现预期效果
# 3.不给切割符会返回什么，只有原字符串的列表
# 4.边缘测试 比如切割符在开头能否实现 切割符号在末尾能否实现 连续两个切割符号挨着能否实现
# 5.异常处理 如果输入的不是字符串如何进行异常处理
```



### sys.stderr

```python
import sys
sys.stderr.write('aaa\n')
# 在控制台输出的是红色字体，主要用于输出错误信息
```

```python
import sys
sys.stdout.write('aaa\n')
# 标准输出，在控制台显示为黑色字体
```



### 什么是Java的弱引用

> 你好，为了说明问题，给你举个例子加以说明：
>
>  String abc = new String ("abcdf"); 
>
> 这就是创建了一个String的实例然后在变量abc中保存一个强引用，为什么说它强(Strong)呢？这是跟垃圾回收器相关的，如果一个对象是通过强引用链(Chain of Strong Reference) 访问到的，也就是像上面那样，那么这个对象是不会被垃圾回收器回收的， 这在正常情况下是正确的，因为你不想垃圾回收器回收你正在使用的对象。当内存空间不足时，Java虚拟机宁愿抛出OutOfMemory错误，是程序异常终止，也不会为了解决内存不足而回收这类引用的对象。这就是使用强引用的一个问题， 强引用的另外一个常见的问题就是缓存， 特别是对于那些非常大的数据结构，像图片等等，平常情况下我们是希望程序能缓存这些大的数据结构的，因为重新加载非常耗费服务器资源。因为缓存就是为了避免重新加载这些大的数据结构的，所以缓存中会保存一个指向内存中数据结构的引用，而这些引用通常都是强引用，所以这些引用会强迫这些大的数据结构保存在内存中，除非用通过某些方法知道哪一个数据结构不再需要保存在内存中了，然后再把他从缓存中清除。  
>
> 弱引用就是不保证能不被垃圾回收器回收的对象，它拥有比较短暂的生命周期，在垃圾回收器扫描它所管辖的内存区域过程中，一旦发现了只具有弱引用的对象，就会回收它的内存，不过一般情况下，垃圾回收器的线程优先级很低，也就不会很快发现那些只有弱引用的对象。 
>
>  弱引用可以和一个引用队列(ReferenceQueue)联合使用，如果弱引用的对象被垃圾回收的话，Java虚拟机就会把这个弱引用加入相关的引用队列中。
>
> 以下就是创建弱引用对象的例子。 
>
>  String abc = new String("abcde");
>
>  WeakReference\<String> wf= new WeakReference\<String>(str, rq); 
>
>  String abc1 = wf.get()//如果abcde这个对象没有被垃圾回收器回收，那么abc1就指向"abcde"对象



### json.dump()和json.load()

json.dump()将字典序列化为json格式写入到文件中

```python
import json

a = {'a': 1, 'b': 2}
fp = open('1.json', 'w')
json.dump(a, fp)
fp.close()
```

```json
1.json
{"a": 1, "b": 2}
```

json.load()从json文件中加载json数据并转化为python对象。

```python
import json
fp = open('1.json', 'r')
res = json.load(fp)
print(res)
print(type(res))
fp.close()
结果:
{'a': 1, 'b': 2}
<class 'dict'>
```

json.loads()不仅可以把json数据转化为字典，还能将其转化为列表。

```python
import json

res = json.loads('[1, 2, 3]')
print(res)
print(type(res))
结果:
[1, 2, 3]
<class 'list'>
```



### C语言 FILE *fp

fp: File Pointer.表示fp是指向FILE结构的指针变量，通过fp即可找存放某个文件信息的结构变量，然后按结构变量提供的信息找到该文件，实施对文件的操作。习惯上也笼统地把fp称为指向一个文件的指针。



### 正则表达式中，正则表达式"[\d_]"和"[0-9\_]"效果一样

```python
import re
a = r'[\d_]'
pattern = re.compile(a)
print(pattern.findall("789_"))
结果:
['7', '8', '9', '_']
```



### 可以匹配以.com，.cn，.net结尾的邮箱地址

```python
import re
a = "^[\w\.-]+@[\w\.]+\.[com,cn,net]{2,3}$"
#这里的{2,3}指2-3个字符。
pattern = re.compile(a)
print(pattern.findall('ahdkas@163.com'))
```



### 如何最大限度防止突然停电引起的数据库损坏

1. 物理解决方法,用智能UPS,带串口/LAN管理的

> [     UPS(Uninterruptible Power System/Uninterruptible Power Supply)，即不间断[电源](https://baike.baidu.com/item/%E7%94%B5%E6%BA%90)，是将[蓄电池](https://baike.baidu.com/item/%E8%93%84%E7%94%B5%E6%B1%A0/990661)（多为铅酸免维护蓄电池）与主机相连接，通过主机逆变器等模块电路将直流电转换成市电的系统设备。主要用于给单台[计算机](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA/140338)、计算机网络系统或其它[电力电子设备](https://baike.baidu.com/item/%E7%94%B5%E5%8A%9B%E7%94%B5%E5%AD%90%E8%AE%BE%E5%A4%87/7338877)如电磁阀、压力变送器等提供稳定、不间断的电力供应。当市电输入正常时，UPS 将市电稳压后供应给[负载](https://baike.baidu.com/item/%E8%B4%9F%E8%BD%BD/906913)使用，此时的UPS就是一台交流式电[稳压器](https://baike.baidu.com/item/%E7%A8%B3%E5%8E%8B%E5%99%A8/1414426)，同时它还向机内电池充电；当市电中断（事故停电）时， UPS 立即将电池的直流电能，通过逆变器切换转换的[方法](https://baike.baidu.com/item/%E6%96%B9%E6%B3%95/2444)向负载继续供应220V[交流电](https://baike.baidu.com/item/%E4%BA%A4%E6%B5%81%E7%94%B5/1023508)，使负载维持正常工作并保护负载软、[硬件](https://baike.baidu.com/item/%E7%A1%AC%E4%BB%B6/479446)不受损坏。UPS 设备通常对电压过高或电压过低都能提供保护。

2. backup every day

每天都要做好数据库的备份工作



GET与POST的区别

|                  | GET                                                          | POST                                                         |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 后退按钮/刷新    | 无害                                                         | 数据会被重新提交（浏览器应该告知用户数据会被重新提交）。     |
| 书签             | 可收藏为书签                                                 | 不可收藏为书签                                               |
| 缓存             | 能被缓存                                                     | 不能缓存                                                     |
| 编码类型         | application/x-www-form-urlencoded                            | application/x-www-form-urlencoded 或 multipart/form-data。为二进制数据使用多重编码。 |
| 历史             | 参数保留在浏览器历史中。                                     | 参数不会保存在浏览器历史中。                                 |
| 对数据长度的限制 | 是的。当发送数据时，GET 方法向 URL 添加数据；URL 的长度是受限制的（URL 的最大长度是 2048 个字符）。 | 无限制。                                                     |
| 对数据类型的限制 | 只允许 ASCII 字符。                                          | 没有限制。也允许二进制数据。                                 |
| 安全性           | 与 POST 相比，GET 的安全性较差，因为所发送的数据是 URL 的一部分。在发送密码或其他敏感信息时绝不要使用 GET ！ | POST 比 GET 更安全，因为参数不会被保存在浏览器历史或 web 服务器日志中。 |
| 可见性           | 数据在 URL 中对所有人都是可见的。                            | 数据不会显示在 URL 中。                                      |



### scrapy

scrapy是一个异步的，基于事件循环的爬虫框架。scapy 底层是异步框架 twisted ，twisted是用Python实现的基于事件驱动的网络引擎框架，支持并发，速度快。



### x ** y可以表示x的y次方

```python
print(3 ** 3)
27
print(pow(3, 3))
27
```



### 格式化输出二进制数

```python
print("{0:b}".format(0b1010))
1010
print("{0:b}").fomat(12345)
1100
```



### 将十进制数转化为二进制数的方法

1. 写函数采用 %2 的方式来算

   ```python
   binary = lambda n: '' if n == 0 else binary(n // 2) + str(n % 2)
   print(binary(9))
   结果:
   1001
   ```

2. 采用 python 自带了方法 bin 函数，比如 bin(12345) 回返回字符串 '0b11000000111001', 这个时候在把0b去掉即可:

   ```python
   print(bin(12345).replace('0b', ''))
   print(bin(12345)[2:])
   结果:
   11000000111001
   11000000111001
   ```



### python将二进制转化为十进制

```python
print(int('100111', base=2))
39
```



### 匿名函数可以直接调用且可以不设置参数

```python
print((lambda x: x * x)(3))
9
print((lambda: 'abc')())
abc
```



### max(i for i in range(10))可以直接这么使用

```python
print(max(i for i in range(10)))
print(i for i in range(10))
结果:
9
<generator object <genexpr> at 0x7f42812f35c8> # 生成器表达式
```

```python
g = lambda: (yield 1)
print(g())
def f():
    yield 1

print(f())
结果:
<generator object <lambda> at 0x7f134198b620>
<generator object f at 0x7f134198b620>
```



### Java中堆内存（heap）和栈内存（stack）的区别

> **在Java代码中，常常会使用到这样的类的声明实例化：**
>
> Person per = new Person();
>
> //这其实是包含了两个步骤，声明和实例化
>
> Person per = null; //声明一个名为Person类的对象per
>
> per = new Person(); // 实例化这个per对象
>
> **声明** 指的是创建类的对象的过程；
>
> **实例化** 指的是用关键词new来开辟内存空间。
>
> 它们在内存中的划分是这样的：
>
> ![848193-20151206120547018-1139699566](/home/andy/Desktop/Notes/848193-20151206120547018-1139699566.png)
>
> **那什么是栈内存（heap）和栈内存（heap）呢？**
>
> #### **栈内存：**
>
> ​       在函数中定义的一些基本类型的变量和对象的引用变量都在函数的栈内存中分配。栈内存主要存放的是基本类型类型的数据 如( int, short, long, byte, float, double, boolean, char) 和对象句柄。注意：并没有String基本类型、在栈内存的数据的大小及生存周期是必须确定的、其优点是寄存速度快、栈数据可以共享、缺点是数据固定、不够灵活。
>
> #### 栈的共享：
>
> 　　　结果为True，这就说明了str1和str2其实指向的是同一个值。
>
> ​       上述代码的原理是，首先在栈中创建一个变量为str1的引用，然后查找栈中是否有myString这个值，如果没找到，就将myString存放进来，然后将str1指向myString。接着处理String str2 = "myString";；在创建完str2 的引用变量后，因为在栈中已经有myString这个值，便将str2 直接指向myString。这样，就出现了str1与str2 同时指向myString。
>
> ​       特别注意的是，这种字面值的引用与类对象的引用不同。假定两个类对象的引用同时指向一个对象，如果一个对象引用变量修改了这个对象的内部状态，那么另一个对象引用变量也即刻反映出这个变化。相反，通过字面值的引用来修改其值，不会导致另一个指向此字面值的引用的值也跟着改变的情况。如上例，我们定义完str1与str2 的值后，再令str1=yourString；那么，str2不会等于yourString，还是等于myString。在编译器内部，遇到str1=yourString；时，它就会重新搜索栈中是否有yourString的字面值，如果没有，重新开辟地址存放yourString的值；如果已经有了，则直接将str1指向这个地址。因此str1值的改变不会影响到str2的值。
>
>  
>
> #### 堆内存：
>
> 堆内存用来存放所有new 创建的对象和 数组的数据
>
> 　　创建了两个引用，创建了两个对象。两个引用分别指向不同的两个对象。以上两段代码说明，只要是用new()来新建对象的，都会在堆中创建，而且其字符串是单独存值的，即使与栈中的数据相同，也不会与栈中的数据共享。



### java堆内存和栈内存的区别

> 2017年06月05日 14:48:57
>
>  
>
> 阅读数：6232
>
>  
>
> 标签： [内存](http://so.csdn.net/so/search/s.do?q=%E5%86%85%E5%AD%98&t=blog) 更多
>
> 个人分类： [垃圾回收](https://blog.csdn.net/chensi16114/article/category/6955555)
>
> 版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/chensi16114/article/details/72867260
>
> 一段时间之前，我写了两篇文章文章分别是[Java的垃圾](http://www.journaldev.com/2856/java-jvm-memory-model-and-garbage-collection-monitoring-tuning)回收和[Java的值传递](http://www.journaldev.com/3884/java-is-pass-by-value-and-not-pass-by-reference)，从那之后我收到了很多要求解释[Java](http://lib.csdn.net/base/java)堆内存和栈内存的邮件，并且要求解释他们的异同点。
>
> 在Java中你会看到很多堆和栈内存的引用，JavaEE书和文章很难在程序的角度完全解释什么是堆什么是栈。
>
> 总结：
> 1 栈：为编译器自动分配和释放，如函数参数、局部变量、临时变量等等
> 2 堆：为成员分配和释放，由程序员自己申请、自己释放。否则发生内存泄露。典型为使用new申请的堆内容。
> 除了这两部分，还有一部分是：
> 3 静态存储区：内存在程序编译的时候就已经分配好，这块内存在程序的整个运行期间都存在。它主要存放静态数据、全局数据和常量。
>
> ### Java堆内存
>
> 堆内存在Java运行时被使用来为对象和JRE类分配内存。不论什么时候我们创建了对象，它将一直会在堆内存上创建。垃圾回收运行在堆内存上来释放没有任何引用的对象所占的内存，任何在堆上被创建的对象都有一个全局的访问，并且可以在应用的任何位置被引用。
>
> ### Java栈内存
>
> Java的栈内存被用来线程的执行，他们包含生命周期很短的具体值的方法和在堆中使用这个方法对象的引用。栈内存是LIFO（后进先出）序列。当方法被调用的时候，堆内存中一个新的块被创建，保存了本地原始值和在方法中对其他对象的引用。这个方法结束之后，这个块对其他方法就变成可用的了。栈内存与堆内存相比是非常小的。
>
> 我们用下边的例子理解堆内存和栈内存
>
> **[java]** [view plain](http://blog.csdn.net/maoyeqiu/article/details/49614061#) [copy](http://blog.csdn.net/maoyeqiu/article/details/49614061#)
>
> 1. package com.journaldev.test;  
> 2.    
> 3. public class Memory {  
> 4.    
> 5. ​    public static void main(String[] args) { // Line 1  
> 6. ​        int i=1; // Line 2  
> 7. ​        Object obj = new Object(); // Line 3  
> 8. ​        Memory mem = new Memory(); // Line 4  
> 9. ​        mem.foo(obj); // Line 5  
> 10. ​    } // Line 9  
> 11.    
> 12. ​    private void foo(Object param) { // Line 6  
> 13. ​        String str = param.toString(); //// Line 7  
> 14. ​        System.out.println(str);  
> 15. ​    } // Line 8  
> 16.    
> 17. }  
>
>  下边的图片展示了上边程序堆和栈内存的引用，并且是怎么用来存储原始值、对象和变量的引用。
>
> ![20151103125937282](/home/andy/Desktop/Notes/20151103125937282.png)
>
> 我们来看看程序执行的过程：
>
> 1、只要我们一运行这个程序，它会加载所有的运行类到堆内存中去，当在第一行找到main()方法的时候，Java创建可以被main()方法线程使用的栈内存。
>
> 2、当在第一行，我们创建了本地原始变量，它在main()的栈中创建和保存。
>
> 3、因为我们在第三行创建了对象，它在堆内存中被创建，在栈内存中保存了它的引用，同样的过程也发生在第四行我们创建Memory对象的时候。
>
> 4、当在第五行我们调用foo()方法的时候，在堆的顶部创建了一个块来被foo()方法使用，因为Java是值传递的，在第六行一个新的对象的引用在foo()方法中的栈中被创建
>
> 5、在第七行一个String被创建，它在堆空间中的[String池](http://www.journaldev.com/797/what-is-java-string-pool)中运行，并且它的引用也在foo()方法的栈空间中被创建
>
> 6、foo()方法在第八行结束，此时在堆中为foo()方法分配的内存块可以被释放
>
> 7、在第九行，main()方法结束，栈为main()方法创建的内存空间可以被销毁。同样程序也在行结束，Java释放了所有的内存，结束了程序的运行
>
> ### 堆内存和栈内存的区别
>
> 基于上边的解释我们可以很简单的总结出堆和栈的区别：
>
> 1、应用程序所有的部分都使用堆内存，然后栈内存通过一个线程运行来使用。
>
> 2、不论对象什么时候创建，他都会存储在堆内存中，栈内存包含它的引用。栈内存只包含原始值变量好和堆中对象变量的引用。
>
> 3、存储在堆中的对象是全局可以被访问的，然而栈内存不能被其他线程所访问。
>
> 4、栈中的内存管理使用LIFO的方式完成，而堆内存的管理要更复杂了，因为它是全局被访问的。堆内存被分为，年轻一代，老一代等等，更多的细节请看，[这篇文章](http://www.journaldev.com/2856/java-jvm-memory-model-and-garbage-collection-monitoring-tuning)
>
> 5、栈内存是生命周期很短的，然而堆内存的生命周期从程序的运行开始到运行结束。
>
> 6、我们可以使用-Xms和-Xmx JVM选项定义开始的大小和堆内存的最大值，我们可以使用-Xss定义栈的大小
>
> 7、当栈内存满的时候，Java抛出java.lang.StackOverFlowError异常而堆内存满的时候抛出java.lang.OutOfMemoryError: Java Heap Space错误
>
> 8、和堆内存比，栈内存要小的多，因为明确使用了内存分配规则（LIFO），和堆内存相比栈内存非常快。
>
> 原文地址：http://www.journaldev.com/4098/java-heap-memory-vs-stack-memory-difference



### 需要直接return super().run()

```python
class A:
    def run(self):
        return 'run'


class B(A):
    def run(self):
        # return A().run()  在本案例中可以使用这种写法
        # return A.run(self)
        return super().run()


print(A().run())
print(B().run())
print(A.run(1)) # Expected type 'A',got 'int' instead.
结果:
run
run
run
```



### try...except...else

```python
try:
    a = 10 / 0
except ZeroDivisionError:
    print('except')
else:
    print('else')
    print('a =', a)
    
结果:
except # 异常的话就走异常处理，不走else
```

```python
try:
    a = 10 / 1
except ZeroDivisionError:
    print('except')
else:
    print('else')
    print('a =', a)

结果:
else
a = 10.0
# 不异常的话直接走else
```



### 装饰器内层可以直接return func(*args, **kwargs)

```python
from functools import wraps


def auto_increment_one(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs) + 1

    return wrapper


@auto_increment_one
def add(a, b):
    return a + b


print(add(3, 4))
结果:
8
```



### os.remove(path)

os.remove()方法用于删除指定路径的文件。如果指定的路径是一个目录将抛出OSError。

在Unix,Windows中有效

语法:

os.remove(path)

```python
import os
os.remove('a.xls')
结果:
FileNotFoundError: [Errno 2] No such file or directory: 'a.xls' # 文件不存在将抛出FileNotFoundError    
```



### 二叉搜索树

> 二叉查找树（Binary Search Tree），（又：[二叉搜索树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91/7077855)，二叉排序树）它或者是一棵空树，或者是具有下列性质的[二叉树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%A0%91/1602879)： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为[二叉排序树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%8E%92%E5%BA%8F%E6%A0%91/10905079)。
>
> ![8644ebf81a4c510f0b3dafdf6359252dd52aa57e](/home/andy/Desktop/Notes/8644ebf81a4c510f0b3dafdf6359252dd52aa57e.jpg)



### 平衡二叉树

> 平衡二叉搜索树（Self-balancing binary search tree）又被称为AVL树（有别于AVL算法），且具有以下性质：它是一 棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。平衡二叉树的常用实现方法有[红黑树](https://baike.baidu.com/item/%E7%BA%A2%E9%BB%91%E6%A0%91/2413209)、[AVL](https://baike.baidu.com/item/AVL/7543015)、[替罪羊树](https://baike.baidu.com/item/%E6%9B%BF%E7%BD%AA%E7%BE%8A%E6%A0%91/13859070)、[Treap](https://baike.baidu.com/item/Treap)、[伸展树](https://baike.baidu.com/item/%E4%BC%B8%E5%B1%95%E6%A0%91/7003945)等。 最小二叉平衡树的节点的公式如下 F(n)=F(n-1)+F(n-2)+1 这个类似于一个递归的[数列](https://baike.baidu.com/item/%E6%95%B0%E5%88%97/731531)，可以参考Fibonacci(斐波那契)数列，1是根节点，F(n-1)是左子树的节点数量，F(n-2)是右子树的节点数量。
>
> ![3801213fb80e7bec26a434f7242eb9389b506bad](/home/andy/Desktop/Notes/3801213fb80e7bec26a434f7242eb9389b506bad.jpg)

平衡二叉树 搜索的时间复杂度0(logN)

平衡二叉树是基于二叉搜索树的，由于更加平衡，相同结点数的情况下层数越少，搜索的效率越高。



### \_\_getattribute\_\_方法 

\_\_getattribute\_\_方法，在对象调用属性和方法时都会调用。

```python
class A:
    num = 1

    def __init__(self):
        self.name = 'lily'

    def __getattribute__(self, item):
        print('__getattribute__')
        return super().__getattribute__(item)

    def run(self):
        print('run')


A().run()
print(A().name)
结果:
__getattribute__
run
__getattribute__
lily
# 说明对象直接调用方法和属性时都会先调用__getattribute__方法
```

```python
# 但是当类调用时就不会__getattribute__方法，因为它是一个对象方法。
print(A.num)
A.run(A())
结果:
1
run
```



### \_\_getattr\_\_() 和 \_\_getattribute\_\_() 方法的区别

python 在访问属性的方法上定义了`__getattr__()` 和 `__getattribute__()` 2种方法，其区别非常细微，但非常重要。

1. 如果某个类定义了 `__getattribute__()` 方法，在 *每次引用属性或方法名称时* Python 都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。
2. 如果某个类定义了 `__getattr__()` 方法，Python 将只在正常的位置查询不到属性时才会调用它。如果实例 x 定义了属性 color， `x.color` 将 *不会* 调用`x.__getattr__('color')`；而只会返回 x.color 已定义好的值。

 

让我们用两个例子来解释一下：

```
class Dynamo(object):
    def __getattr__(self, key):
        if key == 'color':         ①
            return 'PapayaWhip'
        else:
            raise AttributeError   ②

>>> dyn = Dynamo()
>>> dyn.color                      ③
'PapayaWhip'
>>> dyn.color = 'LemonChiffon'
>>> dyn.color                      ④
'LemonChiffon'
```

1. 属性名称以字符串的形式传入 `__getattr()__` 方法。如果名称为 `'color'`，该方法返回一个值。（在此情况下，它只是一个硬编码的字符串，但可以正常地进行某些计算并返回结果。）
2. 如果属性名称未知， `__getattr()__` 方法必须引发一个 `AttributeError` 例外，否则在访问未定义属性时，代码将只会默默地失败。（从技术角度而言，如果方法不引发例外或显式地返回一个值，它将返回 `None` ——Python 的空值。这意味着 *所有* 未显式定义的属性将为 `None`，几乎可以肯定这不是你想看到的。）
3. dyn 实例没有名为 color 的属性，因此在提供计算值时将调用 `__getattr__()` 。
4. 在显式地设置 dyn.color 之后，将不再为提供 dyn.color 的值而调用 `__getattr__()` 方法，因为 dyn.color 已在该实例中定义。

另一方面，`__getattribute__()` 方法是绝对的、无条件的。

```
class SuperDynamo(object):
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError

>>> dyn = SuperDynamo()
>>> dyn.color                      ①
'PapayaWhip'
>>> dyn.color = 'LemonChiffon'
>>> dyn.color                      ②
'PapayaWhip'
```

1. 在获取 dyn.color 的值时将调用 `__getattribute__()` 方法。
2. 即便已经显式地设置 dyn.color，在获取 dyn.color 的值时, *仍将调用* `__getattribute__()` 方法。如果存在 `__getattribute__()` 方法，将在每次查找属性和方法时 *无条件地调用* 它，哪怕在创建实例之后已经显式地设置了属性。

> ☞如果定义了类的 `__getattribute__()` 方法，你可能还想定义一个 `__setattr__()` 方法，并在两者之间进行协同，以跟踪属性的值。否则，在创建实例之后所设置的值将会消失在黑洞中。

必须特别小心 `__getattribute__()` 方法，因为 Python 在查找类的方法名称时也将对其进行调用。

```
class Rastan(object):
    def __getattribute__(self, key):
        raise AttributeError           ①
    def swim(self):
        pass

>>> hero = Rastan()
>>> hero.swim()                        ②
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __getattribute__
AttributeError
```

1. 该类定义了一个总是引发 `AttributeError` 例外的 `__getattribute__()` 方法。没有属性或方法的查询会成功。

2. 调用 `hero.swim()` 时，Python 将在 `Rastan` 类中查找 `swim()` 方法。该查找将执行整个 `__getattribute__()`方法，因为所有的属性和方法查找都通过`__getattribute__()` 方法。在此例中， `__getattribute__()` 方法引发 `AttributeError` 例外，因此该方法查找过程将会失败，而方法调用也将失败。

   

### 对象的\_\_dict\_\_属性

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return 'run'


lily = Student('lily', 18)
print(lily.__dict__)
lily.height = 168
print(lily.__dict__)
print(lily.run())
lily.run = lambda: 1
print(lily.__dict__)
print(lily.run())
结果:
{'name': 'lily', 'age': 18}
{'name': 'lily', 'age': 18, 'height': 168}
run
{'name': 'lily', 'age': 18, 'height': 168, 'run': <function <lambda> at 0x7f9e77dbd158>}
1
# lily.__dict__就是存放当前对象特有的属性信息.
# lily.run = lambda: 1 只是规定可lily这个对象的run方法,并没有改变由Student类建立的其他实例对象的run()方法. 
```



### def sum(): print(sum)

```python
print(sum)
def sum():
    print(sum)

sum()
结果:
<built-in function sum>
<function sum at 0x7ff3eea43b70>
# 说明在def sum():之后,sum函数的内存地址已经分配好了,之后就是函数体部分了.
```



### 线程start()方法和run()方法的区别

- start() 方法是启动一个子线程，线程名就是我们定义的name
- run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。

因此,如果你想启动多线程,就必须使用start()方法。



### python获取多线程返回值

```python
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result # # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except AttributeError:
            return


def foo(a, b, c):
    time.sleep(1)
    return a * 2, b * 2, c * 2


start_time = time.time()
li = []
for i in range(4):
    t = MyThread(foo, args=(i, i + 1, i + 2))
    li.append(t)
    t.start()

for t in li:
    t.join() # 一定要join，不然主线程比子线程跑的快，会拿不到结果
    print(t.get_result())

end_time = time.time()
print(end_time - start_time)
```



### 控制超时时间的装饰器,有重试次数和超时时间两个属性

```python
import threading
import time
import requests


class MyThread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.daemon = True  # 主线程结束，子线程跟着结束

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)

    def get_result(self):
        return self.result


class Timeout:
    def __init__(self, delay=-1):
        self.delay = delay
        # self.retry = 0

    def __call__(self, wrapped):
        def wrapper(*args, **kwargs):
            t = MyThread(wrapped, *args, **kwargs)
            t.start()
            start_time = time.time()
            if self.delay == -1:
                t.join()
                return t.get_result()
            while True:
                runtime = time.time() - start_time
                if runtime > self.delay:
                    return '运行超时'
                try:
                    return t.get_result()
                except AttributeError:
                    continue

        return wrapper


@Timeout(delay=5)
def get_content(url):
    response = requests.get(url)
    return response.content


print(get_content('https://www.google.com.hk/'))
```

ps:未完待续，还有重试功能没完成。关于超时可以使用的模块，timeout_decorator库，signal库



### time.clock()

```python
def clock(): # real signature unknown; restored from __doc__
    """
    clock() -> floating point number
    
    Return the CPU time or real time since the start of the process or since
    the first call to clock().  This has as much precision as the system
    records.
    """
    return 0.0
```

 time clock() 函数以浮点数计算的秒数返回当前的CPU时间。

```python
a = time.clock()
print(a)
time.sleep(4)
b = time.clock()
print(b)
结果:
0.251959
0.252021
```

time.sleep()的时间不算在cpu时间里，故这里的间隔时间没有将4秒算在内。

```python
a = time.clock()
print(a)
requests.get('https://stackoverflow.com/')
b = time.clock()
print(b)
结果:
0.216548
0.260585
```

同理，网络io的等待时间也没算在内，只将处理网络请求的时间算进去了。