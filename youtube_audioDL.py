from pytubefix import YouTube


while True:

    video_url = input("Enter YouTube video URL (or 'exit' to quit): ")
    if video_url.lower() == 'exit':
        break
    output_path = input("Enter output path (or press Enter for default): ")
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)