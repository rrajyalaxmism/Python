############################### sequence ########################
s="Rama Rajyalaxmi Viswanadha"
print(s)
print("length "+str(len(s)))#26
print("s[0] "+s[0]) #R
print("s[-1] "+s[-1]) #a
print("s[len(s)-1] "+s[len(s)-1])#a
print("s[5:10] "+s[5:10]) #Rajya
print("s[5:] "+s[5:]) # Rajyalaxmi Viswanadha
print("s[:5] "+s[:5]) # Rama
print("s[:-1] "+s[:-1]) # Rama Rajyalaxmi Viswanadh
print("s[:] "+s[:]) # equal to s[0:len(s)] #### Rama Rajyalaxmi Viswanadha
#################Immutabillity (char replacement in a string)###################
print("#################Immutabillity (char replacement in a string)################### ")
s= 'r'+s[1:]
print(s)
l=list(s)
print(l)
l[0]='R'
s=''.join(l)
print(s)
st= b"rama rajyalaxmi viswanadha"
B=bytearray(st)
print(B)
B.extend(b' Meduri')
print(B)
print(B.decode())
##############################Type specific methods##################
print(s.find("V"))
print(s.replace("V","B"))
print(s)
print("my name is %s" %(s))
print("my name is {}".format(s))
##################################### UNICODE ####

print('sp\xc4m') #normal str is equal to unicode # spÄm
print(u'sp\u00c4m') #unicode rep # spÄm
print(b'a\x01c') #byte code rep # b'a\x01c'

print('spam'.encode('utf8') )# Encoded to 4 bytes in UTF-8 in files #b'spam'

print('spam'.encode('utf16')) # But encoded to 10 bytes in UTF-16 #b'\xff\xfes\x00p\x00a\x00m\x00'

#print(u'x' + b'y') # Works in 2.X (where b is optional and ignored) failed in 3.10
print(u'x' + 'y') # Works in 2.X: u'xy'
#print(u'x' + b'y') # Fails in 3.3 (where u is optional and ignored) #failed
print(u'x' + 'y') # Works in 3.3: 'xy'
print('x' + b'y'.decode()) # Works in 3.X if decode bytes to str: 'xy'
print('x'.encode() + b'y') # Works in 3.X if encode str to bytes: b'xy'

