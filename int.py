#add 
x=input("what's x" )
y=input("what,s y")
z= int(x)+int(y)
print(z)

#function nested and make  it small
a=int(input(" frist   number "))
b=int(input("second number "))
print(a+b)

# make it more short
# x=int(input("what's x" )) + y=int(input("what,s y")) # prone to mistake


# float 
x= float(input("what's x")) 
y= float(input("what,s y"))
print(x+y)

# round method in int fun
x= float(input("what's x")) 
y= float(input("what,s y"))
z = round(x+y) 
print(z)



# to add conna for reading easy
x= float(input("what's x")) 
y= float(input("what,s y"))
z = round(x+y)
print(f"{z:,}")

#div
x= float(input("what's x")) 
y= float(input("what,s y"))
z = round(x/y,2) #(x/y,2) this to ,mean round of to two digit
print(z)


x= float(input("what's x")) 
y= float(input("what,s y"))
z = round(x/y)
print(f"{z:.2f}")# do rround of f string to two digit


