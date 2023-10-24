i=0
while True:

    i=float(input("Add meg a hőmérsékleti értéket: "))
    if i>=0:
        print("Nem volt fagy")
    if -49<i<0:
        print("Fagy volt")
    if i == -50: break
