import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'


os.system("git clone https://Duta-PiBukanBot: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@github.com/Duta-PiBukanBot/management okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m Telegram &")
