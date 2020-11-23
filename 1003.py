def count_fibonacci(n):
    zero_count = [1, 0]
    one_count = [0, 1]
    if n <= 1:
        return

    for i in range(2, n + 1):
        zero_count.append(zero_count[i - 1] + zero_count[i - 2])
        one_count.append(one_count[i - 1] + one_count[i - 2])

    return zero_count, one_count


n = int(input())
zero_count, one_count = count_fibonacci(40)

for _ in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))