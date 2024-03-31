from pytube import YouTube

link = input("ENTER YOUTUBE LINK:- ")
save_location = r"C:\Users\Rohit K\Downloads"
url = YouTube(link)
print("Video title: ", url.title)
print("Number of views on the video: ",url.views)
print("Length of the video ", url.length, "seconds")
print("Description:", url.description)

n=int(input("If you want to download the highest resolution, enter 1. If you need a different resolution, enter 2. If you want to download audio, enter 3: "))

if n == 1:
    try:
        video = url.streams.get_highest_resolution()
        print("Downloading.............")
        video.download(save_location)
        print("Video downloaded successfully!!!")
    except Exception as e:
        print("Something went wrong:", e)
elif n == 2:
    # Show available resolutions
    print("Available Resolutions:")
    for stream in url.streams.filter(progressive=True):
        if stream.resolution:
            print("Resolution:", stream.resolution)

    # Prompt user to enter resolution
    resolution = input("Enter resolution: ")
    strm = url.streams.filter(res=resolution)
    cs = strm.first()
    print("Downloading.............")
    cs.download(save_location)
    print("Video downloaded successfully!!!")

elif n == 3:
    audio = url.streams.filter(only_audio=True).first()
    print("Downloading audio...")
    audio.download(output_path=save_location)
    print("Audio downloaded successfully!")
else:
    print("Invalid choice!")
