from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Alert Received:", data)
    os.system("ansible-playbook heal-nginx.yml")
    return 'Webhook received and Ansible triggered!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
