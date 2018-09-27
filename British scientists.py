fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
b = []
a = []
for string in fin:
    for word in string.split():
        b = list(word)
        a = b[1:-1]
        print(b)
        print(a)
        for i in range(0, len(a) - 1, 2):
            print(i, a[i], a[i+1])
            a[i], a[i+1] = a[i+1], a[i]
        print(a)
        fout.write(str(b[0]))
        for i in range(len(a)):
            fout.write(str(a[i]))
        fout.write((b[-1]))
        fout.write(' ')
fin.close()
fout.close()
#splits the file by strings and then by words and changes each second letter with the next one
