# Battery Checker and Battery Notifier
"""
    Author : YOGESHWARAN R
    Description: Notify if battery is full or low 
    
"""
import psutil
from win10toast import ToastNotifier
import time
def secs2hours(secs):
    seconds = secs % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)
startup = ToastNotifier()
startup.show_toast("RSYT Battery Alerts! It saves your Battery",icon_path="bat.ico")
battery = psutil.sensors_battery() 
percent = battery.percent
plug = battery.power_plugged
remain = battery.secsleft
def note(a,b,c):
    x = "Battery Percentage:"+str(a)+"%"
    if b is True:
        y = "Charger Connected"
    else:
        y = "Charger Disconnected"
    z = "Time Left:"+secs2hours(remain)
    tub = (x,y,z)
    return str(tub).replace("'","").replace("(","").replace(")","")

def notes(a,b):
    x = "Battery Percentage: "+str(a)+"%"
    if a == 100:
        y = "Battery fully Charged"
    elif a == 30:
        y = "Battery is low"
    else:
        y = "Battery is running"
    z = "Time Left: "+secs2hours(remain)
    tub = (x,y,z)
    return str(tub).replace("'","").replace("(","").replace(")","").replace(",","")

notify = ToastNotifier()

if percent == 100:
    notify.show_toast(notes(percent,remain),
    duration=20,
    icon_path="bat.ico")
    while notify.notification_active():
        time.sleep(0.1)
elif percent == 30:
    notify.show_toast(notes(percent,remain),
    duration=20,
    icon_path="bat.ico")
    while notify.notification_active():
        time.sleep(0.1)
else:
    pass

print(note(percent,plug,remain))
