from pytube import YouTube

link = "" # here insert the link of the video
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yt = yt.streams.get_highest_resolution()

yt.download("") # here insert the folder where you want to put the download