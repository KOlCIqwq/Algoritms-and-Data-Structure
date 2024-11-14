def rep(s):
    first = s[0]
    border = [first]
    i = 0
    while i < len(s):
        j = 0
        if s[i] == first and len(border) == 1:
            j = i + 1
            while j != len(s) and s[j] != first:
                border.append(s[j])
            i = j
            j = 0
        elif s[i] == first and len(border) != 1:
            while j < len(border) and border[j] == s[i + j]:
                border.append(s[i + j])
        else:
            return 0
    return len(border)

s = str(input())
print(rep(s))
