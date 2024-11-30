from colorama import Fore, Style, init
init(autoreset=True)

def is_valid_brackets(string: str) -> bool:
    b: bool = True# valid
    count = 0
    index = 1
    bracket_map = ['[', '{', '(', ']', '}', ')']
    pairs = [("[", "]"), ("{", "}"), ("(", ")")]
    sl = {
        # key, count , index
        "[": [0, []],
        "{": [0, []],
        "(": [0, []],
        "]": [0, []],
        "}": [0, []],
        ")": [0, []],
    }

    # count bracket
    for bracket in bracket_map:
        sl[bracket][count] = string.count(bracket)

    # check even bracket open vs closed
    for open_bracket, close_bracket in pairs:
        if sl[open_bracket][count] != sl[close_bracket][count]:
            b = False
            print(f"{Fore.RED}Error:SyntaxError: closing bracket does not match", open_bracket, ' ',close_bracket ,end=' ')
            return b

    # index each bracket in string
    for idx, char in enumerate(string):
        if char in bracket_map:
            sl[char][index].append(idx)

    # check if open bracket appear first then closed brackets
    for open_bracket, close_bracket in pairs:
        for i in range(len(sl[open_bracket][index])):# run in list index
            if sl[open_bracket][index][i] > sl[close_bracket][index][i]:
                print(f"{Fore.RED}Error:order bracket not match",open_bracket,' ',close_bracket ,end=' ')
                b = False
                return b

    # Check the substring between brackets for improper nesting
    for open_bracket, close_bracket in pairs:
        for open_idx, close_idx in zip(sl[open_bracket][index], sl[close_bracket][index]):
            substring_brackets = string[open_idx + 1:close_idx]
            for sub_open, sub_close in pairs:
                if substring_brackets.count(sub_open) != substring_brackets.count(sub_close):
                    print(f"{Fore.RED}Error: You have bracket not in the place: ", substring_brackets ,end=' ')
                    return False
    return b

list_bracket: list[str] = ["a[v(cc{d})ee]f", "a[b]c]d[e", "ad({dfd[g}bv]bv)", "(nv[]nv})vnv", "(v][n)mm", "(c([bc] ])nn{}[)", "[t(y])"]
for i , string in enumerate(list_bracket):
    print(f"string {i} {string}: ",end=' ')
    print( is_valid_brackets(list_bracket[i]))


