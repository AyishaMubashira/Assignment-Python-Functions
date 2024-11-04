
#Exercise1
# What does the len() function do in Python? Write a code example using len() to find the length of a list.
# The len() Function returns the number of elements in an object (e.g., List,Tuple,String,Dictionary).
#Create a list
# Numbers = [1,2,3,4,5]
#Find the length of the list
# print("Length of list:", len(Numbers))


#Exercise2
# Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".
# def greet(Name):
#     print("Hello," + Name + "!" )
#Test the function
# greet("John")



#Exercise3
# Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without
# using the built-in max() function. Use a loop to iterate through the list and compare values.
# def Find_Maximum(numbers):
#     max_value = numbers[0]
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#     return max_value

# numbers = [12,25,9,30,45,19]
# print("Maximum Value:" , Find_Maximum(numbers))



#Exercise4
# Explain the difference between local and global variables in a Python function. Write a program where a
# global variable and a local variable have the same name and show how Python differentiates between them.
#In python:
#Local Variables - Defined Inside a function and accessible only within that function
#Global Variables - Defined outside functions and accessible from any function

#Global Variable
# x=30
# def test():
#     x=20
#     print("Local x:",x)

# test()
# print("Global x:",x)




#Exercise5
# Create a function calculate_area(length, width=5) that calculates the area of a rectangle. If only the length
# is provided, the function should assume the width is 5. Show how the function behaves when called with and without the width argument.
def calculate_area(length,width=5):
    area = length * width
    return length * width

#Test with only length
print("Area(default width):", calculate_area(20))

#Test with length and width
print("Area(Custom width):", calculate_area(30))
