from flask import Flask, request, send_file
import pyttsx3
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return {'error': 'No text provided'}, 400

    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
