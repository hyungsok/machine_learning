import sys

# 콘솔명령어
# python read_toplist_data.py 'toplist_data.csv' 'output_data.csv'
input_file = sys.argv[1]
output_file = sys.argv[2]

if input_file:
    input_file = 'toplist_data.csv'
if output_file:
    output_file = 'output_data.csv'

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str, header_list)) + '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str, row_list)) + '\n')
