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
    return rez[0][:len(rez[0])-1], rez[1]


def eff(prices, speed, time, sign):
    num = time*speed
    points = sum(prices[:num])

    eff = points / sign

    return eff


data = read_data(r'C:\HASHCODE\e_so_many_books.txt')

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

temp = copy.deepcopy(libz)

for i in temp:
    if temp[i][1] == 1:
        libz.pop(i)

TIME = 0
order = []

while TIME < D:
    effs = []
    for i in libz:
        sign, speed, prices = libz[i]
        effs.append((eff(prices, speed, D - TIME, sign), i))

    maxs = max(effs, key=lambda x: x[0])
    ind = maxs[1]

    order.append(ind)
    TIME += libz[ind][0]

    libz.pop(ind)


print(order)