import streamlit as st
from pytube import YouTube
import os

st.set_page_config(page_title="YouTube para MP3", page_icon="🎵")
st.title("🎧 Baixar áudio de YouTube (MP3)")

link = st.text_input("Cole o link do vídeo do YouTube aqui:")

if link:
    try:
        yt = YouTube(link)
        st.success(f"🎬 Título do vídeo: {yt.title}")

        if st.button("Baixar MP3"):
            with st.spinner("Baixando..."):
                audio_stream = yt.streams.filter(only_audio=True).first()
                out_file = audio_stream.download()
                base, ext = os.path.splitext(out_file)
                mp3_file = base + '.mp3'
                os.rename(out_file, mp3_file)

                with open(mp3_file, 'rb') as f:
                    st.download_button(
                        label="Clique aqui para baixar o MP3",
                        data=f,
                        file_name=f"{yt.title}.mp3",
                        mime='audio/mpeg'
                    )
    except Exception as e:
        st.error(f"Erro: {str(e)}")
