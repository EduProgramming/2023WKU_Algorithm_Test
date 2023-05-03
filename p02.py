def combi(r, start, visit):
    if r == 0:
        total = allV
        for i in range(N):
            if visit[i]:
                total -= people[i]
        if total == 100:
            idx = 0
            for i in range(N):
                if not visit[i]:
                    dwarf[idx] = people[i]
                    idx += 1
        return
    
    for i in range(start, N):
        visit[i] = True
        combi(r-1, start+1, visit)
        visit[i] = False

N = 9
R = 7

people = [0] * N
visited = [False] * N
dwarf = [0] * R
allV = 0

for i in range(N):
    people[i] = int(input())
    allV += people[i]

combi(N-R, 0, visited)
dwarf.sort()

for i in range(R):
    print(dwarf[i])