from datetime import datetime, timedelta
import time
import os

def set_alarm():
    alarm_time = input("Enter the time of alarm to be set (HH:MM:SS): ")
    try:
        alarm_datetime = datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM:SS format.")
        return

    print("Setting up alarm for", alarm_datetime.strftime("%I:%M:%S %p"))

    while True:
        now = datetime.now()
        if now >= alarm_datetime:
            print("Wake Up!")
            play_alarm()
            break
        time.sleep(1)

def play_alarm():
    try:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        audio_file_path = os.path.join(script_directory, 'audio.mp3')
        os.system(f'mpg123 "{audio_file_path}"')
    except Exception as e:
        print(f"Error playing alarm: {e}")

if __name__ == "__main__":
    set_alarm()
