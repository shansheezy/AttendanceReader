# Name: Shante' Perrin
#Project 2 Option B

from getpass import getpass
from winsound import Beep
import csv
import datetime

print('Welcome!')
coursename = input('Please enter the course name (EX DANA 5001): ')

# Name file and open it
a = open('captureattendance.txt', 'w')

def captureattendance():

    #Beep
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    while True:
    # Notepad or other: begin swipes
        swipedata = getpass("Please swipe your card. Press enter when done with attendance capture: ")
        if len(swipedata) < 23:
            print('Invalid swipe. Try again.')
        else:
            a.writelines(swipedata + '\n')
            print('Swipe confirmed')
            Beep(frequency, duration)
            continue

        if swipedata in swipedata == '':
            break        

captureattendance()

beginbatch = input('Would you like to start the batch? Press (y)es or (n)o. Then press enter:')
while True:
    try:
        if 'y' or 'Y' in beginbatch:
            matchnamesCSV()
            writedata()
            break

        if 'n' or 'N' in beginbatch:
            print('Attenance successfully captured without batch. View attendance.txt')
            break
    except:
        if 'y' or 'Y' or 'n' or 'N' not in beginbatch:
            print('Incorrect Selection. Try again.')
            break


capfile = open('captureattendance.txt')

name = ''
sid = ''
currentDT = ''
header = ['Student ID', 'Student Name, Time Logged']
atfile = open('dailyattendance.csv', 'a')


def matchnamesCSV(sid, name, currentDT):
        for line in capfile:
                name = line.split('^')
                morethanname = name[1] 
                name = morethanname[:-18]
                sid = line[1:10]
                currentDT = datetime.datetime.now()
                return
                
def writedata():
    with atfile as dailyattendanceCSV:
            rows = zip(sid, name, currentDT)
            csv_writer = csv.writer(dailyattendanceCSV)
            
            csv_writer.writerow(header) # write header
            for row in rows:
                    csv_writer.writerow(rows)


a.close()
