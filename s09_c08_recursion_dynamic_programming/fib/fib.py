def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_dp_helper(n, mem):
    if n == 0 or n == 1:
        return 1
    else:
        try:
            return mem[n]
        except IndexError:
            mem[n] = fib_dp_helper(n - 1, mem) + fib_dp_helper(n - 2, mem)
        return mem[n]


def fib_dp(n):
    l = [None] * n+1
    return fib_dp_helper(n, l)


for i in range(0, 35):
    print fib_dp(i)


for i in range(0, 35):
    print fib(i)
