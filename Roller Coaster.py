t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    if a>=b:
        print("YES")
    else:
        print("NO")