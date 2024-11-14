def fact (n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=int(input("enter n number of term"))
term=1
s=0
for i in range (1,n+1):
    s+=fact(term)
    term+=2
print(s)        