def swap_case(s):
    mod_str = []
    for char in s:
        if char == char.lower():
            mod_str.append(char.upper())
        elif char == char.upper():
            mod_str.append(char.lower())
    return "".join(mod_str)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
