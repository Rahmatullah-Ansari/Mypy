import time
from plyer import notification
#run app in background with pythonw .\filename.py
while 10:
    notification.notify(
        title = "Please take rest!!!",
        message = "it's harmful to continue work without break!!!",
        app_icon = "rest.ico",
        timeout = 10,
        app_name = "REST",
        ticker ='Please take rest!',
        toast = True
    )
    time.sleep(5)