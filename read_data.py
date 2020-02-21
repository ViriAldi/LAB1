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

print(read_data('a_example.txt'))