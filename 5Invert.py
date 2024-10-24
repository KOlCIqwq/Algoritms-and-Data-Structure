s = input()
out = ""
for i in range(len(s) - 1, 0, -1):
          out += s[i]
out += s[0]
print(out)