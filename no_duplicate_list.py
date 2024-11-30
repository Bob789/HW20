def no_duplicate_list(s_list: list[int]) -> list[int]:

    for index, num in enumerate(s_list):
        if index >= len(s_list) - 1:
            break
        if s_list[index] == s_list[index+1]:
           s_list.pop(index)
    return s_list

s_list = [11, 27, 27, 33, 33, 49, 51, 77, 85, 99]

print(f" duplicate   : {s_list}")
print(f" no duplicate   : {no_duplicate_list(s_list)}")

