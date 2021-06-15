from tkinter import *

SIZE = 600


def devise_rectangle(img, a, b, color):
    for y in range(min(a[1], b[1]), max(a[1], b[1])):     # min och max funktionerna gör att vi inte behöver
        for x in range(min(a[0], b[0]), max(a[0], b[0])): # specificera vilken punkt (a, b) som är vilket hörn i
            img.put(color, (x, y))                        # rektangeln. Alla diagonalt motsatta hörn fungerar.


def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    devise_rectangle(img, [60, 100], [500, 400], "yellow")
    mainloop()


if __name__ == '__main__':
    main()
