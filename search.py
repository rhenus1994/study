def get_keys(lst: list):
    result = []
    for item in lst:
        result += item.keys()
    return result


def get_children(lst, key):
    for item in lst:
        if key in item:
            return item[key]


def retrieve(d, path: str):
    ptr = d
    for p in path.split(','):
        if isinstance(ptr, dict):
            ptr = ptr[p]
        elif isinstance(ptr, list):
            ptr = get_children(ptr, p)
    return get_keys(ptr)


def has_children(d, path: str):
    return False if not retrieve(d, path) else True


def find(d, key):
    stack = list()
    source = list(d.keys())[0]
    if source == key:
        return source
    stack.append(source)
    while len(stack) != 0:
        path = stack.pop()
        items = retrieve(d, path)
        for item in items:
            abspath = ','.join([path, item])
            if item == key:
                return abspath
            if has_children(d, abspath):
                stack.append(abspath)
    return '不存在关键字, {}'.format(key)


if __name__ == '__main__':
    d1 = {'机器学习': [{'线性模型': []}, {'神经网络': [{'神经元模型': []}]}, {'强化学习': []}]}
    d2 = {'机器学习': [{'线性模型': [{'线性回归': [{'最小二乘法': []}]}]}, {'神经网络': [{'神经元模型': [{'激活函数': []}]}, {'多层网络': [{'感知机': []}, {'连接权': []}]}]}, {'强化学习': [{'有模型学习': [{'策略评估': []}, {'策略改进': []}]}, {'免模型学习': [{'蒙特卡洛方法': []}, {'时序差学习': []}]}, {'模仿学习': [{'直接模仿学习': []}, {'逆强化学习': []}]}]}]}
    # print(find(d1, '神经元模型'))
    print(find(d2, '连接权'))
