T = int(input())                  
N = []
S = []

for i in range(0,T):   
    N.append(int(input()))
    S.append(input())
    
for i in range(0,T):
    s = S[i]    
    n = N[i]
    for clen in range(n,-1,-1):
        for start in range(0,n-clen+1):
            end = start+clen
            sub = s[strt:end]
