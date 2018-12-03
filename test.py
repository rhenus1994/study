import jsonpath


class Material:
    def __init__(self, content):
        self._content = content

    def _retrieve(self, key: str, priority='string'):
        """
        a.b.1.c..d.1
        []: ..key .index
        {}: ..key .key
        获取key值，key不存在则抛出KeyError异常
        ..代表递归搜索, .只搜索子节点
        :param key:
        :return: value
        """
        ptr = self.serializer()
        recursive = False
        for partition in key.split('.'):
            if recursive:
                assert partition, 'unsupported syntax \'...\''
                ptr = jsonpath.jsonpath(ptr, '$..%s' % partition)
                if not ptr:
                    raise KeyError('%s doesn\'t exist' % partition)
                recursive = False
                continue
            if partition.isdigit():
                if isinstance(ptr, list):
                    ptr = ptr[int(partition)]
                else:
                    if partition not in ptr and int(partition) not in ptr:
                        raise KeyError('%s and \'%s\' don\'t exist' % (partition, partition))
                    if priority == 'string':
                        ptr = ptr.get(ptr) or ptr.get(int(ptr))
                    elif priority == 'integer':
                        ptr = ptr.get(int(ptr)) or ptr.get(ptr)
            elif partition:
                ptr = ptr[partition]
            else:
                recursive = True
        return ptr

    def retrieve(self, key, default=None):
        """
        支持缺省值
        :param key: 嵌套的路径，"0.a.b"
        :param default: 缺省值
        :return:
        """
        try:
            return self._retrieve(key)
        except (KeyError, TypeError, AssertionError):
            return default


d = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
m = Material(d)
# print(m._get('store'))
# print(m._get('$..store'))
# print(jsonpath(d, '$..store'))
# print(m._retrieve('store..isbn1'))
# d = {'data':[{'name': ''}]}
# print(jsonpath.jsonpath(d, 'data..name'))
print(m.retrieve('store.book..category.0'))