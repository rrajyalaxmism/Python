D={'food':'Noodles','quantity':2, 'color':'pink'}
print(D)
print(D['food'])
D['test']='value'
print(D)
d= dict(name='Bob', job='New',age=40)
print(d)
d1=dict(zip(['name','job','age'],['Bob','New',40]))
print(d1)
############# nested ###############3
rec={'name':{'first':'Bob','last':'Smith'},
     'job':['dev','Mgr'],
     'age':40
}
print(rec['name'])
print(rec['job'][-1])
rec['job'].append('CSR')
print(rec)

######## sorting a dict ####
## type 1
d={'a':1,'b':2,'c':3}
l= list(d.keys())
l.sort()
for k in l:
    print(k ,'=>',d[k])
##type 2 (in built fun)

for key in sorted(d):
    print(key,'=>',d[key])

