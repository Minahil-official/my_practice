# ceating a dictionary
dict1 =  {1:'a',2:'b',3:'c',4:(1,2,3),5:{'d':[5,6,7]}}
print(dict1)

# accessing element
print(dict1[2])
print(dict1[4][1])
print(dict1[5]['d'][2])

# types of key

# alphabetic
dict12 = {'a':1,'b':2,'c':3}
print(dict12)

# numeric
dict1 =  {1:'a',2:'b',3:'c',4:(1,2,3),5:{'d':[5,6,7]}}
print(dict1)

# ways to create a dictionary
my_dict = {}
print(my_dict)

# with empty dictionary
dict2 = {}
dict2["a"] = 1
dict2['b'] = 2
dict2["c"] = 3
print(dict2)

# taking input
dict2 = {}
dict2["a"] = int(input("enter a num"))
dict2['b'] = 2
dict2["c"] = 3
print(dict2)

# from tuple
dic = dict([(1,'h'),(2,'h'),(3,'d')])
print(dic)

# # METHODS

my_dict = {"name": "Asadullah", "age": 21, "city": "Karachi"}

del my_dict["age"]
print(my_dict)


dic = dict([(1,'h'),(2,'h'),(3,'d')])
(dic.clear())
print(dic)

# fromkeys()

seq = (1,2,3)
print(dict.fromkeys(seq,True))

# .get()
dict12 = {'a':1,'b':2,'c':3}
print(dict12.get("d","notfound"))

# pop()
dict12 = {'a':1,'b':2,'c':3}
dict12.pop('c')
print(dict12) # without argument is will give error


# popitem()

dict12 = {'a':1,'b':2,'c':3}
dict12.popitem() # it will remove last key value

# print(dict12)
# update()

my_dict = {"name": "Asadullah", "age": 21}
my_dict.update({"age": 22, "city": "Karachi"})

print(my_dict)

# setdefualt()

my_dict = {"name": "Asadullah", "age": 21}
value = my_dict.setdefault("name", "Unknown")
print(value)          # Output: "Asadullah"
print(my_dict) 

# # if value not present

my_dict = {"name": "Asadullah", "age": 21}
value = my_dict.setdefault("city", "Karachi")
print(value)          # Output: "Karachi"
print(my_dict)

# key(),value(),item()

my_dict = {"name": "Asadullah", "age": 21}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


# arbitary arguments

def add(**a):
    return a
print(add(a= 2,b=4,c=6)) # will return a dict

 # changing a list to dict
dic = {}
li = [1,2,3,4,5,6,7]
for x,y in enumerate(li):
    dic[x] = y
    
print(dic)