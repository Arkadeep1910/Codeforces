t=int(input())
while(t):
    n,k=map(int,input().split())
    a=n//k
    s=a*k
    m=min(n%k,k//2)
    ans=s+m
    print(ans)
    t-=1
