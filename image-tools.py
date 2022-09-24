from fileinput import filename
import os
from turtle import left
from PIL import Image


def program():
    print("Dragon Image Editor")
    for x in range(1, 20):
        print("-", end="")
    print("\n#1 Resizer")
    print("#2 Rotate")
    print("#3 Crop")
    print("#4 Exit")
    for x in range(1, 20):
        print("-", end="")
    choice = str(input("\nEnter Choice : "))

    if choice == str(1):
        x = int(input("Enter x dimensions in pixles : "))
        y = int(input("Enter y dimensions in pixels : "))
        new_im = img.resize((x, y))
        new_im.save(filename + "_resized" + seperator + extension)
        print("Operation Successful")
        new_im.show()

    elif choice == str(2):
        ro = int(input("Enter degrees to rotate : "))
        new_im = img.rotate(ro)
        new_im.save(filename + "_rotated" + seperator + extension)
        print("Operation Successful")
        new_im.show()

    elif choice == str(3):
        left = int(input("Enter left : "))
        top = int(input("Enter top : "))
        right = int(input("Enter right : "))
        bottom = int(input("Enter bottom : "))
        new_im = img.crop((left, top, right, bottom))
        new_im.save(filename + "_cropped" + seperator + extension)
        print("Operation Successful")
        new_im.show()

    elif choice == str(4):
        exit(0)

    else:
        print("Invalid Choice")


fn = input("Enter Filename : ")  # file shoud be in current directory
file_exists = os.path.exists(fn)
if file_exists:
    img = Image.open(fn)
    filename = img.filename
    filename, seperator, extension = filename.partition(".")
    os.system("cls")
    program()
else:
    print("No such file in directory")
