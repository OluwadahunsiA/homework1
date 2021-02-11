def fact(n):
    ls = []
    start = 1
    for v in range(1, n+1):
        start *= v
        ls.append(start)
    for entry in ls:
        yield(entry)


count = 1
for i in fact(20):
    print(f'{count}! = {i}')
    count += 1
