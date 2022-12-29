# Function composition
def square(num):
    return num**2
def double(num):
    return num*2
num=int(input("enter a no: "))
print(square(double(num)))