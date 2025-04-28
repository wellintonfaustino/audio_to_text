import edge_tts
import asyncio

async def gerar_audio():
    texto = "Olá, tudo bem? Wellington, aqui quem está falando é a Beatriz. Eu sou especialista em dores reumáticas e trabalho com produtos físicos 100% naturais. O motivo do meu contato é que vi, aqui no sistema, que você acessou nosso site. Gostaria de entender melhor o que você sente, o que poderia melhorar a sua saúde e seu bem-estar hoje, ou até mesmo o de alguém da sua família. Queria conversar um pouquinho para entender melhor quais são essas dores que você (ou alguém da sua família) sente, já que você acessou nosso site para saber mais sobre nossos produtos. Podemos conversar um pouquinho?" 
    comunicador = edge_tts.Communicate(texto, voice="pt-BR-FranciscaNeural", rate="-10%")
    await comunicador.save("audio.mp3")
    """
    pt-BR-AntonioNeural                Male      General                Friendly, Positive
    pt-BR-FranciscaNeural              Female    General                Friendly, Positive
    pt-BR-ThalitaMultilingualNeural    Female    General                Friendly, Positive
    """

asyncio.run(gerar_audio())
print("Áudio salvo como audio.mp3")