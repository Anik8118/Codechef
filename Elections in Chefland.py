# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        if a>50:
            print("A")
        else:
            print("NOTA")
    elif b>a and b>c:
        if b>50:
            print("B")
        else:
            print("NOTA")   
    elif c>b and c>a:
        if c>50:
            print("C")
        else:
            print("NOTA")        
    elif a==b:
        if c<50:
            print("NOTA")
    elif a==c:
        if b<50:
            print("NOTA")
    elif c==b:
        if a<50:
            print("NOTA")            
        