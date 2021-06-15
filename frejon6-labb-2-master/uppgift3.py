from tkinter import *

SIZE = 600


def devise_rectangle(img, a, b, color):
    for y in range(min(a[1], b[1]), max(a[1], b[1])):     # min och max funktionerna gör att vi inte behöver
        for x in range(min(a[0], b[0]), max(a[0], b[0])): # specificera vilken punkt (a, b) som är vilket hörn i
            img.put(color, (x, y))                        # rektangeln. Alla diagonalt motsatta hörn fungerar.


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


def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#426ff5")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    devise_frame(img, [60, 100], [500, 400], 10, "white", "black")
    mainloop()


if __name__ == '__main__':
    main()
