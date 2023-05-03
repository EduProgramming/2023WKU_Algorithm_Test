N, M = map(int, input().split())
result = (M * (M+1) // 2) - ((N-1) * N // 2)
print(result)