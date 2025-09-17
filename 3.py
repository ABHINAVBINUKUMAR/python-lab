s = input("Enter your string: ")
first = s[0]
s = first + s[1:].replace(first,'$')
print("result: ", s)