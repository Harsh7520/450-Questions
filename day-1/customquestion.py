n = int(input())
a = list(map(int,input().split()))
b = a.copy()
ans = []
for i in range(n):
    if(a[i]<0):
        ans.append(a[i])
        b.remove(a[i])
ans.extend(b)
print(*ans)
