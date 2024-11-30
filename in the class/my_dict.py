
m_keys = []  # str
m_values = []  # str

def keys() -> list[str]:
    return m_keys

def values() -> list[str]:
    return m_values

def items() -> list[tuple[str, str]]:
    # [ ( , ) , ( , ) ]
    # [ 'a', 'b', 'c', 'd']
    # [  9   2    5     ]
    # ('a' , 9), ('b', 2), ('c', 5')

    #1
    # result = []
    # for i in range(len(m_keys)):
    #     result.append( tuple([m_keys[i], m_values[i]]) )
    # return result
    #
    #2
    # return [(m_keys[i], m_values[i]) for i in range(len(m_keys))]

    #3
    return list(zip(m_keys, m_values))

# difficult
def update(update_dict: dict[str, str]) -> None:
    #{'Gladiator II': '82%',
    # "Mission: Impossible – Dead Reckoning Part One": '96%',
    # 'name': 'shani'}
    for key, value in update_dict.items():
        #print(key, value, end=",  ")
        if not key in m_keys:
            setdefault(key, value)
            continue
        index = m_keys.index(key)
        m_values[index] = value

def pop(key: str) -> str:
    # setdefault('name', 'sharon')
    # setdefault('city', 'Tel aviv')
    #                0       1
    # keys =   ['city']
    # values = ['tel aviv']
    if key in m_keys:
        index = m_keys.index(key)  # 0
        value = m_values.pop(index)  # sharon
        # value = m_values[index]
        del m_keys[index]
        return value
    else:
        raise KeyError(f'key {key}does not exist')

def get(key: str, msg: str = None) -> str:
    if key in m_keys:
        index = m_keys.index(key)
        value = m_values[index]
        return value
    else:
        return msg

def clear() -> None:
    m_keys.clear()
    m_values.clear()

# add if not exist, if exist do nothing
def setdefault(key: str, value: str) -> None:
    if not key in m_keys:
        m_keys.append(key)
        m_values.append(value)
    else:
        print(f'key {key} already exist')

#update({'name': 'sharon'})
setdefault('name', 'sharon')
setdefault('city', 'Tel aviv')
setdefault('city', 'Tel aviv')
print(items())  # [('name', 'sharon'), ('city', 'Tel aviv')]
print(get('name', 'not exist'))  # sharon
print(get('age', 'not exist'))  # not exist
print(keys())  # ['name', 'city']
print(values())  # ['sharon', 'tel Aviv']
print(items()) # [('city', 'Tel aviv')]
print(pop('name'))  # sharon
setdefault('zipcode', '90210')
clear()
print(items())  # []
setdefault('name', 'sharon')
print(items())
update({'Gladiator II': '82%',
        "Mission: Impossible – Dead Reckoning Part One": '96%',
        'name': 'shani'})
print(items())  # [('Gladiator II', '82%'),
        #           ("Mission: Impossible – Dead Reckoning Part One", '96%'),
        #           ('name', 'shani')]


