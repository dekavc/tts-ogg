from flask import Flask, send_file
from gtts import gTTS
import os
import io

app = Flask(__name__)

@app.route("/tts/<text>")
def tts(text):
    # Gera o áudio na memória para evitar problemas com arquivos no servidor
    tts = gTTS(text=text, lang="pt")
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    
    return send_file(fp, mimetype="audio/ogg", as_attachment=False, download_name="audio.ogg")

if __name__ == "__main__":
    # O Railway fornece a porta via variável de ambiente PORT
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
    
