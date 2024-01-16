from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os

link = input("Input YouTube Link: ")
yt = YouTube(link)
video_title = yt.title

#downloading video and audio files
video_stream = yt.streams.filter(res="1080p").first()
video = video_stream.download(filename="video.mp4")

audio_stream = yt.streams.filter(only_audio=True).first()
audio = audio_stream.download(filename="audio.mp3")

video_clip = VideoFileClip(video)
audio_clip = AudioFileClip(audio)

new_audioclip = CompositeAudioClip([audio_clip])
video_clip = video_clip.set_audio(new_audioclip)

#creates merged video with audio
video_clip.write_videofile(video_title + ".mp4", codec="libx264", audio_codec="aac")

#deleting downloaded video/audio files
os.remove(video)
os.remove(audio)
video_clip.close()
new_audioclip.close()
