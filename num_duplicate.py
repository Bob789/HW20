def marge_list(s1: list[int], s2: list[int]) -> list[int]:
    l1 = len(s1+s2)
    index = 0
    list_n: list[int] = []
    while index < l1:
        if len(s1) and len(s2):
            if s1[0] < s2[0]:
                list_n.append(s1.pop(0))
            elif s1[0] > s2[0]:
                list_n.append(s2.pop(0))
            else:
               s1.pop(0)
        else:
            if not len(s1):
                list_n.extend(s2)
            else:
                list_n.extend(s1)
                return list_n
        index += 1
    return list_n

s_list1 = [11, 27, 33, 49, 51, 77, 85, 99]
s_list2 = [0, 27, 33, 35, 52, 83, 85, 89, 91]

print(f" duplicate   : {s_list1}")
print(f" duplicate   : {s_list2}")
print(f" no duplicate   : {marge_list(s_list1, s_list2)}")
