colors = input("enter colors separated by commas: ")
color_list = [color.strip() for color in colors.split(",")]
print("list of colors:",color_list)
if color_list:
    print("first color:",color_list[0])
    print("last color:",color_list[-1])
else:
    print("no colors")
