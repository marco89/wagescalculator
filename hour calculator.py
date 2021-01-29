import datetime
import re
import xlsxwriter

# Creates the link to the linked excel file

outWorkbook = xlsxwriter.Workbook('Wages.xlsx')

# Creates a sheet within that excel file
outSheet = outWorkbook.add_worksheet()

# Names the columns
outSheet.write('A1', 'Day')
outSheet.write('B1', 'Hours')


def ask_start_time(day_name, attempts=25):  # Asks what time work was started
    for a in range(attempts):
        start = input(f'What time did you start on {day_name}?')
        if 'na' in start:
            return '00:00'
        validation = re.match("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", start)
        if validation:
            return start
        print('Please use a HH:MM format only.')
    else:
        print('25 wrong attempts and you still don\'t understand that it\'s HH:MM?!')


def ask_finish_time(day_name, attempts=25):  # Asks what time work was finished
    for a in range(attempts):
        finish = input(f'What time did you finish on {day_name}?')
        if 'na' in finish:
            return '00:00'
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


def ask_user(days):  # Condenses ask_start_time and ask_finish_time into one function
    start = ask_start_time(days)
    finish = ask_finish_time(days)
    day_start = datetime.datetime.strptime(start, '%H:%M')
    day_fin = datetime.datetime.strptime(finish, '%H:%M')
    return day_fin - day_start


columns = ["A2", "A3", "A4", "A5", "A6", "A7", "A8"]


mon = (ask_user('Monday'))
outSheet.write('A2', 'Mon')
outSheet.write('B2', (mon * 24))
tue = (ask_user('Tuesday'))
outSheet.write('A3', 'Tue')
outSheet.write('B3', (tue * 24))
wed = (ask_user('Wednesday'))
outSheet.write('A4', 'Wed')
outSheet.write('B4', (wed * 24))
thu = (ask_user('Thursday'))
outSheet.write('A5', 'Thu')
outSheet.write('B5', (thu * 24))
fri = (ask_user('Friday'))
outSheet.write('A6', 'Fri')
outSheet.write('B6', (fri * 24))
sat = (ask_user('Saturday'))
outSheet.write('A7', 'Sat')
outSheet.write('B7', (sat * 24))
sun = (ask_user('Sunday'))
outSheet.write('A8', 'Sun')
outSheet.write('B8', (sun * 24))

outWorkbook.close()