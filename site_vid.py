import streamlit as st
#streamlit run site_vid.py
import youtube_dl

def progresso(d):
    global tzao
    if(d['status'] == 'downloading'):
        tzao.text(d['_percent_str'])#title
    if(d['status']=='finished'):
        file = open(d['filename'], 'rb')
        titulo = d['filename']
        st.text('Video ' + titulo[0:len(titulo) - 4] + " baixado!")
        st.download_button("Download Video", file, file_name=titulo)



def baixa_video(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','progress_hooks': [progresso]})

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
if st.button('Baixar'):
    if(video!=''):
        resultado = baixa_video(video)

    #else:
       # st.warning('Link invalido', icon="⚠️")
