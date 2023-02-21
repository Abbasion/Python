from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of the alarm to be set: HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alram_seconds = alarm_time[6:8]
alram_period = alarm_time[9:11].upper()
print("setting up Alarm...")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if (alram_period == current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alram_seconds==current_seconds):
                    print("wake up")
                    playsound('alarmsound.mp3')
                    break