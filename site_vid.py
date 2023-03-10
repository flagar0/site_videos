import streamlit as st
import json
#streamlit run site_vid.py
import yt_dlp

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
#TODO> adicionar caixinha com link para donwload


def baixa_video():
    url=st.session_state.url_vid
    ydl = yt_dlp.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','progress_hooks': [progresso]})

    with ydl:
        try:
            ydl.download(url)
        except Exception as erro:
            error.warning('Link invalido', icon="⚠️")
            print(erro)

st.title('Youtube Video Donwloader')
#abre o css
with open('estilo.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#Cria o form
def cria_area(thumb,titulo):
    confirma = st.container()

    confirma.markdown(f"""<p id="nome_vid">"""+titulo+"""</p>""",unsafe_allow_html=True)
    confirma.image(thumb,width=300)

    confirma.button("Baixar",type='primary',key='baixar',on_click=baixa_video)

#cria  coluna
col1, col2 = st.columns(2,gap='small')
video=col1.text_input('Url do video:',placeholder='https://www.youtube.com/watch?v=9hMmThJNZu0',value='https://www.youtube.com/watch?v=9hMmThJNZu0')
if col2.button('Procurar',key='procurar'):
    if (video != ''):
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(video, download=False)

            st.session_state.url_vid=video
            cria_area(info['thumbnail'],info['title'])


tzao = st.empty()
error = st.empty()
baixado = st.empty()
#TODO> creditos

