#first u need to import pytube

from pytube import YouTube
link=input("https://www.youtube.com/watch?v=vh525RjO6C0&t=721s")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()
