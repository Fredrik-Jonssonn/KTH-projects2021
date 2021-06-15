from tkinter import *
import math

SIZE = 600


def devise_rectangle(img, a, b, color):
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            img.put(color, (x, y))


def devise_frame(img, a, b, outline, color1, color2):
    devise_rectangle(img, a, b, color1)
    if a[0] > b[0] and a[1] > b[1]:
        c = [a[0] - outline, a[1] - outline]
        d = [b[0] + outline, b[1] + outline]
    elif a[0] > b[0] and a[1] < b[1]:
        c = [a[0] - outline, a[1] + outline]
        d = [b[0] + outline, b[1] - outline]
    elif a[0] < b[0] and a[1] > b[1]:
        c = [a[0] + outline, a[1] - outline]
        d = [b[0] - outline, b[1] + outline]
    else:
        c = [a[0] + outline, a[1] + outline]
        d = [b[0] - outline, b[1] - outline]
    devise_rectangle(img, c, d, color2)


def triangle_area(a, b, c):
    area = abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)
    return area


def devise_triangle(img, a, b, c, color):
    area_of_triangle = triangle_area(a, b, c)
    for x in range(SIZE):
        for y in range(SIZE):
            test_coordinate = [x, y]
            if (triangle_area(a, b, test_coordinate)
                + triangle_area(a, test_coordinate, c)
                + triangle_area(test_coordinate, b, c)
                == area_of_triangle):
                img.put(color, (x, y))


def devise_julgran(img, a, b, c, color): #a vänster, b mitten, c höger
    devise_rectangle(img, ((b[0]+round((c[0]-a[0])*0.075)), a[1]),
                     (round((b[0] - (c[0] - a[0]) * 0.075)),
                     (a[1] + (c[1] - b[1]))), "brown")
    for i in range(4):
        devise_triangle(img, a, b, c, color)
        triangle_base = c[0] - a[0]
        triangle_height = c[1] - b[1]
        a[0] += round(triangle_base*0.075)
        c[0] -= round(triangle_base*0.075)
        a[1] -= round(triangle_height*0.65)
        b[1] -= round(triangle_height*0.65)
        c[1] -= round(triangle_height*0.65)


def devise_circle(img, radius, center, color):
    for y in range(SIZE):
        for x in range(SIZE):
            if math.sqrt(((center[0]-x)**2)+((center[1])-y)**2) <= radius:
                img.put(color, (x, y))


def drawing(img):
    devise_circle(img, 50, [100, 100], "yellow")
    devise_rectangle(img, [200, 200], [400, 300], "yellow")
    devise_frame(img, [300, 250], [325, 300], 3, "black", "brown")
    devise_triangle(img, [200, 200], [400, 200], [300, 100], "red")
    devise_julgran(img, [225, 325], [250, 300], [275, 325], "green")

def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    drawing(img)
    mainloop()


if __name__ == '__main__':
    main()
