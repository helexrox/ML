
import csv

hypo = []
data = []
temp = []
gen = ['?', '?', '?', '?', '?', '?']

with open('enjoysport.csv') as csv_file:
    fd = csv.reader(csv_file)
    print("\nThe given training examples are:")
    for line in fd:
        print(line)
        temp.append(line)
        if line[-1].strip().lower() == "yes":
            data.append(line)

print("\nThe positive examples are:")
for line in data:
    print(line)

    print("\nThe final specific output:")
    row = len(data)
    col = len(data[0])

    for j in range(col - 1):
        hypo.append(data[0][j])

    for i in range(row):
        for j in range(col - 1):
            if hypo[j] != data[i][j]:
                hypo[j] = '?'
print(hypo)

print("\nThe final Generalize output:")
row = len(temp)
col = len(temp[0])

for i in range(row):
    if temp[i][-1].strip().lower() == "no":
        for j in range(col - 1):
            if temp[i][j] != hypo[j]:
                gen[j] = hypo[j]
                print(gen)
                gen[j] = '?'




