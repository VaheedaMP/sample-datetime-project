# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime


def myfun(date):
    formats = ['%d-%b-%Y', '%d %b %Y', '%d/%b/%Y']

    for format_str in formats:
        try:
            date_object = datetime.strptime(date, format_str)
            return date_object.strftime('%d-%m-%Y')
        except ValueError:
            pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(myfun('22-JUN-2024'))
    print(myfun('22-SEP-1994'))
    print(myfun('22 SEP 1994'))
    print(myfun('22/SEP/1994'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
