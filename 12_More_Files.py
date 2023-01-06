mf= open("12_More_Files.txt",'w')
mf.write("new text entered\n")
mf.write("Next line in file.\n")
mf.close()

X,Y,Z= 10,11,12
S='Something'
D={1:'a',26:'z'}
L=[100,200,300]

F= open("12_More_Files.txt",'w')
F.write(S+'\n')
F.write('%s,%s,%s\n'%(X,Y,Z))
F.write(str(L)+"&"+ str(D)+'\n')
F.close()
print(open('12_More_Files.txt').read())
k=open('12_More_Files.txt')
print(k.readline().rstrip())
k.readline()
dpart=k.readline().split('&')
print(dpart)
obj=[eval(o) for o in dpart] # converts each string to an object
print(obj)

########## Pickle (serialize)

dt={'a':1,'z':26}
Fl= open('12_datafile.pkl','wb')
import pickle
pickle.dump(dt,Fl) #serialize
Fl.close()
Fl = open('12_datafile.pkl','rb')
ld= pickle.load(Fl) #deserialize
print(ld)

##############Json operations in files

n= dict(first='Rajyalaxmi', last='Viswanadha')
rec= dict(name=n, job=['SSM','SSA'], age=27)
print(rec)

import json
m=json.dumps(rec)
print(m)
o=json.loads(m)
print(m==rec)
print(o==rec)

json.dump(rec,fp=open('jsontext.txt','w'),indent=5)
print(open('jsontext.txt').read())
p= json.load(fp=open('jsontext.txt'))
print(p)

# file using context manager
with open('jsontext.txt','r') as f:
    for line in f:
        print(line)

#another way to conext manager code
f= open('jsontext.txt')
try:
    for li in f:
        print(li)
finally:
    f.close()