from datetime import datetime, timedelta


def set_alarm(add_time)->str:
    add_time = int(add_time)
    current = datetime.now()
    currentTime = current.strftime("%H:%M:%S")
    alarm = current + timedelta(seconds=add_time)
    alarmTime = alarm.strftime("%H:%M:%S")
    print("The current time is", currentTime, "\n", "The alarm time is", alarmTime)

