# age = 45 # an integer asignment
# salary = 51456.6 # a float point
# name = "Ankush" #a string
# print("Hello my name is : ",name)
# print("My age is:",age ,"and salary is:",salary)





# def myFun(x):

#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = 20
#     return x


# # Driver Code (Note that x is not modified
# # after function call.
# x = 10
# x=myFun(x)
# print(x)




def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y

# Driver code
x = 2
y = 3
temp = x
x = y
y = temp
# x,y=swap(x, y)
print("the value of x is %d" % x)
print("the value of y is %d" % y)