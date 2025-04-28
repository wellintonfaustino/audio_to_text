import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Carrega o arquivo de áudio
audio_file_path = "arquivo_convertido.wav"

with sr.AudioFile(audio_file_path) as source:
    # Lê o áudio do arquivo
    audio_data = recognizer.record(source)
    try:
        # Usa o Google Web Speech API para transcrever
        texto = recognizer.recognize_google(audio_data, language="pt-BR")  # Defina o idioma desejado
        print("Texto transcrito:")
        print(texto)
        # Salva o texto em um arquivo
        with open("transcricao.txt", "w", encoding="utf-8") as f:
            f.write(texto)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro na solicitação do serviço de reconhecimento: {e}")