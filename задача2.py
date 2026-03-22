def fibonacci(n, first=0, second=1):
    if n == 0:
        return first
    if n == 1:
        return second
#первые два элемента
    prev2 = first
    prev1 = second
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1
print(fibonacci(10))
print(fibonacci(5))
print(fibonacci(0))        
print(fibonacci(1))
