import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

def get_calendar_for(year, month):
    cal_text = ''
    cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    cal_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    week_separator = ('+----------' * 7) + '+\n'
    blank_row = ('|          ' * 7) + '|\n'
    current_date = datetime.date(year, month, 1)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)
    while True:
        cal_text += week_separator
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += '|\n'
        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row
        if current_date.month != month:
            break
    cal_text += week_separator
    return cal_text

year = int(input('Enter the year for the calendar: '))
month = int(input('Enter the month for the calendar, 1-12: '))

cal_text = get_calendar_for(year, month)
print(cal_text)

calendar_filename = f'calendar_{year}_{month}.txt'
with open(calendar_filename, 'w') as file_obj:
    file_obj.write(cal_text)

print(f'Saved to {calendar_filename}')
