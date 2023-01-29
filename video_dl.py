import youtube_dl

def baixa_video(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            url,
            download=False  # We just want to extract the info
        )
    return result
