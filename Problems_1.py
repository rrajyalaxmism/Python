'''in a given string say"ababababbb" find the number repeated
chars of the entered string "ab" '''

mainstr=input("Enter a string ")
findchar= input("Enter the char to find number of times repeated ")

num= mainstr.split(findchar)

print(len(num)-1)

#find the index of all the repeated of the entered string in the main string
index=[]
k=0
while k < len(mainstr):
    i = mainstr.find(findchar, k)
    if i==-1:
        break
    index.append(i)
    k=k+len(findchar)
temp=[]
for a in index:
    if a not in temp:
        temp.append(a)

print(temp)




