## simple function
# def even_odd(x):
#        if x % 2 ==0:
#           print('EVEN')
#        else:
#         print("ODD")
# even_odd(int(input("enter your number:")))

#add function
# def sum(a,b):  #here a and b are parameters
#     print(a+b)
# sum(3,5) #here 3 and 5 are arguments

#FUNCTION WITH RETURN

# def sum(a,b): 
#     return(a+b) #code distructor
# print(sum(3,5)) 


#TYPES OF ARGUMENTS
# DEFUALT ARGUMENTS
# def sum(a,b=3): 
#     return(a+b) 
# print(sum(3)) 


#positional arguments
# def 











# #PARACTICE
# my_str = str(input("enter your data:"))
# r = my_str[::-1]
# def reverse_str():
#     return r
# print(reverse_str())

my_str = str(input("enter your data:"))
def finding_vowel():
    vowels = "a,e,i,o,u"
    for i in vowels:
        if vowels == my_str:
            print(vowels)
        else:
            print("not correct")
finding_vowel()