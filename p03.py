N = int(input())
P = list(map(int, input().split()))

P.sort()
DP = [0] * (N+1)
sumV = 0
for i in range(N):
    DP[i+1] = DP[i] + P[i]
    sumV += DP[i+1]
    
print(sumV)