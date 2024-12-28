with open("huffman.in", "r") as input:
    n = int(input.readline().strip())
    a = list(map(int, input.readline().strip().split()))

a.sort()

r = 0
m1, m2 = 0, 0
i, j = 0, 0

s = []

for k in range(n - 1):
    if i < len(a) and (j >= len(s) or a[i] <= s[j]):
        m1 = a[i]
        i += 1
    else:
        m1 = s[j]
        j += 1
        
    if i < len(a) and (j >= len(s) or a[i] <= s[j]):
        m2 = a[i]
        i += 1
    else:
        m2 = s[j]
        j += 1

    s.append(m1 + m2)
    r += s[-1] 

with open("huffman.out", "w") as output:
    output.write(str(r) + '\n')
