with open('input.txt', 'r') as input:
    s = input.read().strip()

a1 = list(s)
a2 = a1[::-1]

def LCS(a1, a2):
    dinprog = [[0 for _ in range(len(a2) + 1)] for _ in range(len(a1) + 1)]

    for i in range(len(a1) - 1, -1, -1):
        for j in range(len(a2) - 1, -1, -1):
            if a1[i] == a2[j]:
                dinprog[i][j] = 1 + dinprog[i + 1][j + 1]
            else:
                dinprog[i][j] = max(dinprog[i][j + 1], dinprog[i + 1][j])

    return dinprog

def find_palindrome(a1, dinprog):
    i, j = 0, 0
    palindrome = []

    while i < len(a1) and j < len(a1): 
        if a1[i] == a1[len(a1) - 1 - j]:
            palindrome.append(a1[i])
            i += 1
            j += 1
        elif dinprog[i + 1][j] >= dinprog[i][j + 1]:
            i += 1
        else:
            j += 1

    full_palindrome = ''.join(palindrome)

    return full_palindrome


dinprog = LCS(a1, a2)
length = dinprog[0][0]

palindrom = find_palindrome(a1, dinprog)

with open('output.txt', 'w') as output:
    output.write(str(length) + '\n') 
    output.write(palindrom)
