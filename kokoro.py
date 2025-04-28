# pip install kokoro streamlit soundfile
# streamlit run kokoro.py

import streamlit as st
from kokoro import KPipeline
import soundfile as sf
import os

# Carregar pipeline
pipeline = KPipeline()

# Listar todas as vozes disponíveis
# pipeline.list_voices() retorna dicionário
lista_vozes = pipeline.list_voices()

# Apenas vozes de português (começam com 'p')
vozes_portugues = {k: v for k, v in lista_vozes.items() if k.startswith('p')}

# Configurações da página
st.set_page_config(page_title="Kokoro TTS em Português", layout="centered")
st.title("🗣️ Kokoro TTS - Múltiplas Vozes (Português)")
st.markdown("Converta seu texto em fala, escolhendo entre várias vozes em português.")

# Entrada de texto
texto = st.text_area("Digite o texto que deseja converter:", height=150)

# Seleção de voz
voz_escolhida = st.selectbox(
    "Escolha a voz:",
    options=list(vozes_portugues.keys()),
    format_func=lambda x: vozes_portugues[x]['desc']
)

# Botão de geração
if st.button("🔊 Gerar Áudio"):
    if not texto.strip():
        st.warning("Por favor, insira um texto.")
    else:
        with st.spinner("Gerando áudio..."):
            generator = pipeline(texto, voice=voz_escolhida)
            for _, _, audio in generator:
                sf.write("saida.wav", audio, 24000)
                break  # Gera apenas o primeiro trecho

            st.success("Áudio gerado!")
            st.audio("saida.wav", format="audio/wav")
