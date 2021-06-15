from tkinter import *
import math
import time

SIZE = 600


def devise_rectangle(img):
    print("Choose the coordinates of two opposite corners in your rectangle:")
    a = [(int(input("x1="))), (int(input("y1=")))]
    b = [(int(input("x2="))), (int(input("y2=")))]
    color = input("What color is you rectangle?\n")
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            img.put(color, (x, y))


def triangle_area(a, b, c):
    area = abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)
    return area


def devise_triangle(img):
    print("Choose the coordinates of the corners in your triangle:")
    a = [(int(input("x1="))), (int(input("y1=")))]
    b = [(int(input("x2="))), (int(input("y2=")))]
    c = [(int(input("x3="))), (int(input("y3=")))]
    color = input("What color is you triangle?\n")
    area_of_triangle = triangle_area(a, b, c)
    for x in range(SIZE):
        for y in range(SIZE):
            test_coordinate = [x, y]
            if (triangle_area(a, b, test_coordinate)
                    + triangle_area(a, test_coordinate, c)
                    + triangle_area(test_coordinate, b, c)
                    == area_of_triangle):
                img.put(color, (x, y))


def devise_circle(img):
    print("Choose the center coordinates of your circle:")
    center = [(int(input("x="))), (int(input("y=")))]
    radius = (int(input("Choose the radius of your circle:\n")))
    color = input("What color is you circle?\n")
    for y in range(SIZE):
        for x in range(SIZE):
            if math.sqrt(((center[0] - x) ** 2) + ((center[1]) - y) ** 2) <= radius:
                img.put(color, (x, y))


def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    menu = {"1": (lambda: devise_rectangle(img)),
            "2": (lambda: devise_triangle(img)),
            "3": (lambda: devise_circle(img))}
    while True:
        print("(1.)Rectangle\n(2.)Triangle\n(3.)Circle\n(4.)Quit")
        choice = input("With this program you can create these shapes on a 600x600 grid\n"
                       "What do you want to do?\n")
        if choice == "4":
            break
        if choice in menu.keys():
            menu[choice]()
            window.update_idletasks()
        else:
            print("False input :(")
        time.sleep(1)


if __name__ == '__main__':
    main()
