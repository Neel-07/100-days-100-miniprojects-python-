import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        return "Unknown"
    except sr.RequestError:
        return "Could not request results"

def add_note():
    speak("Please speak the title of the note.")
    title = recognize_speech()
    speak("Now, please speak the content of the note.")
    content = recognize_speech()
    notes[title] = content
    update_note_list()
    speak("Note added successfully.")

def view_note():
    speak("Please speak the title of the note you want to view.")
    title = recognize_speech()
    if title in notes:
        speak("Here is your note: " + notes[title])
    else:
        speak("Note not found.")

def update_note():
    speak("Please speak the title of the note you want to update.")
    title = recognize_speech()
    if title in notes:
        speak("Now, please speak the new content for the note.")
        content = recognize_speech()
        notes[title] = content
        update_note_list()
        speak("Note updated successfully.")
    else:
        speak("Note not found.")

def delete_note():
    speak("Please speak the title of the note you want to delete.")
    title = recognize_speech()
    if title in notes:
        del notes[title]
        update_note_list()
        speak("Note deleted successfully.")
    else:
        speak("Note not found.")

def update_note_list():
    note_list.delete(0, tk.END)
    for title in notes:
        note_list.insert(tk.END, title)

def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

notes = {}
root = tk.Tk()
root.title("Note Organizer with Voice Commands")

note_list = tk.Listbox(root)
note_list.pack()

add_button = tk.Button(root, text="Add Note", command=add_note)
view_button = tk.Button(root, text="View Note", command=view_note)
update_button = tk.Button(root, text="Update Note", command=update_note)
delete_button = tk.Button(root, text="Delete Note", command=delete_note)

add_button.pack()
view_button.pack()
update_button.pack()
delete_button.pack()

root.mainloop()
