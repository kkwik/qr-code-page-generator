import csv
import sys

file_input = sys.argv[1]

template = '''
<div>
    <a href="%URL%">%TEXT%</a>
    <a href="%QRCODE_PATH%"><img class="qr-code" src="%QRCODE_PATH%" /></a>
</div>
'''

output = ''

with open(file_input) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        qrcode_filename = f'qr_codes\{row[0].lower().replace(" ", "_")}.svg'

        output += template
        output = output.replace('%URL%', row[1])
        output = output.replace('%TEXT%', row[0])
        output = output.replace('%QRCODE_PATH%', qrcode_filename)
    
    print(output)


        

