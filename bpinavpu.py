import requests, csv, datetime
from bs4 import BeautifulSoup


date_today = datetime.date.today()

r = requests.get('https://www.bpiexpressonline.com/p/1/689/investment-funds-daily-prices')
soup = BeautifulSoup(r.content, 'html.parser')
tables = soup.findAll('table')

data_today = []
rows = tables[0].find('tbody').findAll('tr')
for row in rows:
    cols = row.findAll('td')
    cols = [elements.text.strip() for elements in cols]
    if cols[0] == 'BPI Philippine Equity Index Fund':
        data_today.append(date_today)
        data_today.append(cols[1])

with open('bpinavpu.csv', mode='a', newline="") as bpi_data_file:
    csv_writer = csv.writer(bpi_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(data_today)
bpi_data_file.close()
