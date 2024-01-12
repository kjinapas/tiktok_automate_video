
import moviepy.editor as mpe
import random
import os
from moviepy.editor import  AudioFileClip
from get_quotes import *

from moviepy.editor import clips_array

import datetime
time = datetime.datetime.now()

# Directory containing your video files
video_directory = "video"
audio_directory = "music"


#define screensize 
screensize =(1000,1920)

video_files = [os.path.join(video_directory, f) for f in os.listdir(video_directory) if f.endswith(".mp4")]
audio_files = [os.path.join(audio_directory, f) for f in os.listdir(audio_directory) if f.endswith(".mp3")]

#------------------------------------------------------

def delete_video_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".avi"):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print(e)
               
#----------------------------------------------------------------------------



def gen_clip_v1(number):
    
    text = gen_quotes(number)
    video_file = random.choice(video_files)
    
    audio_file = random.choice(audio_files)
    clip = mpe.VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    audio_clip = audio_clip.subclip(0, 10)
    
    text_clip = mpe.TextClip(
        txt=text,
        font="font/TH-Krub/TH Krub Bold.ttf",
        fontsize=50,
        color="white", 
        method='caption',
        size=screensize,
        align='center',
    
    ).set_position('center','top')

    video_clip = clip.set_audio(audio_clip)
    final_clip = mpe.CompositeVideoClip([video_clip, text_clip]).set_duration(10)
    final_clip.write_videofile(f"out_put/day_{time.day}_{time.minute}_clip.mp4")

#----------------------------------------------------------------------------


def gen_clip_v2(number):
    
    for number ,i in enumerate( gen_quotes_v2(number)):
        video_file = random.choice(video_files)
        audio_file = random.choice(audio_files)

        clip = mpe.VideoFileClip(video_file)
        audio_clip = AudioFileClip(audio_file)

        audio_clip = audio_clip.subclip(0, 10)
        
        text_clip = mpe.TextClip(
            txt=i,
            font="font/TH-Krub/TH Krub Bold.ttf",
            fontsize=50,
            color="white", 
            method='caption',
            size=screensize,
            align='center',
        
        ).set_position('center','top')

        video_clip = clip.set_audio(audio_clip)
        final_clip = mpe.CompositeVideoClip([video_clip, text_clip]).set_duration(10)
        final_clip.write_videofile(f"out_put/day_{time.day}_{time.minute}_clip{number+1}.mp4")

#----------------------------------------------------------------------------


def gen_clip_text(text):
    
    video_file = random.choice(video_files)
    audio_file = random.choice(audio_files)

    clip = mpe.VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)

    audio_clip = audio_clip.subclip(0, 10)

    full_text =f'"{text}"\n..........'


    
    text_clip = mpe.TextClip(
        txt=full_text,
        font="font/TH-Krub/TH Krub Bold.ttf",
        fontsize=70,
        color="white", 
        method='caption',
        size=screensize,
        align='center',
    
    ).set_position('center','top')

    video_clip = clip.set_audio(audio_clip)
    final_clip = mpe.CompositeVideoClip([video_clip, text_clip]).set_duration(10)
    final_clip.write_videofile(f"out_put/day_{time.day}_{time.minute}_clip.mp4")




delete_video_files("out_put")

gen_clip_v1(1)


