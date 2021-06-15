from tkinter import *

SIZE = 600


def devise_rectangle(img, a, b, color):
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            img.put(color, (x, y))


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


def devise_julgran(img, a, b, c, color):
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



def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    devise_julgran(img, [200, 400], [300, 300], [400, 400], "green")
    mainloop()


if __name__ == '__main__':
    main()
