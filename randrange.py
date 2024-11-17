import random as r
s=0
begin=r.randint(1,3)
for i in range (3):
    s+=begin
    begin+=r.randrange(3)
print(s)    