



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

```python
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

老师之前用到的只是在整个项目中的某一个文件自定义一个类，然后在该py文件中实例化一个对象，别的文件调用这个实例化过一次的类的对象就叫他单例模式

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



1、halt   立刻关机 2、poweroff  立刻关机 3、shutdown -h now 立刻关机(root用户使用) 

linux有postman客户端

1、reboot 2、shutdown -r now 立刻重启(root用户使用）



#### Pycharm中快速打印print('a')的方法->'a'.print

模板中快速遍历，直接for然后按tab键，就直接出来了。



#### python可视化工具pyecharts

Echarts是百度出的很有名 也很叼。  Echarts 是百度开源的一个数据可视化 JS 库。主要用于数据可视化。  pyecharts 是一个用于生成 Echarts 图表的类库。实际上就是 Echarts 与 Python 的对接。



python数据可视化库seaborn,matplotlib,pyecharts

python数据分析:Numpy,pandas,scipy



list方法insert

```python
def insert(self, index, p_object): 
    """ L.insert(index, object) -- insert object before index """
    pass
l = [1, 2]
```



#### 浏览器强制刷新ctrl+shift+R

pycharm整理代码ctrl + alt + L



#### re模块

```python
# 若都能匹配到，则
>>> res1 = re.match('hello','hello world')
>>> type(res1)
<class '_sre.SRE_Match'>
>>> res2 = re.search('hello','hello world')
>>> type(res2)
<class '_sre.SRE_Match'>
>>> res3 = re.findall('hello','hello world')
>>> type(res3)
<class 'list'>
# .group()只能是re.match()和re.search()后的对象使用。group(0)代表匹配到的字符串，group(1)代表自定义的内部小组。group('key')代表你自定义的参数匹配，例如(?P<key>\d+)此类形式。
# re.findall()方法返回的是个字符串，如果有自定义分组两个及以上，则返回列表，列表内元素为元组，例如
import re
s = '/2/3/4/5dsadadsas'
r = '(\d+)(/)'
res3 = re.findall(r, s)
print(res3)
# 结果[('2', '/'), ('3', '/'), ('4', '/')]
```



#### pycharm取消联想使用esc



#### string库

```python
string.py
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
string.capword(s, sep=None) # 将一段话的首字母大写。
```



#### 将一句话的首字母大写

```python
def capword(s, sep=None)：
	# return (sep or ' ').join(list(map(lambda x: x.capilize(), s.split(sep))))
    return (sep or ' ').join(i.capitalize() for i in s.split(sep))
a = "hi i'm mike"
print(capword(a))
# 输出结果 -> Hi I'm Mike
```

str.join()里面可以直接加列表生成器

```python
>> print(''.join(i for i in ['a', 'b']))
'ab'
```



#### 判断一个字符串是不是数字还是字母

```python
s.isdigits() # 判断字符串里是不是全是数字
s.isalpha() # 判断字符串里是不是全是字母
s.isalnum() # 判断字符串里是不是字母和数字的组合
```



#### Pycharm的Structure中的函数和类的顺序是按照字母顺序排列的



#### Python中super的用法

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。总之前人留下的经验就是：保持一致性。要不全部用类名调用父类，要不就全部用 super，不要一半一半。

普通继承

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```python
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print 'Parent'
    
    def bar(self,message):
        print message, 'from Parent'
        
class FooChild(FooParent):
    def __init__(self):
        FooParent.__init__(self)
        print 'Child'
        
    def bar(self,message):
        FooParent.bar(self,message)
        print 'Child bar function.'
        print self.parent
        
if __name__=='__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
```

 

super继承

```python
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print 'Parent'
    
    def bar(self,message):
        print message,'from Parent'

class FooChild(FooParent):
    def __init__(self):
        super(FooChild,self).__init__()
        print 'Child'
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print 'Child bar fuction'
        print self.parent

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
```



程序运行结果相同，为：

Parent
Child
HelloWorld from Parent
Child bar fuction
I'm the parent.
从运行结果上看，普通继承和super继承是一样的。但是其实它们的内部运行机制不一样，这一点在多重继承时体现得很明显。在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）。
注意：super继承只能用于新式类，用于经典类时就会报错。
新式类：必须有继承的类，如果没什么想继承的，那就继承object
经典类：没有父类，如果此时调用super就会出现错误：『super() argument 1 must be type, not classobj』

 

更详细的参考

http://blog.csdn.net/johnsonguo/article/details/585193

总结
　　1. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，
       产生了一个super对象；
　　2. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
　　3. super(B, self).func的调用并不是用于调用当前类的父类的func函数；
　　4. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数
       只调用一次（如果每个类都使用super）；
　　5. 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一
       个父类函数被调用多次。

摘自https://www.cnblogs.com/wjx1/p/5084980.html



#### super内的参数可以省略

```python
class Animal:
    def run(self):
        print('run')

class Cat(Animal):
    def run(self):
        print(super())
        super().run() 
        # 详写 super(Cat, self).run()
c = Cat()
c.run()
输出:
<super: <class 'Cat'>, <Cat object>> # super类
run
```



#### 字典的get方法

```python
def get(self, k, d=None): # real signature unknown; restored from __doc__
    """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
    pass
```

```python
d = dict(name='lily', age=13)
print(d.get('class'))
结果: None
    
```



#### os.path.basename()和os.path.dirname()

```python
>>> print(os.path.basename('/usr/bin/python3.6')) # 文件名
>>> print(os.path.dirname('/usr/bin/python3.6')) # 目录名
python3.6
/usr/bin
```



#### str.partition()方法

```python
 def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass
```

```python
>>> s1 = 'a;b'
>>> s1.partition(';')
('a', ';', 'b')
>>> s2 = 'a;b;c'
>>> s2.partition(';')
('a', ';', 'b;c)
>>> s2.partition('/')
('a;b;c', '', '')
```



#### 在python中切忌不要使用str,list,print等builtins.py内自带的方法

```python
>>> str = 'aaa'
>>> b = str(123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
# 相当与重写了str这个对象 本来str是一个类，现在重新赋值变成字符串'aaa'了

>>> str
<class 'str'>
>>> str = 'aaa'
>>> str
'aaa'

>>> print
<built-in function print>
>>> print = 1
>>> print
1
>>> print(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```



#### enumerate用法

```python
>>> arr = [1, 2, 3]
>>> enumerate(arr)
<enumerate object at 0x7fd19f0c74c8>
>>> list(enumerate(arr))
[(0, 1), (1, 2), (2, 3)]
>>> for i, v in enumerate(arr):
... 	i ,v
(0, 1)
(1, 2)
(2, 3)
```



#### json.dumps()返回一个json字符串

```python
Serialize ``obj`` to a JSON formatted ``str``
# 序列化一个对象使其转化为JSON格式的字符串
# 例如
>>> m = json.dumps({'name':'lily','age':13})
'{"name": "lily", "age": 13}'
>>> type(m)
<class 'str'>
```



#### def f(x, \*, y)中\*的作用

相当于是位置参数和关键字参数的分割，\*号前面是位置参数，*号后面是关键字参数。所以def f(x, \*, y, z):和def f(x, *, y=None, z=None):都可以，但在之后赋值的时候关键词参数部分必须要以关键词参数赋值。

```python
def f(x, *, y, z, k):
    print(x +y +z + k)

f(1, 2, 3, 4)
TypeError: f() takes 1 positional argument but 4 were given # 所以相当于星号前面赋值时要传递位置参数，星号后面要传递关键字参数

f(1, y=2, z=3, k=4)
10
# 函数定义时星号后面的形参加不加默认值都没关系
def f1(x, *, y, z=None, k):
    print(x +y +z + k)
def f2(x, *, y=None, z=None, k=None)
    print(x +y +z + k)
```





#### 什么是序列化

序列化是把模型对象转化为JSON格式然后响应出去，便于客户端进行数据分析。



#### shift+F6 全局修改变量名



#### time模块

```python
# 返回当前时间的时间戳，浮点数，不需要参数
c = time.time()
print(c)

# 将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=21, tm_hour=16, tm_min=22, tm_sec=30, tm_wday=1, tm_yday=233, tm_isdst=0)
# 将时间戳转为本地时间元组
b = time.localtime(c)
print(b)
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=22, tm_hour=0, tm_min=22, tm_sec=30, tm_wday=2, tm_yday=234, tm_isdst=0)
# 将本地时间转为时间戳
m = time.mktime(b)
print(m)

# 将时间元组转为字符串
s = time.asctime(b)  # Tue Apr 24 11:35:29 2018
print(s)
print(type(s))
Wed Aug 22 00:22:30 2018
# 将时间戳转为字符串
p = time.ctime(c)
print(p)

# 将时间元组转为指定格式的时间的字符串
# time.strftime(我们规定的时间格式, 时间元组)
q = time.strftime("%y-%m-%d  %X", b)
print(q)
18-08-22  00:22:30
# 将时间字符串转为指时间元组
w = time.strptime(q, "%y-%m-%d %X")
print(w)

```





#### 倒计时计时器

```python
import time
import sys

num = 10
while num:
    # sys.stdout.write(str('\r%s'%num))
    print('\r%s' % num) 
    num -= 1
    time.sleep(1)
# 注:\r要放前面，放后面起不到预期效果。
```



#### property类

```python
class property(object):
    """
    property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
    
    fget is a function to be used for getting an attribute value, and likewise
    fset is a function for setting, and fdel a function for del'ing, an
    attribute.  Typical use is to define a managed attribute x:
    
    class C(object):
        def getx(self): return self._x
        def setx(self, value): self._x = value
        def delx(self): del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")
    
    Decorators make defining new properties or modifying existing ones easy:
    
    class C(object):
        @property
        def x(self):
            "I am the 'x' property."
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x
    """
```



#### python nonlocal,global

```python
x = 100


def func():
    global x
    x = 5

    def funny():
        nonlocal x
        # global x
        # x = 1
        x += 1
        print(x)
        # return x

    funny()
    print(x)


func()
print(x)
结果:
	nonlocal x
    	^
SyntaxError: no binding for nonlocal 'x' found
```

改成

```python
x = 100


def func():
    nonlocal x
    x = 5

    def funny():
        nonlocal x
        # global x
        # x = 1
        x += 1
        print(x)
        # return x

    funny()
    print(x)


func()
print(x)
结果:
    nonlocal x
    ^
SyntaxError: no binding for nonlocal 'x' found
# 也会报同样的错误
```



#### python是如何进行内存管理的

**a、对象的引用计数机制**

python内部使用引用计数，来保持追踪内存中的对象，Python内部记录了对象有多少个引用，即引用计数，当对象被创建时就创建了一个引用计数，当对象不再需要时，这个对象的引用计数为0时，它被垃圾回收。

**b、垃圾回收**

1>当一个对象的引用计数为零时，它将被垃圾收集机制处理掉。

2>当两个对象a和b互相引用时，del语句可以减少a,b的引用计数，并销毁引用底层对象的名称。然而由于每个对象都包含一个对其他对象的引用，因此引用计数不会归零，对象也不会销毁。（从而导致内存泄漏）。为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问对象的循环并删除它们。

**c、内存池机制**

Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回操作系统。

1>Pymalloc机制。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。

2>Python中所有小于256字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的malloc。

3>对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能分配给浮点数了。



#### list.insert()方法

```python
def insert(self, index, p_object): # real signature unknown; restored from __doc__
    """ L.insert(index, object) -- insert object before index """
    pass

l = [1, 2, 3]
l.insert(1, 4)
print(l)
结果:
[1, 4, 2, 3]
```



#### list.pop()方法

```python
def pop(self, index=None): # real signature unknown; restored from __doc__
    """
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
    """
    pass

>>> l = [1, 2, 3]
>>> l.pop(1)
2
>>> l
[1, 3]
>>> l.pop() # 默认删除最后一个元素
3
>>> l
[1]
```



#### Python关键词就是除了builtins.py中的方法，函数，变量，类之外的可以不用导入任何库就能直接使用的

```shell
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                
```



#### re.sub()方法将字符串中的 old（旧字符串） 替换成 new(新字符串)

```python
def sub(pattern, repl, string, count=0, flags=0):
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used."""
    return _compile(pattern, flags).sub(repl, string, count)
```

```python
import re
print(re.sub('\s', '*', "Hello I'm Mike!"))
结果：
Hello*I'm*Mike!
# 将字符串里的空白字符转化为*号
```



#### python深拷贝浅拷贝

python中对于列表，集合，字典，如果浅拷贝那么拷贝出来的对象和原对象内存地址相同，如若是深拷贝，拷贝出来的对象和原对象内存地址不同。

```python
import copy
l1 = [1, 2, 3]
print(id(l1))
l2 = copy.deepcopy(l1) # 深拷贝，原对象内存地址不同
print(id(l2))
l3 = copy.copy(l1) # 浅拷贝，与原对象内存地址相同
print(id(l1))

结果:
140048729134216
140048729133704
140048729134216
```



#### str.find()方法

```python
def find(self, sub, start=None, end=None): 
    """
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
    """
    return 0
```

str.find()方法，返回在字符串中找到的第一个子串的下标。如果找不到，就返回-1。

```python
>>> s = 'abc,dea'
>>> s.find('a')
0
>>> s.find('f')
-1
```



#### random.shuffle()方法

```python
def shuffle(self, x, random=None):
    """Shuffle list x in place, and return None.

    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.

    """
```

random.shuffle()方法传入一个列表参数，返回值为None.运行这个方法后，列表内的值会重新排列，而且是随机排列。

```python
>>> import random
>>> l = [1, 2, 3, 4]
>>> print(random.shuffle(l))
None
>>> l
[4, 1, 2, 3]
```



#### Python内置的eval()方法



**描述**

eval() 函数用来执行一个字符串表达式，并返回表达式的值。

**语法**

以下是 eval() 方法的语法:

```
eval(expression[, globals[, locals]])
```

**参数**

- expression -- 表达式。
- globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
- locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

**返回值**

返回表达式计算结果。

------

**实例**

以下展示了使用 eval() 方法的实例：

```python
>>> eval('8')
8
>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> n=81
>>> eval("n + 4")
85
```



#### 如何去除字符串中的所有空白字符

- 去除两边空白字符:str.strip()
- 去除两边及中间空白字符:''.join(str.split())
- 去除两边及中间空白字符:re.sub('\w', '', str)



#### type方法可以直接获取对象的类，调用即可实例化

```python
>>> cls = type([1, 2, 3])
>>> l = cls()
>>> l
[]
>>> l.append(1)
>>> l
[1]
```



#### 异或

如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。



#### Pycharm将一个变量的名称全局修改

Ctrl+R 然后选择replace all

还有SHIFT+F6也能达到同样的效果



#### Python类里面定义了\_\_repr\_\_的

```python
>>> class A:
...     def __repr__(self):
...             return 'hello'
... 
>>> a = A()
>>> a
hello
>>> print(a)
hello
```

类里定义了\_\_repr\_\_方法，那么无论是在python交互环境直接输入该类的实例化对象，还是print该类的实例化对象，都会调用该方法。



#### i.e.、e.g.、etc.

![124044119_1_20180206092712128](/home/andy/Desktop/Notes/124044119_1_20180206092712128.jpeg)



#### raise后面要写上错误信息的详细说明

```python
raise IndexError

结果:
Traceback (most recent call last):
  File "/home/andy/PycharmProjects/contest/test.py", line 1, in <module>
    raise IndexError
IndexError
```

但这样错误信息里会出现raise语句，会比较奇怪

```python
raise IndexError(
    'Out of Index!'
)

结果:
Traceback (most recent call last):
  File "/home/andy/PycharmProjects/contest/test.py", line 2, in <module>
    'Out of Index!'
IndexError: Out of Index!
```

所以在错误类别后加上错误的详细说明，就能呈现比较自然的错误信息了，而且还可以自定义错误信息。



#### 所有类都是type的实例化对象，但所有类的共同父类是object

```python
from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):

    @abstractmethod
    def load(self, input):
        return

    @abstractmethod
    def save(self, output, data):
        return


class B(object):
    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


print(isinstance(A, ABCMeta)) # True
print(isinstance(A, type)) # True
print(isinstance(B, ABCMeta)) # True
print(isinstance(B, type)) # True
print(issubclass(A, object)) # True
print(issubclass(type, object))# True
print(issubclass(ABCMeta, object)) # True
print(issubclass(B, A)) # True
print(isinstance(B(), A)) # True
```



#### 继承一个类后，直接pass就能继承父类的方法与属性

```python
class A:
    def __init__(self, name):
        self.name = name
    def run(self):
        return '{0} is there!'.format(self.name)

class B(A):
    pass


b = B('lily')
print(b.name) 
'lily'
print(b.run())
'lily is there!'
```



#### 格式化输出f'{arg}'

```python
name = 'lily'
print(f'{name} is good girl!')
'lily is a good girl'
```



#### return a, b 会返回一个元组

```python
def test(a, b):
    return a, b
print(test(1, 2))
结果:
(1, 2)
```



#### 魔术方法_\_str\_\_与\_\_repr\_\_的相同点与不同点

**相同点**

1. 在print该类的对象时，_\_str\_\_与\_\_repr\_\_都会直接打印在其方法内定义的return值，使对象的表现方式更加清晰。

**不同点**

1. 在python交互式窗口中直接输入该类的对象，仍会调用\_\_repr\_\_方法，

   但_\_str\_\_起不到效果。

2. 如果列表中含有对象，打印该列表时，对象的表现形式会调用\_\_repr\_\_方法，但_\_str\_\_起不到效果，以此类推，元组，字典，集合也是这种情况。

_\_str\_\_

```python
class A:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)


l = [A(1), A(2), A(3)]
print(l)
结果:
[<__main__.A object at 0x7f5ce7761128>, <__main__.A object at 0x7f5ce76ef630>, <__main__.A object at 0x7f5ce76b57b8>]

```

\_\_repr\_\_

```python
class A:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return str(self.num) # 返回值必须为字符串


l = [A(1), A(2), A(3)]
print(l)
结果:
[1, 2, 3]
```



#### 类中的私有变量

```python
class A:
    def __init__(self, num):
        self.__num = num

a = A(11)
print(a.__num)
结果:
AttributeError: 'A' object has no attribute '__num'
print(a._A__num)
11
```

可以通过.\_类名\_\_属性名来获取私有属性的值

同时，私有变量是无法被继承的

```python
class B(A):
    def get(self):
    	return self.__num

b = B(13)
print(b._B__num)
结果:
AttributeError: 'B' object has no attribute '_B__num'
print(b._A__num)
结果:
13
print(b.get())
结果:
AttributeError: 'B' object has no attribute '_B__num'
# 在类里调用self.__num会自动去找self._B__num属性
print(a.__dict__)
结果:
{'_A__num': 11}
print(b.__dict__)
结果:
{'_A__num': 13}
# 继承过来的是self._A__num属性
```



#### 类的\_\_dict\_\_和对象的\_\_dict\_\_的区别以及对象的\_\_dir\_\_方法

```python
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def travel(cls):
        print('travel')

    @staticmethod
    def drink():
        print('drink')

    def run(self):
        print(self, 'is run')

    def eat(self):
        print(self, 'is eat')

    def __repr__(self):
        return self.name


print(Cat.__dict__)
结果:
{'__module__': '__main__', '__init__': <function Cat.__init__ at 0x7fd884d5b0d0>, 'travel': <classmethod object at 0x7fd884d6a8d0>, 'drink': <staticmethod object at 0x7fd884d6a908>, 'run': <function Cat.run at 0x7fd884d5b7b8>, 'eat': <function Cat.eat at 0x7fd884d5b840>, '__repr__': <function Cat.__repr__ at 0x7fd884d5b8c8>, '__dict__': <attribute '__dict__' of 'Cat' objects>, '__weakref__': <attribute '__weakref__' of 'Cat' objects>, '__doc__': None}

print(Cat('lily', 13).__dict__)
结果:
{'name': 'lily', 'age': 13}

print(Cat('lily', 13).__dir__())
结果:
['name', 'age', '__module__', '__init__', 'travel', 'drink', 'run', 'eat', '__repr__', '__dict__', '__weakref__', '__doc__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

```

**类的\_\_dict\_\_方法返回的是类(如\_\_module\_\_)以及所有定义的方法，包括类方法，静态方法以及对象方法还有魔术方法。**

**对象的\_\_dict\_\_方法返回的只是对象的属性，不包含任何方法。**

**对象的\_\_dir\_\_方法返回的是一个列表，包含对象的所有属性，以及类的所有属性及方法，包括类方法，静态方法，对象方法以及所有的魔术方法。**



#### 对象的方法也可以由类来调用

```python
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self, 'is run')

    def __repr__(self):
        return self.name
lily = Cat('lily', 16)
Cat.run(lily)
输出:
'lily is run'

print(Cat.__repr__(lily))
输出:
'lily'

Cat.__init__(lily, 'mike', 15)
print(lily.name)
输出:
'mike'
print(lily.age)
输出:
15
```



#### 输入一个字符串str，输出最长的对称字符串长度

![699524491](/home/andy/Desktop/Notes/699524491.jpg)

```python
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
        try:
            if s[i] == s[i + 2]:
                count = 3
                key = 2 * i + 2
                while i - 1 >= 0 and key - i + 1 <= length - 1:
                    i = i - 1
                    if s[i] != s[key - i]:
                        break
                    count += 2
                list_s.append(count)
        except IndexError:
            continue
    return max(list_s)


print(count_sym('0o1o0'))
结果:
5
```



#### 循环里continue

```python
for i in range(1, 10):
    continue
    print(1)
# 1永远不会输出，因为python解释器一遇到continue就会开始下一次循环。while也同理
while True:
    continue
    print(1)
# 这里1也永远不会输出，因为循环体内一遇到continue就会进入下次循环
```



#### range反序遍历

```python
for i in range(5, 0, -1):
    print(i)
结果:
5
4
3
2
1
```

range反序遍历的话，大的数字放前面，小的数字放后面，最后在写个参数1代表反序，然后也是末尾的数取不到。在本案例中，即0取不到。



#### str.find和str.index的区别

python 字符串查找有4个方法，1 find, 2 index方法，3 rfind方法, 4 rindex方法

find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1

```python
info = 'abca'
print(info.find('a'))　#从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
 
info = 'abca'
print(info.find('a',1))　#从下标1开始，查找在字符串里第一个出现的子串，返回结果3
 
info = 'abca'
print(info.find('333')) #返回-1,查找不到返回-1

```

index()方法：python 的index方法是在字符串里查找子串第一次出现的位置，类似字符串的find方法，不过比find方法更好的是，如果查找不到子串，会抛出异常，而不是返回-1

```python
In [10]: info = ‘abca’
 
In [11]: info.index(‘a’)
Out[11]: 0
 
In [12]: info.index(’33’)
—————————————————————————
ValueError Traceback (most recent call last)
in ()
  —-> 1 info.index(’33’)
 
ValueError: substring not found
```

很显然，抛出了ValueError异常

!!! rfind 和 rindex 方法用法和上面一样，只是从字符串的末尾开始查找



#### list.index()方法

```python
 def index(self, value, start=None, stop=None): 
        """
        L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0
```

返回给定值第一次出现的索引，如果不存在，则抛出ValueError的异常。





