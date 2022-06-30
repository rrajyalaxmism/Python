T=(1,2,3,4,4)
print (T[0])
print (len(T))
print(T+(5,6))
print(T)
print(T.index(4))
print(T.count(4))
T=(2,)+T[1:] # we can overwrite a tuple
print(T)
#Tuple are immutable
# Tuple cannot be changed, append method doesnot exists