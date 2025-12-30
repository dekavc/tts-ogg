from gtts import gTTS

# Texto de exemplo
text = "Olá! Serviço TTS funcionando."

# Gerar áudio
tts = gTTS(text=text, lang='pt')
tts.save("audio.ogg")

print("Arquivo audio.ogg gerado com sucesso!")
