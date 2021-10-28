from pytube import YouTube
# link = "https://www.youtube.com/watch?v=Q1mG449nemg"
link = "https://www.youtube.com/watch?v=XVv6mJpFOb0"
yt = YouTube(link)
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(progressive=True))
ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')
print("Downloading".center(10, "~"))
ys.download()
print("Downloaded!".center(10, "~"))
'''
from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
'''