## simple function
def even_odd(x):
       if x % 2 ==0:
          print('EVEN')
       else:
        print("ODD")
even_odd(int(input("enter your number:")))

#add function
def sum(a,b):  #here a and b are parameters
    print(a+b)
sum(3,5) #here 3 and 5 are arguments

#FUNCTION WITH RETURN

def sum(a,b): 
    return(a+b) #code distructor
print(sum(3,5)) 


#TYPES OF ARGUMENTS
# DEFUALT ARGUMENTS
def sum(a,b=3): 
    return(a+b) 
print(sum(3)) 


#positional arguments
def sum(a,b): 
    print("a",a)
    print("b",b)

sum(4,3)

#keword argument
def sum(a,b): 
    return a+b

print(sum(a=3,b=8))

# variable lenght arguments
def vari(*a):
    return a
print(vari(2,3,5,6,7)) # return tuple

def vari(**a):
    return a
print(vari(a= 1, b= 2,c= 3))# return a dictionary


# #PARACTICE
my_str = str(input("enter your data:"))
r = my_str[::-1]
def reverse_str():
    return r
print(reverse_str())


# finding vowels

def find_vowels(user_input):
    vowels = "aeiouAEIOU"  
    found_vowels = []      
    
    for char in user_input:
        if char in vowels:
            found_vowels.append(char)
    
    return found_vowels


user_input = input("Enter a string: ")
vowels_in_input = find_vowels(user_input)

print("Vowels in the input string:", vowels_in_input)

