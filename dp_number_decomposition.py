def find_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def min_factors(a, b, c):
    # Находим все делители a
    divisors = find_divisors(a)
    
    # Фильтруем делители по диапазону [b, c]
    valid_divisors = [d for d in divisors if b <= d <= c]
    
    if not valid_divisors:
        return -1
    
    # Инициализируем множество для произведений
    current_products = set(valid_divisors)
    previous_products = set()
    count = 1  # Номер сета
    
    while current_products:
        if a in current_products:
            return count
        
        # Генерируем новые произведения из текущих
        previous_products = current_products.copy()
        new_products = set()
        
        for x in previous_products:
            for y in valid_divisors:
                product = x * y
                if product <= a:
                    new_products.add(product)
        
        current_products = new_products
        count += 1
        
    return -1


with open('input.txt', 'r') as input:
    a, b, c = map(int, input.readline().strip().split())

result = min_factors(a, b, c)

with open('output.txt', 'w') as output:
    output.write(str(result) + '\n')
