# Python基础

#### 计算函数运行时间的装饰器

```python
decorate.py
import time
from functools import wraps
def runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print('执行时间:',time.time() - start_time)
        return result
    return wrapper

@runtime
def add(a,b):
    print(a + b)
    sum = 0
    for i in range(10000):
        sum += i
    return sum
add(1, 2)
```

```python
test.py
from decorate import runtime
直接这样运行就直接执行decorate.py里的add(1,2)的函数了,所以应该在decorate.py里改成
if __name__ == '__main__':
    add(1, 2)
还有就是就算runtime装饰器内部需要用到time模块内的time.time()函数,但直接
from decorate import runtime无需再导入time模块也直接可以用runtime装饰器了
```





#### 控制函数失败重启的装饰器,可传参,参数为重启次数

```pyth
import requests
import time
from functools
RETRY_TIMES = 3
DOWNLOAD_DELAY = 2


class Retry:
    def __init__(self, retry=3, delay=0):
        self.retry = retry
        self.delay = delay

    def __call__(self, func):
    	@wraps(func) # 使得装饰后的函数的属性与原函数一致,比如__doc__,__name__等
        def wrapper(*args, **kwargs):
            for i in range(self.retry):
                try:
                	# 这里一定要用一个参数,如result去接受函数返回值,之后return result
                	# 不然如果在返回的时候也调用func,会使函数执行两次
                    result = func(*args, **kwargs) 
                except Exception as e:
                    # print(e)
                    time.sleep(self.delay)
                    continue
                else:
                    return result
        return wrapper


@Retry(RETRY_TIMES, DOWNLOAD_DELAY)
def fetch(url):
    resp = requests.get(url, timeout=5)
    print(resp.status_code)
    

fetch('http://www.baidu.com')
```



#### 匿名函数lambda可以直接调用,不用把他赋值给变量

```python
>>> (lambda x, y=0,z=0:x+y+z)(3,5,6)
14
>>> (lambda x, y=0,z=0:x+y+z)
<function <lambda> at 0x7f14c2fe2ea0>
```

上式中(lambda x, y=0,  z=0:x+y+z)为一个函数变量,因此它可以被调用,在后面传入参数(3,5,6),获得返回值14.



#### 字符串中去除空格换行符等

```python
>>>a = 'a     b  \nc  \fd'
>>>''.join(a.split())
'abcd'
```



#### 字典dict.items()和dict.keys()

```python
>>> dict = {'a': 1, 'b': 2, 'c': 3}
>>> print(dict.items())
dict_items([('a', 1), ('b', 2), ('c', 3)])
>>> print(type(dict.items()))
<class 'dict_items'>
>>> for i in dict.items():
>>>     print(i)
('a', 1)
('b', 2)
('c', 3)
>>> print(dict.keys())
dict_keys(['a', 'b', 'c'])
>>> print(type(dict.keys()))
<class 'dict_keys'>
>>> for i in dict.keys():
>>>    print(i)
a
b
c
```



#### 换行，制表，换页，回车　->   [\n\t\f\r]

```python
>>> print('a\nb') ＃换行符　newline
a
b
>>> print('a\tb') # 制表符 tabs
 a	b
\f 换页符　form feed character
>>> print('a\rb') #　回车符 return
b
\n,\t,\f,\r均为转义字符，改变了字符串原来的意思
```



#### 字符串前面加'r'

在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转意backslash '\' 。 例如，\n 在raw string中，是两个字符，\和n， 而不会转意为换行符。由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。



#### 字符串切割

**str.split(sep=None, maxsplit=-1)**  

- separator:分割符
- maxsplit:切割次数，默认-1,表示无限多次,贪婪匹配

```python
>>> a = 'a,,a'
>>> print(a.split(','))
['a', '', 'a'] #从a开始读取,读到第一个,时,把在这之前获得的字符串放在列表内,此时列表为['a'].然后从第一个逗号之后读取,直接碰到第二个,因此第二个匹配到的为空字符串,此时列表内为['a', ''].然后从第二个逗号出发,匹配到a,此时字符串结束.将'a'放入列表中,最终得到结果['a', '', 'a']
>>> a = 'a,,a'
>>> print(a.split(',',maxsplit=1)) #最多切割一次
['a', ',a']
```

type只是负责创建类,但创建的类的父类仍然是object.

包括type的父类也是object.



#### 单例模型

老师之前用到的只是在整个项目中的某一个文件自定义一个类，然后在该py文件中实例化一个对象，别的文件调用这只实例化过一次的类的对象就叫他单例模式

目前只会一种真正的单例模式：

```python
class single_instance(object):
    __instance=None
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls,*args,**kwargs)
        return cls.__instance

a=single_instance()
b=single_instance()
print(a)
print(b)
输出结果如下：
<__main__.singleton object at 0x0000016D5191D320>
<__main__.singleton object at 0x0000016D5191D320>
```



#### 动态创建类

```python
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class '__main__.Hello'>
```



#### metaclass

```python
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
class MyList(list, metaclass=ListMetaclass):
    pass

# 自定义的MyList有add()方法
>>> L = MyList()
>>> L.add(1)
>> L
[1]
# 普通的list没有add()方法：
>>> L2 = list()
>>> L2.add(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
```



#### 简易ORM

```python
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                # print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        args = list(map(str, args))
        sql = 'INSERT INTO %s (%s) VALUES (%s);' % (self.__table__.lower(), ', '.join(fields), ', '.join(args))
        # sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        # print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org',password='my_pwd')
u.save()
输出结果如下:
SQL: INSERT INTO user (id, username, email, password) VALUES (12345, Michael, test@orm.org, my_pwd);
```



#### markdown中显示\_\_init\_\_

用\加下杠表示一个下杠



#### 定义一个字典时最好使用d1 = dict(name='张三',age=14)这样的格式，比较清晰。



#### .copy方法所得到的对象的内存地址与原对象不同

```python
d1 = {'name':'张三','age':14}
d2 = d1.copy()
print(id(d1))
print(id(d2))
输出结果:
139915638925280
139915638925352
# 内存地址不同
```



#### 字典的setdefalut,get,update方法

- setdefault

```python
def setdefault(self, k, d=None): 
	""" D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
    pass
```

```python
>>> d = dict(name='lily', age=13)
>>> d.setdefault('sex', 'female')
>>> print(d)
{'name': 'lily', 'age': 13, 'sex': 'female'}
>>> d.setdefault('name', 'mary')
>>> print(d)
{'name': 'lily', 'age': 13, 'sex': 'female'}
```

- get

```python
>>> d = dict(name='lily', age=13)
>>> print(d.get('name'))
'lily'
>>> print(d.get('sex')) # 键不存在返回None
None
>>> print(d.get('sex', 'female')) # 如果没有返回提供的默认值
'female'
```

- update

```python
def update(self, E=None, **F): 
"""
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v In either case, this is followed by: for k in F:  D[k] = F[k]
"""
pass
```

```python
>>> d = dict(name='lily', age=13)
>>> d.update({'sex': 'female'})
>>> print(d)
{'name': 'lily', 'age': 13, 'sex': 'female'}

>>> d = dict(name='lily', age=13)
>>> d.update([('sex', 'female'), ('from', 'China')])
>>> print(d)

>>> d = dict(name='lily', age=13)
>>> d.update(sex='female')
>>> print(d)
```



#### \_\_next\_\_和\_\_iter\_\_的用法

```python
class My_gen(object):
    def __init__(self):
        self.number = 0

    def __next__(self):
        self.number += 1
        # print(self.number)
        if self.number < 10:
            return self.number
        else:
            raise StopIteration
        
    def __iter__(self):
        number = 0
        while number < 10:
            number += 1
            yield number
```

```python
>>> gen
>>> gen = My_gen()
>>> next(gen) # 调用__next__方法，返回1
1
>>> gen.__next__() # 调用__next__方法，self.number=2
2
>>> for i in gen: # 直接走__iter__方法，遇到yield就把yield后的值返回，这样相当于while循环一直没断，所以可以记录遍历到的位置。
>>> print(i)
1
2
3
4
5
6
7
8
9
10
```



#### 自制生成器

```python
def f1():
    number = 0
    while number < 10:
        number += 1
        yield number
>>> gen = f1()
>>> print(gen)
<generator object f1 at 0x7f441ed3be60>
>>> next(gen)
1
>>> next(gen) # 还在同一个while循环里，所以记录了number的值
2
```



#### python守护线程

如果你设置一个线程为守护线程，，就表示你在说这个线程是不重要的，在进程退出的时候，不用等待这个线程退出。 
如果你的主线程在退出的时候，不用等待那些子线程完成，那就设置这些线程的daemon属性。即，在线程开始（thread.start()）之前，调用setDeamon（）函数，设定线程的daemon标。thread.setDaemon(True)）就表示这个线程“不重要”。

如果你想等待子线程完成再退出，那就什么都不用做。，或者显示地调用thread.setDaemon(False)，设置daemon的值为false。新的子线程会继承父线程的daemon标志。整个Python会在所有的非守护线程退出后才会结束，即进程中没有非守护线程存在的时候才结束。

用代码测试一下上面的结论。 
情况1，不设置deamon的时候。

```python
#!coding:utf8 

import time
import threading


def fun():
    print "start fun"
    time.sleep(2)
    print "end fun"


print "main thread"
t1 = threading.Thread(target=fun,args=())
#t1.setDaemon(True)
t1.start()
time.sleep(1)
print "main thread end"
```

得到的结果是 
main thread 
start fun 
main thread end 
end fun 
说明，程序在等待子线程结束，才退出了。

情况2，设置了daemon。

```python
#!coding:utf8 
 
import time
import threading
 
def fun():
    print "start fun"
    time.sleep(2)
    print "end fun"

 
print "main thread"
t1 = threading.Thread(target=fun,args=())
t1.setDaemon(True)
t1.start()
time.sleep(1)
print "main thread end"
```

程序输出 
main thread 
start fun 
main thread end

程序在主线程结束后，直接退出了。 导致子线程没有运行完。

摘自https://blog.csdn.net/u012063703/article/details/51601579

  

#### Linux守护进程(daemon)详解与创建

> **一、概述**
>
> Daemon（守护进程）是运行在后台的一种特殊进程。它独立于控制终端并且周期性地执行某种任务或等待处理某些发生的事件。它不需要用户输入就能运行而且提供某种服务，不是对整个系统就是对某个用户程序提供服务。Linux系统的大多数服务器就是通过守护进程实现的。常见的守护进程包括系统日志进程syslogd、 web服务器httpd、邮件服务器sendmail和数据库服务器mysqld等。
>
> 守护进程一般在系统启动时开始运行，除非强行终止，否则直到系统关机都保持运行。守护进程经常以超级用户（root）权限运行，因为它们要使用特殊的端口（1-1024）或访问某些特殊的资源。
>
> 守护进程的父进程是init进程，因为它真正的父进程在fork出子进程后就先于子进程exit退出了，所以它是一个由init继承的孤儿进程。守护进程是非交互式程序，没有控制终端，所以任何输出，无论是向标准输出设备stdout还是标准出错设备stderr的输出都需要特殊处理。
>
> 守护进程的名称通常以d结尾，比如sshd、xinetd、crond等。



#### SSL

只要你听过HTTPS，不可能没听过SSL协议吧，SSL协议是一种安全协议。对于互联网协议没有了解的童鞋可以参考博主另一篇博客：[internet协议入门](http://blog.damonare.cn/2016/11/26/%E4%BA%92%E8%81%94%E7%BD%91%E5%8D%8F%E8%AE%AE%E5%85%A5%E9%97%A8/)

> HTTP+SSL = HTTPS

HTTPS之所以安全就是因为加持了SSL这个外挂来对传输的数据进行加密，那么具体的加密方法又是什么呢？

请听我娓娓道来。先看下面两个概念：

- **对称加密**

- **非对称加密**

你知道上面两个概念是什么意思么？😳

🤣OK，不管你懂不懂，我先用我的方式来给你解释下：

**亲，你作过弊么？**😑不要告诉我在你漫长的学生生涯里你没作过弊(那你的学生生涯得多枯燥)，作弊我们常用的方法是啥？(说把答案写在胳膊大腿纸条上的同学请你出去，谢谢🙂)当然是加密了！比如我出于人道主义，想要帮助小明同学作弊，首先考试前我们会约定好一个暗号来传递选择题的答案，摸头发——A，摸耳朵——B，咳嗽——C，跺脚——D，于是一个加密方法就诞生了，这个加密方法只有我和小明知道，老师虽然看我抓耳挠腮但他顶多把我当成神经病，并没有直接证据说我作弊。好，**这种我和小明知道，别人不知道的加密方法就是一种对称加密算法**,对称加密算法也是我们日常最常见的加密算法。这种算法🔑只有一把，加密解密都用同一把钥匙，一旦🔑泄露就全玩完了。

随时时代的进步，人们发现实际上加密和解密不用同一把🔑也是可以的，只要加密和解密的两把🔑存在某种关系就行了。

于是，层出不穷的非对称加密算法就被研究了出来，那么它基于什么样的道理呢？请严格记住下面这句话：

**将a和b相乘得出乘积c很容易，但要是想要通过乘积c推导出a和b极难。即对一个大数进行因式分解极难**

听不懂因式分解的童鞋先去面壁5分钟，这么多年数学白学了？甩给你维基百科链接，自行补课🙂：[因式分解](https://zh.wikipedia.org/zh-cn/%E5%9B%A0%E5%BC%8F%E5%88%86%E8%A7%A3)

好的，我们继续，非对称加密算法就多了两个概念——公钥c和私钥b。

用法如下：**公钥加密的密文只能用私钥解密，私钥加密的密文只能用公钥解密。**

公钥我们可以随便公开，因为别人知道了公钥毫无用处，经过公钥加密后的密文只能通过私钥来解密。而想要通过公钥推导出a和b极难。但很明显的是，使用非对称加密效率不如对称加密，因为非对称加密需要有计算两个密钥的过程。

我们通过密码学中的两个典型的[爱丽丝和鲍勃](https://zh.wikipedia.org/wiki/%E6%84%9B%E9%BA%97%E7%B5%B2%E8%88%87%E9%AE%91%E4%BC%AF)人物来解释这个非对称加密算法的过程：

**客户端叫做爱丽丝，服务器叫做鲍勃。**

> 爱丽丝： 鲍勃我要给你发送一段消息，把你的公钥给我吧；
>
> 鲍勃： OK，这是我的公钥：234nkjdfdhjbg324**；
>
> 爱丽丝：收到公钥，我给你发送的消息经过公钥加密之后是这样的：#$#$@#@!$%*(@;
>
> 鲍勃：好的，收到了，亲，我来用我的私钥解密看下你真正要给我发送的内容；

上述过程就是一个**非对称加密**的过程，这个过程安全么？好像是很安全，即使**查理**(通信中的第三位参加者)截取了密文和公钥没有私钥还是没法得到明文。😂非对称加密的典型代表算法：RSA算法，笔者在另一篇博客:[RSA算法详解](http://blog.damonare.cn/2017/12/31/RSA%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3/#more)中也有详细的介绍。

可如果第三者查理发送给爱丽丝他自己的公钥，然后爱丽丝用查理给的公钥加密密文发送了出去，查理再通过自己的私钥解密，这不就泄露信息了么？我们需要想个办法让爱丽丝判断这个公钥到底是不是鲍勃发来的。

于是就有了**数字证书**的概念：

> 数字证书就是互联网通讯中标志通讯各方身份信息的一串数字，提供了一种在Internet上验证通信实体身份的方式，数字证书不是[数字身份证](https://baike.baidu.com/item/%E6%95%B0%E5%AD%97%E8%BA%AB%E4%BB%BD%E8%AF%81)，而是身份认证机构盖在数字身份证上的一个章或印（或者说加在数字身份证上的一个签名）。

😑上面官方的解释看起来就头大。其实它就是一段信息。

数字证书内容大体如下：

- 签发证书的机构
- 鲍勃的加密算法
- 鲍勃所使用的Hash算法
- 鲍勃的公钥
- 证书到期时间
- 等等

数字证书是由权威机构——CA机构统一来进行发行，我们绝对信任这个机构，至于CA机构的安全性…反正99.99%之下都是安全的。🕵

为了防止中间有人对证书内容进行更改，有了一个**数字签名**的概念，所谓的数字签名就是把以上所有的内容做一个Hash操作，得到一个固定长度然后再传给鲍勃。然而如果别人截取了这个证书然后更改内容，同时生成了新的Hash值那怎么办？处于这个考虑，CA机构在颁发这个证书的时候会用自己的私钥将Hash值加密，从而防止了数字证书被篡改。

好，我们来梳理下整个过程：

- **第一步：**首先，当爱丽丝开启一个新的浏览器第一次去访问鲍勃的时候，会先让爱丽丝安装一个**数字证书**，这个数字证书里包含的主要信息就是CA机构的公钥。
- **第二步：**鲍勃发送来了CA机构颁发给自己的数字证书，爱丽丝通过第一步中已经得到的公钥解密CA用私钥加密的Hash-a(**这个过程就是非对称加密**)，然后再用传递过来的HASH算法生成一个Hash-b，如果Hash-a === Hash-b就说明认证通过，确实是鲍勃发过来的。

如上，是整个数字证书的使用过程就是这样的。

多说一句，非对称加密实际应用的例子除了SSL还有很多，比如**SSH**、**电子签名**等；

如上提到的，非对称加密计算量很大，效率不如对称加密，我们打开网页最注重的是啥？是速度！是速度！是速度！🏃🏃🏃

**这点SSL就玩的很巧妙了🤣**，通信双方通过对称加密来加密密文，然后使用非对称加密的方式来传递对称加密所使用的密钥。这样效率和安全就都能保证了。

#### SSL协议的握手过程

先用语言来阐述下：

1. **第一步**：爱丽丝给出支持SSL协议版本号，一个客户端**随机数**(Client random，请注意这是第一个随机数)，客户端支持的加密方法等信息；

2. **第二步：**鲍勃收到信息后，确认双方使用的加密方法，并返回数字证书，一个服务器生成的**随机数**(Server random，注意这是第二个随机数)等信息；

3. **第三步：**爱丽丝确认数字证书的有效性，然后生成一个新的**随机数**(Premaster secret)，然后使用数字证书中的公钥，加密这个随机数，发给鲍勃。

4. **第四步：**鲍勃使用自己的私钥，获取爱丽丝发来的**随机数**(即Premaster secret)；(第三、四步就是非对称加密的过程了)

5. **第五步：**爱丽丝和鲍勃通过约定的加密方法(通常是[AES算法](https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%A7%E5%8A%A0%E5%AF%86%E6%A0%87%E5%87%86))，使用前面三个随机数，生成**对话密钥**，用来加密接下来的通信内容.

   摘自http://blog.damonare.cn/2017/12/29/SSL%E5%8D%8F%E8%AE%AE%E4%B9%8B%E6%95%B0%E6%8D%AE%E5%8A%A0%E5%AF%86%E8%BF%87%E7%A8%8B%E8%AF%A6%E8%A7%A3/#more



#### 生成器开启的两种方式

```python
def f():
    while True:
        x = yield 1
        print(x)
# f = f() 不推荐这种写法，f应该是一个函数变量
f1 = f() 
print(f1)
输出结果:
<generator object f at 0x7f4cd1e074c0> # 生成器对象
# 第一种开启方式
f1.send(None) # 到yield停住，返回了一个1
# 第二种开启方式
next(f1) # 到yield停住，返回一个1
# 之后next和send都可以重新启动生成器，区别:
next:重新启动生成器，但是不发送信息
f1.send(10)重新启动生成器，并且发送信息10，生成器函数中用x接收。
```



#### Pycharm中，导入的库没安装或没导入时，可以按alt+enter键自动导入或安装。

Pycharm中,pip安装的包是通过https://pypi.python.org/simple中下载并安装的，但速度比较慢，可以把源改成https://mirrors.aliyun.con/pypi/simple



#### 爬虫jobs暂停



#### linux视频软件 MPV MEDIA PLAYER



直接一个程序无法中断，只能先完成再去完成另一个消息。



#### str.lstrip和str.rstrip

```python
def lstrip(self, chars=None): 
	"""
	S.lstrip([chars]) -> str
        
    Return a copy of the string S with leading whitespace 	removed.
    If chars is given and not None, remove characters in chars instead.
    """
    return ""
```

```python
def rstrip(self, chars=None): # real signature unknown; restored from __doc__
    """
    S.rstrip([chars]) -> str

    Return a copy of the string S with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    """
    return ""
```

```python
>>> str = 'xxxabcxxx'
>>> print(str.lstrip('x'))
'abcxxx'
>>> print(str.rstrip('x'))
'xxxabc'
>>> print(str.rstrip('x').lstrip('x'))
'abc'
```



#### 阻塞队列

```python
urls_queue.join()
```

> 阻塞队列（BlockingQueue）是一个支持两个附加操作的队列。这两个附加的操作是：在队列为空时，获取元素的线程会等待队列变为非空。当队列满时，存储元素的线程会等待队列可用。阻塞队列。



#### 阻塞线程
```python
import threading
import time
def hello():
    time.sleep(4)
    print('hello')
t = threading.Thread(target=hello)
t.start()
t.join() # 线程阻塞
print('结束')
"""
如果加了t.join那么主线程会等子线程t运行结束后再执行，相当于代码会卡在t.join()这里直至子线程t运行完毕然后再执行print('结束')
"""
```



#### 阻塞进程

```python
"""
主进程会等待所有使用过.join方法的子进程运行结束后再运行。
"""
```



#### Pycharm连按两次shift即可全局搜索



#### flask断点测试

from ipdb import set_trace

set_trace()