width = int(input("Number one: "))
height = int(input("Number two: "))

max_domin: int  # 0 if the input out of 1 ≤ M ≤ N ≤ 16 rule
if 1 <= width <= height <= 16:
    if (width % 2 == 0 or (width % 2 == 0 and height % 2 == 0)):
        max_domin = (width*height)//2
        print(max_domin)
    elif width % 2 != 0 and height % 2 != 0:
        max_domin = (width*height)//2
        print(max_domin)
else:
    print("Invalid input")
