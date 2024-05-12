L = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]
for x in L:
    first = "123" + x + '5'
    second = "1" + x + '233'
    if (int(first, 15) + int(second, 15)) % 14 == 0:
        print((int(first, 15) + int(second, 15)) // 14)
        break
