#str= input("enter string: ") #enter string:  raMa Rajya laxmi
str = " raMa Rajya laxmi "
print("Title : "+str.title())#Title :  Rama Rajya Laxmi
print("Upper : "+str.upper())#Upper :  RAMA RAJYA LAXMI
print("Lower : "+str.lower())#Lower :  rama rajya laxmi
print("Strip : "+str.strip())#Strip : raMa Rajya laxmi
print(str.__contains__("laxmi"))
#_____________________
first_name = "Rama"
last_name = "Rajyalaxmi"
full_name = f"Full name is: {first_name} {last_name}"
#print(full_name)
print(first_name.__add__(" * ").__add__(last_name))
#################

message = "One of Python's strengths is its diverse community."
print(message)

r=reversed(message) # returns a list object
print("".join(list(r)))

#########################
S="A\nB\tC"
print(S)
print(len(S))
print(ord("\n")) #prints ASCII value of \n
S="A\0B\0C"
print(len(S))
print(S)
msg="""
I can type 
The way i want.
What you see is what you get.
"""
print(msg)