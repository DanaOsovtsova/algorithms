def hash_table(m, c, keys):
    t = [-1] * m
    
    for key in keys:
        i = 0
        while True:
            index = (key % m + c * i) % m
            if t[index] == -1:
                t[index] = key
                break
            elif t[index] == key:
                break
            i += 1

    return t

    
with open('input.txt', 'r') as input:
        m, c, n = map(int, input.readline().strip().split())
        keys = [int(input.readline().strip()) for _ in range(n)]
    
hash_t = hash_table(m, c, keys)
    
with open('output.txt', 'w') as output:
        output.write(' '.join(map(str, hash_t)) + '\n')
