from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)

print(yt.thumbnail_url)
print("Title: ", yt.title)
print("Channel: ", yt.author)
print("Length: ", yt.length)


yd = yt.streams.get_highest_resolution()
yd.download("C:/Users/jjaco/Downloads")