number = []
for i in range(10):
    number.append(str(i))
out = []
with open ('C:/Test Space of Python/dataset_3363_2.txt', 'r') as inf:
    for line in inf:
        txt = list(line.strip())
        y = 0
        stroka = ''
        for i in range(len(txt)):
            if y < len(txt) - 1:
                if txt[y] in number and txt[y + 1] in number:
                    stroka += (txt[y - 1]*(int(txt[y] + txt[y + 1])))
                    y += 2
                elif txt[y] in number:
                    stroka += (txt[y - 1] * (int(txt[y])))
                    y += 1
                else:
                    y += 1
        out.append(stroka)
with open('C:/Test Space of Python/out.txt', 'w') as ouf:
    for i in out:
        ouf.write(i)

