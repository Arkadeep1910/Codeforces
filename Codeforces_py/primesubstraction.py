t=int(input())
while(t):
    x,y=map(int,input().split())
    diff=x-y
    if(diff>1):
        print("YES")
    else:
        print("NO")
    t-=1