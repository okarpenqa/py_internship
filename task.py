import csv
import json

def generator(first=5, last=90, step=1):
    x = first
    while x < last:
        yield x
        x += step


f1 = lambda x: x / (x + 100)
f2 = lambda x: 1 / x
f3 = lambda x: 20 * (f1(x) + f2(x)) / x
result_csv_filename = 'result.csv'
result_json_filename = 'result.json'

result = {}

for x in generator():
    result[x] = [f1(x), f2(x), f3(x)]

with open(result_csv_filename, 'w') as file:
    writer = csv.writer(file)

    for key, value in result.items():
        writer.writerow([key] + value)

with open(result_csv_filename, mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    result_from_csv = []

    for row in csv_reader:
        result_from_csv.append(row)

with open(result_json_filename, 'w') as f:
    f.write(json.dumps(result_from_csv))
