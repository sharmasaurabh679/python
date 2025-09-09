# ask user for name 
name = input("what your name !!")
print("hello," , name)
print ("hello" ,name, sep="&&&")
print ("hello",name, end="**") 
print(f"hello ,{name}") # newly added format string or f string
print('hello ,"friend"') # can use single or double quotes
print("hello \"friend\"") # this back shash called esc char that print literal

x= input("hi")
# remove white space from string
x= x.strip()

# capitalze users name frist letter only
x=x.capitalize()

# capitalze users name  all frist 
x=x.title()

print(f'hello,{x}')

# make it better and small
# chain two print method




# make it more small 
# add to the input

userid= input('what your name').strip().title()
# user name spit into two parts frist and last
frist, last = userid .split(" ")
print(f"hello,{frist}") # we writ here frist because we only need uesr frist name only




print('hello')