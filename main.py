from flask import Flask, send_file
from gtts import gTTS
import os
import io
import gc  # Importado para ajudar a reduzir o uso de memória

app = Flask(__name__)

# Rota para o link principal não dar erro 404
@app.route("/")
def index():
    return "API de Voz Online! Use: /tts/seu-texto-aqui"

@app.route("/tts/<text>")
def tts(text):
    try:
        # Gera o áudio na memória
        tts = gTTS(text=text, lang="pt")
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        # Envia o arquivo
        response = send_file(
            fp, 
            mimetype="audio/ogg", 
            as_attachment=False, 
            download_name="audio.ogg"
        )
        
        # Limpa a memória após gerar a resposta para evitar o erro de 1.1GB
        gc.collect()
        
        return response
    except Exception as e:
        return f"Erro ao gerar áudio: {str(e)}", 500

if __name__ == "__main__":
    # O Railway usa a variável PORT. O padrão 8080 é comum no Railway.
    port = int(os.environ.get("PORT", 8080))
    # '0.0.0.0' é obrigatório para o Railway expor a aplicação
    app.run(host="0.0.0.0", port=port)
