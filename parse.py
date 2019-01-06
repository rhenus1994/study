def split_lines(s: str):
    return [line.strip() for line in s.split('\n') if line.strip()]


def count_start_comma(s: str):
    count = 0
    while s.startswith(','):
        count += 1
        s = s[1:]
    return count


def restore(lst: list):
    restore_list = []
    for index, line in enumerate(lst):
        comma_num = count_start_comma(line)
        lst = line.lstrip(',').split(',')
        if not comma_num:
            restore_list.append(lst)
            continue
        line = restore_list[index - 1][:comma_num] + lst
        restore_list.append(line)
    return restore_list


def append_node(initial, lst):
    ptr = initial
    for item in lst:
        if isinstance(ptr, dict):
            ptr = ptr.setdefault(item, [])
        elif isinstance(ptr, list):
            for p in ptr:
                if item in p.keys():
                    ptr = p[item]
                    break
            else:
                node = {item: []}
                ptr.append(node)
                ptr = node[item]
    return initial


def parse_to_json(s):
    lst = restore(split_lines(s))
    initial = {}
    for i in lst:
        append_node(initial, i)
    return initial


if __name__ == '__main__':
    s1 = """机器学习,线性模型
    ,神经网络
    ,,神经元模型
    ,强化学习
    """
    s2 = """机器学习,线性模型,线性回归,最小二乘法
    ,神经网络,神经元模型,激活函数
    ,,多层网络,感知机
    ,,,连接权
    ,强化学习,有模型学习,策略评估
    ,,,策略改进
    ,,免模型学习,蒙特卡洛方法
    ,,,时序差学习
    ,,模仿学习,直接模仿学习
    ,,,逆强化学习
    """
    import sso
    # print(parse_to_json(s1))
    # print(parse_to_json(s2))
    import re
    from http import HTTPStatus

    print(re.fullmatch(r'\d*', '123a'))
    from flask import abort