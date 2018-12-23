T = int(input())                  

N = []
S = []
for i in range(0,T):   
    N.append(int(input()))
    S.append(input())
    
for i in range(0,T):
    s = S[i]    
    n = N[i]
    found = False
    for clen in range(n,-1,-1):
        if(found):
            break
        for strt in range(0,n-clen):
            end = clen+strt
            sub = s[strt:end+1]
