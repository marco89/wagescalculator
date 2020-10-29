from datetime import datetime
import time
import xlsxwriter

# This part is to export the final numbers to an excel spreadsheet #

# Creates the link to the linked excel file
outWorkbook = xlsxwriter.Workbook('Wages.xlsx')

# Creates a sheet within that excel file
outSheet = outWorkbook.add_worksheet()

# Creates the data fields needed i.e Days of the week and hours worked
days = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
values = ['wed_hours', 'thur_hours', 'fri_hours', 'sat_hours', 'sun_hours']

# Names the columns
outSheet.write('A1', 'Day')
outSheet.write('B1', 'Hours')


# Defines all the phrases to save space

def ask_start():
    return 'What time did you start on'


def ask_finish():
    return 'What time did you finish on'


def tell_work():
    return 'You worked'


# This is the code itself #

print('Initialising wage calculator...')

time.sleep(0.5)

wed_start = input(ask_start() + ' Wednesday?')
wed_fin = input(ask_finish() + ' Wednesday?')
fmt = '%H:%M'
wed_hours = datetime.strptime(wed_fin, fmt) - datetime.strptime(wed_start, fmt)
print(tell_work(), wed_hours, 'hours on Wednesday.')

outSheet.write('A2', 'Wed')
outSheet.write('B2', (wed_hours * 24))

thur_start = input(ask_start() + ' Thursday?')
thur_fin = input(ask_finish() + ' Thursday?')
fmt = '%H:%M'
thur_hours = datetime.strptime(thur_fin, fmt) - datetime.strptime(thur_start, fmt)
print(tell_work(), thur_hours, 'hours on Thursday.')

outSheet.write('A3', 'Thur')
outSheet.write('B3', (thur_hours * 24))

fri_start = input(ask_start() + ' Friday?')
fri_fin = input(ask_finish() + ' Friday?')
fmt = '%H:%M'
fri_hours = datetime.strptime(fri_fin, fmt) - datetime.strptime(fri_start, fmt)
print(tell_work(), fri_hours, 'hours on Friday.')

outSheet.write('A4', 'Fri')
outSheet.write('B4', (fri_hours * 24))

sat_start = input(ask_start() + ' Saturday?')
sat_fin = input(ask_finish() + ' Saturday?')
fmt = '%H:%M'
sat_hours = datetime.strptime(sat_fin, fmt) - datetime.strptime(sat_start, fmt)
print(tell_work(), sat_hours, 'hours on Saturday.')

outSheet.write('A5', 'Sat')
outSheet.write('B5', (sat_hours * 24))

sun_start = input(ask_start() + ' Sunday?')
sun_fin = input(ask_finish() + ' Sunday?')
fmt = '%H:%M'
sun_hours = datetime.strptime(sun_fin, fmt) - datetime.strptime(sun_start, fmt)
print(tell_work(), sun_hours, 'hours on Sunday.')

outSheet.write('A6', 'Sun')
outSheet.write('B6', (sun_hours * 24))

total_hours = wed_hours + thur_hours + fri_hours + sat_hours + sun_hours

hours = total_hours.total_seconds() / 3600

print('You have worked', hours, 'hours this week.')

print('At your rate of pay that is', '£', (hours * 8.72), 'paid for this week.')

outSheet.write('B8', hours)

outWorkbook.close()
