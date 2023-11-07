import tkinter as tk
from tkinter import simpledialog
import time
import winsound

def set_alarm():
    alarm_time = simpledialog.askstring("Alarm Clock", "Set the alarm time (HH:MM AM/PM):")
    
    if alarm_time is not None:
        while True:
            current_time = time.strftime("%I:%M %p")
            if current_time == alarm_time:
                play_alarm_sound()
                break

def play_alarm_sound():
    # You can replace 'sound.wav' with your preferred alarm sound file.
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

root = tk.Tk()
root.title("Alarm Clock")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

set_button = tk.Button(frame, text="Set Alarm", command=set_alarm)
set_button.pack()

exit_button = tk.Button(frame, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
