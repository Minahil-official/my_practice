# CREATING A LIST
multiple = [1,3,4,'ali','world',True]
print(multiple)

#FINDING LENGTH
print(len(multiple))

# accessing specific element with indexing
print(multiple[3])
print(multiple[-2])
# accessing multiple elements with slicing
print(multiple[1:4])
print(multiple[1:5:2])

# slicing make no effect on parent
# it is shalow copy

li = multiple[1:4]
print(li)
print(multiple)


#FUNCTIONS OF LIST

#APPEND()

l1 = [1,2,3,4,5,'ali','hassen']
print(li.append('hashim'))

insert()

l1 = [1,2,3,4,5,'ali','hassen']
li.insert(1,'ahmed')
print(l1)

#EXREND()

l1 = [1,2,3,4,5,'ali','hassen']
l2 = [6,7,8]
li.extend(l2)
print(l1)

#pop()

l1 = [1,2,3,4,5,'ali','hassen']
l1.pop()
print(l1)
#by giving index
l1 = [1,2,3,4,5,'ali','hassen']
remove_element = l1.pop(2)
print(remove_element)
print(l1)

# REMOVE()

l1 = [1,2,3,4,5,'ali','hassen']
l1.remove(4) #it rem e the element not the index
print(l1)

# CLEAR()

l1 = [1,2,3,4,5,'ali','hassen']
l1.clear() 
print(l1)

# DELL
my_list = [5,7,9,2,'raffy']
del my_list[3]
print(my_list)

# COUNT()
my_list = [5,7,9,2,4,3,2,2,'raffy']
new_list = my_list.count(2)
print(new_list)

# COPY()
my_list = [5,7,9,2,4,3,2,2,'raffy']
new_list = my_list.copy()
print(new_list)

# SORT()
my_list = [5,7,9,2,4,3,2,2,8,9]
my_list.sort()
print(my_list)


# reversed()

my_list = [5,7,9,2,4,3,2,2,8,9]
my_list.reverse()
print(my_list)


# MAX,MIN,SUM
my_list = [5,7,9,2,4,3,2,2,8,9]
max = max(my_list)
min = min(my_list)
sum = sum(my_list)

print(max)
print(min)
print(sum)


#taking input in list

li= []
for i in range(0,3):
    num = int(input("enter your number:"))
    li.append(num)
    print(li)

# TUPLES
#creating tuple
tu = (1,2,3,'ali',3.4)
print(tu)


# print(tu.count(3))

# single item tuple
tu = ('ali',) # , is essential for single item tuple
print(type(tu))



# taking input

l1 = []
for i in range(0,3):
    num = int(input("enter your number:"))
    l1.append(num)
    tu = tuple(l1)
    print(tu)


# make changes to tuple

t2 = tuple(t1)
print(t2)
li = []
name =input("enter your name:")
age = int(input('enter your age:'))
edu = input('enter your edu:')
li.append(name)
li.append(age)
li.append(edu)
tu = tuple(li)
print(tu)
t1 = list(tu)
t1[0] = "nawaz"


# find highest number
li = [1,2,3,4,5,6,7,8,9,10]
h = 5
for i in range(h):
   y = max(li)
   z = li.index(y)
   del li[z]
print(y)
   