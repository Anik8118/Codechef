# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    if 'I' in s:
        print("INDIAN")
    elif 'Y' in s:
        print('NOT INDIAN')
    else:
        print('NOT SURE')