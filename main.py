from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    if 'Twitterbot' in request.headers.get('User-Agent', ''):
        return redirect("https://x.ai")
    else:
        return redirect("https://chat.openai.com")