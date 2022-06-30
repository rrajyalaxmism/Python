######### file write##########
f=open('06_files.txt','w')#creates a new file if doesnt exists
f.write('Hello\n')
f.write('world\n')
f.close()
print('Write Done')
########## file read ##########
f=open('06_files.txt')# default is to read attibute ,'r'
text =f.read()
print(text) #file content is always a string
print('read done')

for line in open('06_files.txt') :print(line)