import argparse
import datetime
import holidays
import csv

parser = argparse.ArgumentParser()
parser.add_argument('year', type=int, help='year')  # argument "year" int tüüpi
args = parser.parse_args()

header = ["Kuu ", "Palgapäev ", "Meeldetuletus"]  # tabeli päis
rows = []  # siia kogunevad iga kuu andmed

max_payday_len = len(header[1])   # hoiame sõna "Palgapäev" pikkuse
max_reminder_len = len(header[2])  # hoiame sõna "Meeldetuletus" pikkuse

# genereerime iga kuu andmeid ja lisame neid listi
for month in range(1, 13):
    date = datetime.date(args.year, month, 1)
    pay_date = datetime.date(args.year, month, 10)

    # kui nädalavahetus, siis valime eelmise tööpäeva
    while pay_date.weekday() >= 5 or pay_date in holidays.EST():
        pay_date -= datetime.timedelta(days=1)

    reminder_date = pay_date - datetime.timedelta(days=3)

    # kui nädalavahetus, siis valime eelmise tööpäeva
    while reminder_date.weekday() >= 5 or reminder_date in holidays.EST():
        reminder_date -= datetime.timedelta(days=1)

    # lisame hetkeloleva kuu andmed rows listi
    rows.append([datetime.date(args.year, month, 1).strftime("%B"), pay_date.strftime('%d.%m.%Y'), reminder_date.strftime('%d.%m.%Y')])

# lisame andmeid CSV faili
with open(f'{args.year}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE, quotechar='')
    writer.writerow(['{:<20}'.format(header[0]), '{:<{}}'.format(header[1], max_payday_len), '{:<{}}'.format(header[2], max_reminder_len)])
    for row in rows:
        writer.writerow(['{:<20}'.format(row[0]), '{:<{}}'.format(row[1], max_payday_len), '{:<{}}'.format(row[2], max_reminder_len)])
    csvfile.close()
