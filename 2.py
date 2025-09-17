s = input("enter a string:")
if len(s) < 3:
    print(s)
else:
    swapped = s[-1] + s[1:-1] + s[0]
    print ("result: ", swapped)
