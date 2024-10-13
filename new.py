f=open("pehla","a")
s="TOday is my first day in school 123"
f.write(s)
f.close()
f1=open("pehla","r")
d=f1.read()
l=d.split()
c=0
d=0
for i in l:
    if i=="in":
        c+=1
    if i=="my":
        d+=1
print (c)
print (d)
print (l)        