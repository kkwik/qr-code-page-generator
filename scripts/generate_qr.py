import segno
import csv
import sys

file_input = sys.argv[1]
output_dir = sys.argv[2]

with open(file_input) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        file_name = row[0].lower().replace(" ", "_")
        qrcode = segno.make(f'{row[1]}')
        print(f'{file_name} {qrcode.designator}')
        print(f'{output_dir}\\{file_name}.svg')
        qrcode.save(f'{output_dir}\\{file_name}.svg', scale=10)
