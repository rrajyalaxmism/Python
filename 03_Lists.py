########### Sequence operations############
print("########### Sequence operations############")
l= [123,"py",6.10]
print("l")
print(l)
print("len(l)")
print(len(l))
print("l[0]")
print(l[0])
print("l[:-1]")
print(l[:-1])
print("l+[4,5,6]")
print(l+[4,5,6])
print("l*2")
print(l*2)
print("l")
print(l)
#################### type specific operations ############
print("#################### type specific operations ############")
print('l.append("Rajis")')
print(l.append("Rajis"))
print("l.pop(2)")
print(l.pop(2))
print(l)
print("l.insert(2,20)")
print(l.insert(2,20))
print(l)
print("l.remove(123)")
print(l.remove(123))
print("l.extend([0,9,8])")
print(l.extend([0,9,8]))
print(l)
print("k.sort()")
k=[4,6,3,6,2,6]
print(k.sort())
print(k)
k.remove(6)
k.append(4)
print(k)
k.remove(4)
print(k)
print("l.reverse()")
print(l.reverse())
print(l)
######################## Nested ###################
print("######################## Nested ###################")
M=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print("M[1][1]")
print(M[1][1])
######################## Comprehensions ################
print("######################## Comprehensions ################")
#“Give me row[1] for each row in matrix M, in a new list.”
col2= [row[1] for row in M] # similar to , for row in M : print row[1]
print(col2)
### more
q=[row[1]+1 for row in M]
print(q)
'''
this is similar to 
for row in M:
   print row[1]+1
'''
q=[row[1] for row in M if row[1]%2==0]
print(q)
'''
for row in M:
   if row[1]%2==0:
      print row[1]
'''
dia= [M[i][i] for i in [0,1,2]]
print(M)
print(dia)
'''
for i in [0,1,2]
   print M[i][i]
'''
print("list(range(4))")
print(list(range(4)))
print("list(range(−6, 7, 2))")
a= [list(range(-6, 7, 2))]
print(a)
print("[[x, x / 2, x * 2] for x in range(−6, 7, 2) if x > 0]")
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
###################### advance topics ###############
print(" creation generator")
G=(sum(row) for row in M)
print(next(G))
print(next(G))
print("list(map(sum, M))")
print(list(map(sum, M))) # similar to above output but at once
print("comprehension in sets")
print({sum(row) for row in M})
print({i : sum(M[i]) for i in range(3)} )

[ord(x) for x in 'spaam'] #lists
{ord(x) for x in 'spaam'} # Sets
{x: ord(x) for x in 'spaam'} # dictionary
(ord(x) for x in 'spaam') # generator




