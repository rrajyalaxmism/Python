d={'spam':1,'happy':2,'maps':3}
print(d['spam'])
print(d)
print(len(d))
print('maps'in d)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
d['maps']=[4,5,6]
print(d)
del d['spam']
print(d)
d['test']='tset'
print(d)
print(d.get("maps"))
d2={1:"one",2:"two"}
d.update(d2)
print(d)
print(d.get("map",0))
print(d.pop("test"))
print(d)
table = {'Move 1': 1975,'Movie 2': 1979,'Movie 3': 1983}

res=[title for (title,year) in table.items() if year==1983]
print(res)
res=[key for key in table.keys() if table[key]==1983]
print(res)

mat={}
mat[(2,4,6)]=66
mat[(1,3,5)]=99
x=1;y=3;z=5
print(mat[(x,y,z)])

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {c: c * 4 for c in 'SPAM'}
print(D)

D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)

D = dict.fromkeys('spam')
print(D)

print(D.keys() & {'a'}) #intersection
print(D.keys()|{'i':0}) #union

#-------Sorted
D= {1:'a',2:'b',4:'d',3:'c'}
for k in sorted(D) : print(k,D[k])

#--------- to find if key, values exits

if 2 in D: print('present', D[2])
if D.get(3) != None: print('present', D[3])