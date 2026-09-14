a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6

val = int(input("Enter a value: "))

match val:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case 6:
        print("Sunday")
    case _:
        print("ENTER FROM 0-6 cuz week has only 7 dayssss :)")