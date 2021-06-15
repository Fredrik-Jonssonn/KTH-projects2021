def ramanujan(n):
    lösningar = []
    a = 0
    b = 0
    while a <= b:
        b = int(round((n - (a**3))**(1/3)))
        if a <= b and ((a ** 3) + (b ** 3) == n):
            lösningar.append((a, b))
        a += 1
    print(lösningar)