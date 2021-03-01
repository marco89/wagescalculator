from datetime import datetime
import datetime
import re
import xlsxwriter
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()  # Creates GUI
canvas = tk.Canvas(root, width=500, height=500)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open('titleofcalc.png')  # Adds text logo for GUI
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=2, row=0)

instructions = tk.Label(root, text='Please input your hourly wage.')  # Instructions for user on GUI
instructions.grid(columnspan=1, column=2, row=1)

entry1 = tk.Entry(root)
canvas.create_window(200, 140, window=entry1)

proceed_text = tk.StringVar()  # Creates proceed button for GUI
proceed_button = tk.Button(root, textvariable=proceed_text, command=lambda: proceed_to_input(), bg='#858485',
                           fg='white', height=2, width=15)

outWorkbook = xlsxwriter.Workbook('Wages.xlsx')  # Creates the link to the linked Excel file

outSheet = outWorkbook.add_worksheet()  # Creates a sheet within that excel file

outSheet.write('A1', 'Day')  # Names the columns
outSheet.write('B1', 'Hours')


def proceed_to_input():  # Button functionality
    print('Test')


def ask_start_time(day_name, attempts=25):  # Asks what time work was started
    for a in range(attempts):
        start = input(f'What time did you start on {day_name}?')
        if 'na' in start:
            return '00:00'
        validation = re.match('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', start)
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
        validation = re.match('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', finish)
        if validation:
            return finish
        print('Please use a HH:MM format only.')


def hourly_wage(attempts=25):  # Asks hourly rate of pay
    for a in range(attempts):
        wage = input(f'What is your hourly rate of pay?')
        validation = re.match('^[0-9].[0-9]|[0-9]*$', wage)
        if validation:
            return wage
        else:
            print('Please use a N:NN format only.')


def days():  # Lists the days of the week which allows ask_start_time/ask_finish_time to work
    work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_times = {day: ask_start_time for day in work_days}
    print(start_times)


def ask_user(days):  # Condenses ask_start_time and ask_finish_time into one function
    start = ask_start_time(days)
    finish = ask_finish_time(days)
    day_start = datetime.datetime.strptime(start, '%H:%M')
    day_fin = datetime.datetime.strptime(finish, '%H:%M')
    return day_fin - day_start


proceed_text.set('Next')
proceed_button.grid(column=2, row=2)

root.mainloop()  # Closes GUI instructions

print('Please enter \'na\' on days you didn\'t work')
print('')

wage = float(hourly_wage())

mon = (ask_user('Monday'))
tue = (ask_user('Tuesday'))
wed = (ask_user('Wednesday'))
thu = (ask_user('Thursday'))
fri = (ask_user('Friday'))
sat = (ask_user('Saturday'))
sun = (ask_user('Sunday'))

hours_worked = (
    ['Mon', mon],
    ['Tue', tue],
    ['Wed', wed],
    ['Thu', thu],
    ['Fri', fri],
    ['Sat', sat],
    ['Sun', sun],
)

row = 1
col = 0

for day, hours in hours_worked:
    outSheet.write(row, col, day)
    outSheet.write(row, col + 1, hours * 24)
    row += 1

week_hours = (mon + tue + wed + thu + fri + sat + sun)

total_seconds = week_hours.total_seconds()

hours = ((total_seconds / 60) / 60)

pay = float(hours * wage)

outSheet.write('A10', 'Wages')
outSheet.write('B10', pay)

outWorkbook.close()  # Closes and saves Excel spreadsheet
