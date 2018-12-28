import yaml


def get_slot(s: str):
    return s.split('=', maxsplit=1)[0]


def split_slot(s: str):
    return s.split('.')


def get_split(raw: str):
    s = get_slot(raw)
    return split_slot(s)


def parse_model(filename: str):
    with open(filename) as f:
        obj = yaml.safe_load(f.read())
    d = dict()
    for item in obj:
        parts = get_split(item)
        for n, v in enumerate(parts):
            s = '.'.join(parts[:n + 1])
            d[s] = d.setdefault(s, 0) + 1


if __name__ == '__main__':
    import sys
    import inspect
    inspect.getmembers(sys.modules[__name__], inspect.isclass)