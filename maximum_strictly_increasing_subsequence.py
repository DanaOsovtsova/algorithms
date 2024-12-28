import bisect

with open('input.txt', 'r') as input: #прочитали
    n = int(input.readline().strip())
    a = list(map(int, input.readline().strip().split())) 

t = []

def maxIncreasedPosled(n, a):
    for num in a:
        pos = bisect.bisect_left(t, num)

        if pos == len(t):
            t.append(num)
        else:
            t[pos] = num

    return len(t)


result = maxIncreasedPosled(n, a)

with open('output.txt', 'w') as output:
    output.write(str(result))
