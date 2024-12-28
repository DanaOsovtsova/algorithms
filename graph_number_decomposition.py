from collections import deque
#как задача по нахождению кратчайшего пути в ориентированном графе, где узлы представляют множители
def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def min_factors(a, b, c):
    divisors = find_divisors(a)

    valid_divisors = sorted(d for d in divisors if b <= d <= c)
    
    if not valid_divisors:
        return -1
    
    queue = deque([(1, 0)])  # (текущий произведение, количество множителей)
    visited = set() 
    
    while queue:
        current_product, count = queue.popleft()

        for d in valid_divisors:
            new_product = current_product * d

            if new_product > a:
                break

            if new_product == a:
                return count + 1

            if new_product not in visited:
                visited.add(new_product)
                queue.append((new_product, count + 1))
    
    return -1

with open('input.txt', 'r') as input:
    a, b, c = map(int, input.readline().strip().split())

result = min_factors(a, b, c)

with open('output.txt', 'w') as output:
    output.write(str(result) + '\n')
