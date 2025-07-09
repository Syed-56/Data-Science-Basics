x=10
if x>10:
    print("Bigger Than 10")
elif x<10:
    print("Less than 10")
else:
    print("Equal to 10")
#also && operator is written as and, || operator as or and ! operator as not.

result = "Even" if x%2==0 else "Odd"
print(result)

day = "Monday"
match day:
    case "Monday":
        print("Boring")
    case "Friday":
        print("Almost There")
    case _:
        print("Weekend")
