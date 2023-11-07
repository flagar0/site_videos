import re
import streamlit as st
from pytube import YouTube
#streamlit run site_video.py

if 'url_vid' not in st.session_state:
    st.session_state.url_vid = ''

def progresso(d):
    if(d['status'] == 'downloading'):
        global tzao
        tzao.text(d['_percent_str'])#title
        st.progress(value)
        #TODO> barra que sobe
    if(d['status']=='finished'):
        file = open(d['filename'], 'rb')
        titulo = d['filename']
        st.text('Video ' + titulo[0:len(titulo) - 4] + " baixado!")
        st.download_button("Download Video", file, file_name=titulo)
#TODO> adicionar caixinha com link para download

def baixar_video():
    url = st.session_state.url_vid
    yt = YouTube(url)
    nomeArquivo = re.sub(r"[^a-zA-Z0-9_.-]", "", yt.title.replace(" ", "_"))

    try:
        yt.streams.get_highest_resolution().download(filename = "%s.mp4" % nomeArquivo)
    except Exception as erro:
        error.warning('Link invalido', icon="⚠️")
        print(erro)

st.title('Youtube Video Downloader')

#abre o css
with open('estilo.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Cria o form
def cria_area(thumb,titulo):
    confirma = st.container()

    confirma.markdown(f"""<p id="nome_vid">"""+titulo+"""</p>""",unsafe_allow_html=True)
    confirma.image(thumb,width=300)

    confirma.button("Baixar",type='primary',key='baixar',on_click=baixar_video)

#cria  coluna
col1, col2 = st.columns(2,gap='small')
video = col1.text_input('Url do video:', placeholder='https://youtu.be/dQw4w9WgXcQ')
if col2.button('Procurar',key='procurar'):
    if (video != ''):
        yt = YouTube(video)

        st.session_state.url_vid = video
        cria_area(yt.thumbnail_url, yt.title)


tzao = st.empty()
error = st.empty()
baixado = st.empty()
#TODO> creditos
