a = None
b = []
c = 0
d = 0
while True:
    a = int(input("Введите число:"))
    if a != 0:
        b.append(a)
    else:
        for i in range(len(b)):
            if (sum(map(int, str(b[i])))) >= c:
                c = (sum(map(int, str(b[i]))))
                d = i
        print("Число с максимальной суммой цифр:", b[d])