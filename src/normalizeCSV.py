import csv
with open('../docs/comp.csv') as input, open('../docs/company_sector.csv', newline='', mode='w') as output:
    reader = csv.reader(input, delimiter=',')
    writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['company', 'sector'])
    check = False
    for row in reader:
        if not check:
            header = row
            check = True
        else:
            for c in range(len(row)):
                if row[c] == 'X':
                    writer.writerow([row[0], header[c]])