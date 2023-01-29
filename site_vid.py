import streamlit as st
#streamlit run site_vid.py
import youtube_dl

def progresso(d):
    global tzao
    if(d['status'] == 'downloading'):
        print(d['_percent_str'])
        tzao.text(d['_percent_str'])
    if(d['status']=='finished'):
        file = open(d['filename'], 'rb')
        st.download_button("Download file", file, file_name='video.mp4')

def baixa_video(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s','progress_hooks': [progresso]})

    with ydl:
        result = ydl.extract_info(
            url,
            download=True  # We just want to extract the info
        )
    return result

st.title('Flavin site')
video=st.text_input('Url do video:',placeholder='https://www.youtube.com/watch?v=9hMmThJNZu0')
tzao = st.empty()
if st.button('Baixar'):
    print(video)
    if(video!=''):
        resultado = baixa_video(video)

    else:
        print("digita certo")
