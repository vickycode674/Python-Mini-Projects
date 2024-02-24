# from pytube import YouTube
#
# link = "https://www.youtube.com/watch?v=bBXf0geAFVQ"
#
# youtube_1 = YouTube(link)
#
# # print(youtube_1.title)
# # print(youtube_1.views)
# # print(youtube_1.thumbnail_url)
#
# # vidoes = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_audio=True)
# vid = list(enumerate(videos))
#
# for i in vid:
#     print(i)
#
# print()
# strm = int(input("Enter :"))
# videos[strm].download()
#
# print("Successfully downloaded")

# playlist downloader

from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PLRi1P8GZ-oCZSwzFuSlZiQUG7S4UFUoL1")

# print(f'Downloading:{py.title}')

for video in py.videos:
    video.streams.first().download()