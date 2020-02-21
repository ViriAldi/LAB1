import copy


def read_data(path):
    rez = [[]]
    file = open(path)
    line1 = list(map(int, file.readline().strip().split()))
    line2 = list(map(int, file.readline().strip().split()))
    rez.append((line1, line2))
    while line1:
        line1 = list(map(int, file.readline().strip().split()))
        line2 = list(map(int, file.readline().strip().split()))
        rez[0].append((line1, line2))
    return rez[0][:len(rez[0]) - 1], rez[1]


def eff(prices, speed, time, sign):
    num = time * speed
    points = sum(prices[:num])

    eff = points / sign

    return eff


data = read_data(r'd_tough_choices.txt')

libs = data[0]
info = data[1]

price = info[1]
B, L, D = info[0]

libz = {}

for i in range(len(libs)):
    books = list(libs[i][1])
    libz[i] = [libs[i][0][1], libs[i][0][2]]
    pricez = sorted([price[book] for book in books], reverse=True)

    libz[i].append(pricez)

TIME = 0
order = []
libaries = copy.deepcopy(libz)
while TIME < D:
    effs = []
    for i in libz:
        sign, speed, prices = libz[i]
        effs.append((eff(prices, speed, D - TIME, sign), i))

    maxs = max(effs, key=lambda x: x[0])
    ind = maxs[1]

    order.append(ind)
    TIME += libz[ind][0]
    print(TIME)
    libz.pop(ind)


f = open('d_tough_choices.txt')
daysleft = int(f.readline().split()[2])

price = [int(x) for x in f.readline().split()]
f.close()
f = open('d.txt', 'w')
used = [0] * 100000
print(price)
uuu = 0

for i in order:
    printed = 0
    daysleft -= libaries[i][0]
    if daysleft < 0:
        uuu += 1
        break
    books = libs[i][1]
    takebooks = min(len(books), daysleft * libaries[i][1])
    if takebooks <= 0:
        uuu += 1
        break
    f.write(str(i) + ' ' + str(takebooks) + '\n')
    left = len(books)
    i = 0
    while printed < takebooks:
        if used[i] == 0:
            f.write(str(books[i]) + ' ')
            printed += 1
        elif printed + left <= takebooks:
            f.write(str(books[i]) + ' ')
        i += 1
        left -= 1
    f.write('\n')
f.write(str(len(order) - uuu) + '\n')
