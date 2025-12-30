from flask import Flask
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/tts/<text>")
def tts(text):
    tts = gTTS(text=text, lang="pt")
    filename = "audio.ogg"
    tts.save(filename)
    return f"Arquivo {filename} gerado com sucesso!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
