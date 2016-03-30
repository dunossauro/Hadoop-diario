from sys import stdin

print (("Nº |%-20s%s|%-7s|%s") % ("Frase", " " * 8, "Prob", "Cont"))
print (("%s+%s+%s+%s") % ("-"*3, "-" * 28,"-" * 7 ,"-" * 5))
dic = {}
contador = 0

for line in stdin:
    contador += 1
    line = line.strip()
    word, count = line.split('\t')

    count = int(count)

    if word not in dic:
        dic[word] =  count
    else:
        dic[word] += count

for n,x in enumerate(sorted(dic)):
    print (('{n}  |\t%-20s\t|%0.2f%%\t|%5s') % (n, x, float(dic[x]/contador*100),dic[x]))
