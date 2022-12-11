mantra = """Always look
... on the bright
... side of life."""

print(mantra)
path = r'C:\new\text.dat'
print(path)
concatination = 'abc'+'def'
print (concatination)
sample = 'Ra'*4
print(sample)
print('-'*40)

s= 'hacker'
for c in s: print(c, end=' ')

S = 'abcdefghijklmnop'
print(S[1:10:2]) #bdfhhj
print(S[::2]) #acegikmo
S="hello"
print(S[::-1]) #reverse string o/p 'olleh'
S = 'abcedfg'
S=S[5:1:-1] #fdec
print(S)

print('spam'[slice(1,3)]) #pa
print('spam'[slice(None,None,-1)])#maps

''' to print arguments passed for the script 
# File echo.py
import sys
print(sys.argv)
% python echo.py −a −b −c
['echo.py', '−a', '−b', '−c']'''

#----------------------------
f=46.89
print(f)
s=str(f)
print(s)
i=int(f)
print(i)
f=float(f)
print(f)
l=ord("s")
print(l)
print(chr(l))
#-------------------------------------
b=int('1011',2)
print(b)
print(bin(b))
#-------------

s="ramaLaxmi"
S=s.replace('rama','rajya')
print(S)
s="ababababbb"
S=s.replace("b","c",4) #acacacacbb
print(S)
fi= s.find('b')
print(fi)

S = 'spammy'
L = list(S)
L[3] = 'x' # Works for lists, not strings
L[4] = 'x'
S = ''.join(L)

st='That is %d %s bird!' % (1, 'dead') #That is 1 dead bird!
print(st)
st='That is {0} {1} bird!'.format(1, 'dead') # 'That is 1 dead bird!'
print(st)

print('%d %s %g you' % (1, 'spam', 4.0) )# Type-specific substitutions '1 spam 4 you'

x = 1.23456789
print( '%e | %f | %g' % (x, x, x))#'1.234568e+00 | 1.234568 | 1.23457'

x = 1234
print('integers: ...%d...%6d...%06d' % (x, x, x))#'integers: ...1234...1234 ...001234

food = 'spam'
qty = 10
print(vars()) #{ ...plus built-in names set by Python...'food': 'spam', 'qty': 10 }

print('%x, %o' % (255, 255))# hexa and oct 'ff, 377'