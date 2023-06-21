T= ('Value1',('NV1','NV2')) #nested tuples
t= tuple('spam')
print(t)
print(T[1][0])
print(len(T))
tt= T+t
print(tt)
print(t*3)

##########Sorting
#convert the tuple to list , use sort method and reconvert the resulting list to a tuple

ll= list(t)
ll.sort()
t=tuple(ll)
print(t)

# alternate method to be sed is sorted method on the tuple
t1=(1,3,6,4,8.2,9)
print(sorted(t1))
#------------------------------
t2=(1,2,3,4,5,2,4,2)
print(t2.index(2))
print(t2.index(4,4))
print(t2.count(4))

#--------------------

tx= (1,[2,3],4)
tx[1][0]=5 # tx[0]=5 is not possible

############ Named tuples
from collections import namedtuple

rec= namedtuple('rec',['name', 'age', 'jobs'])
b= rec('SR',age=40, jobs=['SM','SSM'])
print(b)
print(b.name)
print(b[0])
