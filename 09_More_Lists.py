#basic
print(len([1,2,3,4]))
print([1,2,3]+[4,5,6])
print(['NI']*4)

print(str([1,2])+'34')
print([1,2]+list("34"))

#List comprehensions-------------
r=[c*4 for c in 'SpAm']
print(r)

print(list(map(abs,[-1,-2,0,1,2])))

#----------Slicing -------------

l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[2])
print(l[-2])
print(l[1:])
print(l[1][2])

#---------few inbuilt functions----------
L=['eat','more','eggs']
L[1:3]=['less','carbs']
print(L)
L.append(':)')
print(L)
L.sort()
print(L)
Li=[1,2,3,4]
Li[len(Li):]=[5,6,7]
print(Li)
Li.extend([8,9,10])
print(Li)

LS=['abc','ABC','Xyz','xYZ']
LS.sort(key=str.lower,reverse=True)
print(LS)
LS=['abc','ABC','Xyz','xYZ']
print(sorted(LS,key=str.lower,reverse=True))
print(sorted([x.lower() for x in LS],reverse=True))

Li.reverse()
print(Li)
print(reversed(Li))
print(list(reversed(Li)))

L = ['spam', 'eggs', 'ham', 'toast']
del L[0] # Delete one item
print(L)#['eggs', 'ham', 'toast']
del L[1:] # Delete an entire section
print(L) # Same as L[1:] = [] #['eggs']

L = ['Already', 'got', 'one']
L[1:] = []
print(L)#['Already']
L[0] = []
print(L)#[[]]

L= ["Spam","spam","SPAM"]
L.insert(1,L) # ['Spam', [...], 'spam', 'SPAM', 4, 5, 6, 7] recursive structure or a circular reference within the list.

#-----------------
L=["Spam",90]
L.insert(1,L)
print(L)
print(L.index([...])) # throws an  ValueError: [Ellipsis] is not in list
#-------------

L=["Spam","90"]
k=L.copy()
print(k)
k.append(20)
print(L)
print(k)
k.clear()
print(k)
