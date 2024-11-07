# #  creating error
x = 3
y = "h"
print(x+y)

# solution
x = 5 
y = 'gfg'
try:
    print(x+y)
except:
    print("i found an error")
    
print("i am learning python")

# for caughting exact error
# solution
x = 5 
y = 'gfg'
try:
    print(x+y)
except  TypeError as e:
    print(e)
    
print("i am learning python")

# zerodivision error
y = 5
x = 0
try:
    print(y/x)
except ZeroDivisionError as d:
    print(d)

print("i am learning python")

# with double except
y = 5
x = 0
try:
    print(y/x)
except ZeroDivisionError as d:
    print(d)
except TypeError as e:
    print(e)
    
    
print("i am learning python")

# adding else
y = 5
x = 10
try:
    print(y/x)
except ZeroDivisionError as d:
    print(d)
except TypeError as e:
    print(e)
else:
    print("there found no error")
    
    
print("i am learning python")


# adding finally
y = 5
x = 0
try:
    print(y/x)
except ZeroDivisionError as d:
    print(d)
except TypeError as e:
    print(e)
finally:
    print("i dont depend on both")    # this will always exicute
print("i am learning python")

#  if no error present
y = 5
x = 10
try:
    print(y/x)
except ZeroDivisionError as d:
    print(d)
except TypeError as e:
    print(e)
finally:
    print("i dont depend on both")    # this will always exicute
print("i am learning python")

# SyntaxError

try:
    var = 'my name
except SyntaxError as e:
   print(e)
   
print("i am learning python") #not aught it directly

try:
    exec("x === 5")
except SyntaxError as d:
    print(d) # using this syntax error can be caught


#  learnig ezception
x = 5 
y = 'gfg'
try:
    print(x+y)
except Exception as e:# it will caught any type of error
    
#     print(e)

# raise error
user_input = int(input("enter your age:"))
print(type(user_input))
if type(user_input) == str:
    raise("this is not a valid input")


# FILE HANDLING
# opening in read mood
f = open("file.txt",'r')
con = f.read()
print(con)
f.close()

# opening in writing mod

f = open("file.txt",'w')
f.write("this is my data")
f.close()

f = open("file.txt",'r')
con = f.read()
print(con)
f.close()

#  creating filw through write mod

f = open("file.txt2",'w')
f.write("i am nwe file")
f.close()

# work with a

f = open("file.txt2",'a')
f.write("i created new data")
f.close()


f = open("file.txt",'r+')
f.write("i created new data of r+")
f.seek(0)
con = f.read()
print(con)
f.close()

# changing seek

f = open("file.txt",'r+')
f.write("i created new data of r+")
f.seek(1)
con = f.read()
print(con)
f.close()
 
#  working with w+

f = open("file.txt",'w+')
f.write("i add new line")
f.seek(0)
con = f.read()
print(con)
f.close()


#   working with WITH
with open("file.txt2",'r') as r:
    con = r.read()
    print(con)
