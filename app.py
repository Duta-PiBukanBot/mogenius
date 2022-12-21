import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://mogenius:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://mogenius: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@github.com/username/reponame ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
