
m_keys = []  # str
m_values = []  # str

def keys() -> list[str]:
    return m_keys

def values() -> list[str]:
    return m_values

def items() -> list[tuple[str, str]]:
    a: list[tuple[str, str]] = []
    for i in range(len(m_keys)):
        a.append({m_keys[i], m_values[i]})
    return a

# difficult
def update(dict1: dict[str, str]) -> None:
    pass

def pop(key: str) -> str:
    s = m_keys[-1]
    if len(m_keys) > 0:
        m_keys.remove(m_keys[-1])
        m_values.remove(m_values[-1])

    return s


def get(key: str, msg: str = None) -> str:
    if key in m_keys:
        return m_values[m_keys.index(key)]


def clear() -> None:
    pass

# add if not exist, if exist do nothing
def setdefault(key: str, value: str) -> None:
    if not key in m_keys:
        m_keys.append(key)
        m_values.append(value)

#update({'name': 'sharon'})
setdefault('name', 'sharon')
setdefault('city', 'Tel aviv')
setdefault('city', 'Tel aviv')
print(items())  # [('name', 'sharon'), ('city', 'Tel aviv')]
print(get('name', 'not exist'))  # sharon
print(get('age', 'not exist'))  # not exist
print(keys())  # ['name', 'city']
print(values())  # ['sharon', 'tel Aviv']
print(pop('name'))  # sharon
print(items()) # [('city', 'Tel aviv')]
# clear()
# print(items())  # []