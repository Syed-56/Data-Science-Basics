try:
    x=10/0
except ZeroDivisionError:
    print("Cant Divide by Zero")

try:
    x=10/0
except (ZeroDivisionError, ValueError): #error with parameter
    print("Division or Value error occured")

try:
    x = 10/0
except Exception as e:  # all error
    print("Error 404 : {e}")

try:
    x=10/5
except ZeroDivisionError:
    print("Cant Divide by Zero")
else:
    print("Division Successful: ", x)

x=1
if x==0:   
    raise ZeroDivisionError("Cant Divide by 0 (custom)")    #this raises actual compiler error
else:
    print(x)

while True:
    try:
        num = int(input("Enter Number to divide with 10 = "))
        result = 10/num
        print("result = ", result)
        break
    except ZeroDivisionError:
        print("Cant Divide with 0")
    except ValueError:
        print("Enter Value")