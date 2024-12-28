def LCS(a1, a2):
    dinprog = [[0 for _ in range(len(a2) + 1)] for _ in range(len(a1) + 1)]

    for i in range(len(a1) - 1, -1, -1):
        for j in range(len(a2) - 1, -1, -1):
            if a1[i] == a2[j]:
                dinprog[i][j] = 1 + dinprog[i + 1][j + 1]
            else:
                dinprog[i][j] = max(dinprog[i][j + 1], dinprog[i + 1][j])

    i, j = 0, 0
    indices_a1 = []
    indices_a2 = []

    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            indices_a1.append(i)
            indices_a2.append(j)
            i += 1
            j += 1
        elif dinprog[i + 1][j] >= dinprog[i][j + 1]:
            i += 1
        else:
            j += 1

    return dinprog[0][0], indices_a1, indices_a2


n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

if len(a1) != n or len(a2) != n:
    raise ValueError("Длина последовательностей должна быть равна n.")

k, indices_a1, indices_a2 = LCS(a1, a2)

print(k)
print(' '.join(map(str, indices_a1)))
print(' '.join(map(str, indices_a2)))
