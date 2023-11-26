import os
import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def extract_text_from_video(video_file):
    num_seconds_video = 52 * 60
    print("The video is {} seconds".format(num_seconds_video))
    timestamps = list(range(0, num_seconds_video + 1, 60))

    results = {}
    for i in range(len(timestamps) - 1):
        ffmpeg_extract_subclip(video_file, max(0, timestamps[i] - 2), timestamps[i + 1],
                               targetname=f"chunks/cut{i + 1}.mp4")
        
        clip = mp.VideoFileClip(f"chunks/cut{i + 1}.mp4") 
        clip.audio.write_audiofile(f"converted/converted{i + 1}.wav")
        
        r = sr.Recognizer()
        audio = sr.AudioFile(f"converted/converted{i + 1}.wav")
        
        with audio as source:
            r.adjust_for_ambient_noise(source)  
            audio_file = r.record(source)
        
        result = r.recognize_google(audio_file)
        results[f'chunk{i + 1}'] = result

    return [results[f'chunk{i + 1}'] for i in range(len(results))]

def save_text_to_file(text, output_file):
    text_content = '\n'.join(text)
    with open(output_file, mode ='w') as file: 
        file.write("Recognized Speech:\n") 
        file.write(text_content)
        print("Text extracted and saved successfully!")

# Example usage:
video_file_path = "videorl.mp4"
extracted_text = extract_text_from_video(video_file_path)
save_text_to_file(extracted_text, "recognized.txt")
