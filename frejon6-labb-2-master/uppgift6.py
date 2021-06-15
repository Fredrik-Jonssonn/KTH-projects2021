from tkinter import *
import math

SIZE = 600


def devise_circle(img, radius, center, color):
    for y in range(SIZE):
        for x in range(SIZE):
            if math.sqrt(((center[0]-x)**2)+((center[1])-y)**2) <= radius:
                img.put(color, (x, y))

def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    devise_circle(img, 100, [300, 300], "red")
    mainloop()


if __name__ == '__main__':
    main()
