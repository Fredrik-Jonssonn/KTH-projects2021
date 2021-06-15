from tkinter import *

SIZE = 600


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


def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    devise_triangle(img, [1, 1], [300,  599], [599, 1], color="yellow")
    mainloop()


if __name__ == '__main__':
    main()
