"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user = ()


def prompt():
    global user
    user = input(
        "Press Enter to see the current month and year \nalso you can provide a month, \nor a month and year separated by a dash: ").split('-')
    user = [int(i) for i in user if i != '']
    render_data(user)


def render_data(user_input):
    today = datetime.now()
    if not user_input:
        # Print current month
        print(calendar.month(today.year, today.month))
        prompt()
    elif len(user_input) == 1:
        # Print month in current year
        print(calendar.month(today.year, user_input[0]))
        prompt()
    elif len(user_input) == 2:
        # Print month and year provided
        print(calendar.month(user_input[1], user_input[0]))
        prompt()
    else:
        error_handler()


def error_handler():
    print("Press Enter to see the current month and year also you can provide a month, or a month and year separated by a dash: ")
    prompt()


prompt()
