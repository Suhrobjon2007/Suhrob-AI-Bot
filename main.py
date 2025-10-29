from flask import Flask
import threading
import bot  # bu pastdagi bot.py ni ishga tushiradi

app = Flask(__name__)

@app.route('/')
def home():
    return "Suhrob AI Bot ishlayapti ✅"

# Flask serverni ishga tushirish
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
