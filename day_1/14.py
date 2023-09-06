L = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]
x = 0
while True:
    first = "123" + L[x] + '5'
    second = "1" + L[x] + '233'
    if (int(first, 15) + int(second, 15)) % 14 == 0:
        print((int(first, 15) + int(second, 15)) // 14)
        break
    else:
        x += 1
