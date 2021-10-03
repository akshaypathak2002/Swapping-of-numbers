# In this we will see how to do swapping of two numbers
#here we are doing swapping of two numbers by using bitwise ^XOR
a = 3
b = 5
print("a= ", a, " b= ", b)
a ^= b 
b ^= a
a ^= b
print("a= ", a, " b = ", b)
