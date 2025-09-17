list1 = input("enter colors for list1: ").split()
list2 = input("enter colors for list2: ").split()
unique_colors = [color for color in list1 if color not in list2]
print(unique_colors)
