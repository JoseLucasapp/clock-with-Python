from datetime import datetime
import threading

hour    = datetime.now()
minutes  = datetime.now()
seconds = datetime.now()
hour    = hour.strftime('%H')
minutes  = minutes.strftime('%M')
seconds = seconds.strftime('%S')
hour    = int(hour)
minutes = int(minutes)
seconds = int(seconds)

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
    print(schedule)

setInterval(clock,1)