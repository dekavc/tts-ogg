from gtts import gTTS
import time

# Loop infinito leve para manter o container vivo
while True:
    # Texto de teste
    text = "Olá! Serviço TTS funcionando."
    
    # Gerar áudio OGG
    tts = gTTS(text=text, lang='pt')
    tts.save("audio.ogg")
    
    print("Arquivo audio.ogg gerado com sucesso!")
    
    # Espera 60 segundos antes de gerar novamente (evita travar CPU)
    time.sleep(60)
