from bs4 import BeautifulSoup
import requests
import re
import csv

r = requests.get('https://en.wikipedia.org/wiki/Singlish_vocabulary')
soup = BeautifulSoup(r.text, 'html.parser')


data = [] #WORD-ORIGIN-DEFINATION-EXAMPLE
for table in soup.find_all('table'):
    tr = table.tr

    table_cells = []
    for row in table.find_all('tr'):
        row_cells = []
        for cell in row.find_all('td'):
            # replacing hyperlinks
            temp = re.sub(r'(\[\d+\])',r'',cell.text)
            cell = re.sub('\n','',temp)
            row_cells.append(cell)
        table_cells.append(row_cells)

    if (tr.contents[1].string =='Term' and tr.contents[3].string == 'Origin'):
        # TERM-ORIGIN-DEFINATION
        for row in table_cells:
            if row != []:
                row.append('')
                data.append(row)
    elif (tr.contents[1].string == 'Word'):
        # WORD-MEANING-EXAMPLE
        for row in table_cells:
            if row != []:
                new_row = []
                new_row.append(row[0])
                new_row.append('')
                new_row.append(row[1])
                new_row.append(row[2])
                data.append(new_row)
    else:
        # TERM-DEFINATION
        for row in table_cells:
            if row != []:
                new_row = []
                new_row.append(row[0])
                new_row.append('')
                new_row.append(row[1])
                new_row.append('')
                data.append(new_row)

f = open('singlish.txt', 'w', encoding='utf-16')

for row in data:
    first = True
    for cell in row:
        if (first == False):
            f.write('!@#$%')
        f.write(cell)
        first = False
    f.write('\n')
f.close()
