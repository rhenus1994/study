

链式调用只能是一直返回被修改过的对象。

所以一个类继承list，他也可以拥有这样的效果

\_\_slots\_\_

```__new__()```方法

```
mah_list = MahjongList().append(1)
print(mah_list)
```

```
# def __new__(cls, *args, **kwargs):
#     return list.__new__(list)

```



在类里面print(\_\_name\_\_)

然后打印类看看