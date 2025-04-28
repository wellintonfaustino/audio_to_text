from pydub import AudioSegment


# Caminho para o arquivo original e convertido
input_file = "audio.ogg"  # Substitua pela extensão correta
output_file = "arquivo_convertido.wav"

# Converte para WAV (PCM)
audio = AudioSegment.from_file(input_file)
audio.export(output_file, format="wav")

print("Arquivo convertido com sucesso!")