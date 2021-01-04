import datetime
import re
import xlsxwriter

# Creates the link to the linked excel file
outWorkbook = xlsxwriter.Workbook('Wages.xlsx')

# Creates a sheet within that excel file
outSheet = outWorkbook.add_worksheet()

# Names the columns for the excel document
outSheet.write('A1', 'Day')
outSheet.write('B1', 'Hours')


def tell_work():  # Relays how many hours worked
    return 'You worked'


def ask_start_time(day_name, attempts=25):  # Asks what time work was started
    for a in range(attempts):
        start = input(f'What time did you start on {day_name}?')
        validation = re.match("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", start)
        if validation:
            return start
        print('Please use a HH:MM format only.')
    else:
        print('25 wrong attempts and you still don\'t understand that it\'s HH:MM?!')


def ask_finish_time(day_name, attempts=25):  # Asks what time work was started
    for a in range(attempts):
        finish = input(f'What time did you finish on {day_name}?')
        validation = re.match("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", finish)
        if validation:
            return finish
        print('Please use a HH:MM format only.')


def days():  # Lists the days of the week which allows ask_start_time/ask_finish_time to work
    work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_times = {day: ask_start_time for day in work_days}
    print(start_times)


def time_diff(a, b):  # Calculates time difference between start and finish
    return b - a


start = ask_start_time('Monday')
mon_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Monday')
mon_fin = datetime.datetime.strptime(finish, '%H:%M')
mon_hours = time_diff(mon_start, mon_fin)
print(mon_hours)
outSheet.write('A2', 'Mon')
outSheet.write('B2', (mon_hours * 24))

start = ask_start_time('Tuesday')
tue_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Tuesday')
tue_fin = datetime.datetime.strptime(finish, '%H:%M')
tue_hours = time_diff(tue_start, tue_fin)
print(tue_hours)
outSheet.write('A3', 'Tue')
outSheet.write('B3', (tue_hours * 24))

start = ask_start_time('Wednesday')
wed_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Wednesday')
wed_fin = datetime.datetime.strptime(finish, '%H:%M')
wed_hours = time_diff(wed_start, wed_fin)
print(wed_hours)
outSheet.write('A4', 'Wed')
outSheet.write('B4', (wed_hours * 24))

start = ask_start_time('Thursday')
thu_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Thursday')
thu_fin = datetime.datetime.strptime(finish, '%H:%M')
thu_hours = time_diff(thu_start, thu_fin)
print(thu_hours)
outSheet.write('A5', 'Thu')
outSheet.write('B5', (thu_hours * 24))

start = ask_start_time('Friday')
fri_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Friday')
fri_fin = datetime.datetime.strptime(finish, '%H:%M')
fri_hours = time_diff(fri_start, fri_fin)
print(fri_hours)
outSheet.write('A6', 'Fri')
outSheet.write('B6', (fri_hours * 24))

start = ask_start_time('Saturday')
sat_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Saturday')
sat_fin = datetime.datetime.strptime(finish, '%H:%M')
sat_hours = time_diff(sat_start, sat_fin)
print(sat_hours)
outSheet.write('A7', 'Sat')
outSheet.write('B7', (sat_hours * 24))

start = ask_start_time('Sunday')
sun_start = datetime.datetime.strptime(start, '%H:%M')
finish = ask_finish_time('Sunday')
sun_fin = datetime.datetime.strptime(finish, '%H:%M')
sun_hours = time_diff(sun_start, sun_fin)
print(sun_hours)
outSheet.write('A8', 'Sun')
outSheet.write('B8', (sun_hours * 24))

total_hours = mon_hours + tue_hours + wed_hours + thu_hours + fri_hours + sat_hours + sun_hours

print(total_hours)

outSheet.write('A11', 'Hours worked')
outSheet.write('B11', total_hours)

outWorkbook.close()
