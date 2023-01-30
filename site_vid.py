import streamlit as st
import json
#streamlit run site_vid.py
import yt_dlp

def progresso(d):
    global tzao
    if(d['status'] == 'downloading'):
        tzao.text(d['_percent_str'])#title
        #TODO> barra que sobe
    if(d['status']=='finished'):
        file = open(d['filename'], 'rb')
        titulo = d['filename']
        st.text('Video ' + titulo[0:len(titulo) - 4] + " baixado!")
        st.download_button("Download Video", file, file_name=titulo)
#TODO> adicionar caixinha com link para donwload


def baixa_video(url):
    ydl = yt_dlp.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','progress_hooks': [progresso]})

    with ydl:
        try:
            result = ydl.extract_info(
            url,
            download=True  # We just want to extract the info
            )
            return result
        except Exception as erro:
            error.warning('Link invalido', icon="⚠️")
            print(erro)

st.title('Youtube Video Donwloader')
video=st.text_input('Url do video:',placeholder='https://www.youtube.com/watch?v=9hMmThJNZu0')
tzao = st.empty()
error = st.empty()
#TODO> creditos
if st.button('Baixar'):
    #TODO> adicionar confirmação de video
    if(video!=''):
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(video, download=False)

            print(json.dumps(ydl.sanitize_info(info)))
        #resultado = baixa_video(video)

    #else:
       # st.warning('Link invalido', icon="⚠️")
