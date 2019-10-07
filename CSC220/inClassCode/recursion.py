def recur(n):
     if(n==0):
          return 0
     print n
     return n*recur(n-1)

print recur(-1)
