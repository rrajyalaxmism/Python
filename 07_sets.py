print(list(set([1,2,3,2,1,5])))#filtering duplicates
##################
X=set('Raji')
Y={'R','a','m','a'}

print(X,Y)
print(X&Y) #intersection
print(X|Y) #Union
print(X-Y) #difference
A={n**2 for n in [1,2,3,4]} #comprehension
print(A)