### 十秒钟取不到自动退出循环

```python
l = [1, 2, 3, 4, 5]
flag = 0
while True:
    if flag:
        if time.time() - start_time > 10:
            break
    try:
        item = l.pop()
        flag = 0
        print(item)
    except IndexError:
        if flag == 1:
            continue
        flag = 1
        start_time = time.time()
```



### 单元测试还是有必要的。

### sqlalchemy中

default是指sqlalchemy帮你在插入数据的时候自动加默认值，而server_default是指直接在创建表的时候就指定default。