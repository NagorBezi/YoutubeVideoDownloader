from pytube import YouTube

link = input("Enter URL: \n")

vid = YouTube(link)
vid_stream = vid.streams.get_highest_resolution()
vid_stream.download()
print("Download Succesful")
