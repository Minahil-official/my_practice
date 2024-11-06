# # WITH VARIABLE

# name = "nawaz"
# for i in name:
#     print(i)
#     # or 

# # WITH DIRECT METHOD

# for i in "nawaz":
#  print(i)

# # With range

# for i in range(0,11):
#     print(i)

# # #WITH STEPPING

# for x in range(0,101,5):
#     print(x)

# # eENUMIRATE FUNCTION IN LOOP

# name = "piaic student"
# for char,index in enumerate(name):
#     print(index,':',char)

# #JUST INDEX
# name = "piaic student"
# for index,char in enumerate(name):
#     print(index)

    
# num ="44567892"
# for id,chr in enumerate(num):
#     print(id,chr)

# #NESTED FOR LOOP
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)


# # CONTROLL STATEMENTS
# # CONTINUE

# for i in range(0,15):
#     if i == 9:
#         continue
#     print(i)
    
    
# #BREAK
# for i in range(0,10):
#     if i == 2:
#         break
#     print(i)



# for i in range(0,10):
#     if i == 2:
#         pass
#     print(i)


# ## WHILE LOOP

# count = 0
# while (count<5):
#     print("I am while loop")
#     count = count + 1
  
  
# count = 0
# while (count<5):
#     print("I am while loop")
#     count = count + 1
#     if count == 2:  
#        continue  
    
# count = 0
# while (count<5):
#     print("I am while loop")
#     count = count + 1
#     if count == 2:  
#        break 

# count = 0
# while (count<5):
#     print("I am while loop")
#     count = count + 1
#     if count == 2:  
#        pass


# # PRACTICE
# num = int(input("enter what table you want:"))
# for i in range(1,11):
#     total = num*i
#     print(num ,"x","=",total)

# # print***

# for i in range(0,4):
#     print("****")

# # fizzbuzz

# for i in range(101):
#     if i%3 ==0:
#         print('FIZZ')
#     if i%5 == 0:
#         print("BUZZ")
#     if i%3 and i%5 == 0:
#         print("fizzbuzz")
#     else:
#         print(i)