# Taking input and slicing,indexing
intro = ("my name is minahil nawaz and my age is 18 and my edu is fsc")
print(intro[11:24],end="")
print(intro[38:41],end= "")
print(intro[55::])
        ##OR
print(intro[11:24],intro[38:41],intro[38:41],)
#printing even numbers
num = ("12345678910")
print(num[1:10:2])
# changing str to list and making changing
name = 'minahil nawaz'
li = list(name)
print(list)
li.pop()
list1 = " ".join(li)
print(list1)
# working with conditional statements
marks = int(input('enter your marks:'))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("c")
elif marks >= 50:
    print("c+")
else:
    print('you are fail')
