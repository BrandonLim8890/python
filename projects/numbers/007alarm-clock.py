'''
Name: alarm-clock.py
Purpose: A simple clock where it plays a sound after X numbre of minutes/seconds or at a particular time
Author: Brandon Lim
'''

import winsound, time, datetime
def alarm():
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)

def user_inputs():
    print('1. Enter X number of minutes\n2. Enter hh/mm/ss for the alarm to go off')
    print('Select(1/2):')
    user_in = int(input())
    if user_in is 1:
        print('Enter # of minutes: ')
        minutes = int(input())
        print('Enter # of seconds')
        seconds = int(input())
        if minutes <= 60 and seconds <= 60 and minutes >= 0 and seconds >= 0:
            time.sleep(minutes * 60 + seconds)
            alarm()
        else:
            print('Incorrect format of seconds and minutes')
    elif user_in is 2:
        print('Enter hour:')
        hours = int(input())
        print('Enter minutes:')
        minutes = int(input())
        print('Enter seconds:')
        seconds = int(input())
        now = datetime.datetime.now()
        hour_wait = now.hour - hours
        minute_wait = 60 - now.minute + minutes
        second_wait = 60 - now.second + seconds
        total_wait = hour_wait * 60 * 60 + minute_wait * 60 + second_wait
        time.sleep(total_wait)
        alarm()

user_inputs()

