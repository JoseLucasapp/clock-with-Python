from datetime import datetime
from tkinter import *
import threading

j = Tk()

label = Label(j,text='')
label.place(x=20,y=25)

hour    = datetime.now()
minutes  = datetime.now()
seconds = datetime.now()
hour    = hour.strftime('%H')
minutes  = minutes.strftime('%M')
seconds = seconds.strftime('%S')
hour    = int(hour)
minutes = int(minutes)
seconds = int(seconds)

timeOn = False

def setInterval(func,time):
    event = threading.Event()
    while not event.wait(time):
        func()

def clock():
    global seconds,minutes,hour,schedule
    if seconds <= 59:
        seconds = seconds + 1
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
        if minutes == 59:
            minutes = 0
            hour = hour + 1
        if hour == 24:
            hour = 0
    schedule = str(hour) + ":" + str(minutes) + ":" + str(seconds)
    label['text'] = schedule

    j.geometry('200x200')
    j.update()

setInterval(clock,1)