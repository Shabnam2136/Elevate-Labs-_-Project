# gen_key.py
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key.decode())  # copy this and store securely
# server.py
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import os
from datetime import datetime

# load key from file (same one used by the client)
with open("fernet_key.txt", "rb") as f:
    KEY = f.read().strip()

fobj = Fernet(KEY)
app = Flask(__name__)
RECEIVED_DIR = "received_logs"
os.makedirs(RECEIVED_DIR, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    payload = request.get_json(force=True)
    enc_b64 = payload.get("data")   # base64-like string from client
    timestamp = payload.get("ts")
    source = payload.get("source", "client")

    try:
        token = enc_b64.encode()
        plaintext = fobj.decrypt(token).decode()
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 400

    # store a readable copy (timestamped)
    filename = os.path.join(RECEIVED_DIR, f"recv_{datetime.utcnow().isoformat()}_from_{source}.log")
    with open(filename, "w", encoding="utf-8") as fh:
        fh.write(f"received_ts: {timestamp}\n")
        fh.write("decrypted_payload:\n")
        fh.write(plaintext)

    print(f"[{datetime.utcnow().isoformat()}] Received and decrypted log from {source}:")
    print(plaintext)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # WARNING: for an isolated lab only. Do not expose to internet.
    app.run(host="127.0.0.1", port=5000, debug=True)
# client_sim.py
import time
import json
import socket
import requests
from cryptography.fernet import Fernet
from datetime import datetime
import os
import random
import string

# config
KEY_FILE = "fernet_key.txt"
LOG_DIR = "local_encrypted_logs"
os.makedirs(LOG_DIR, exist_ok=True)
SERVER_URL = "http://127.0.0.1:5000/upload"  # local server

# load key
with open(KEY_FILE, "rb") as f:
    KEY = f.read().strip()
fobj = Fernet(KEY)

def make_synthetic_event():
    # create a fake 'keystroke' line — purely synthetic for training/testing
    text = ''.join(random.choices(string.ascii_lowercase + " ", k=random.randint(5, 25)))
    meta = {
        "typed": text,
        "source": "sim-client-1",
        "local_ts": datetime.utcnow().isoformat()
    }
    return json.dumps(meta)

def encrypt_and_store(plaintext):
    token = fobj.encrypt(plaintext.encode())
    ts = datetime.utcnow().isoformat()
    filename = os.path.join(LOG_DIR, f"log_{ts.replace(':','-')}.enc")
    with open(filename, "wb") as fh:
        fh.write(token)
    return token, ts

def send_to_server(token, ts):
    payload = {
        "data": token.decode(),  # token is a URL-safe base64 token string
        "ts": ts,
        "source": "sim-client-1"
    }
    try:
        resp = requests.post(SERVER_URL, json=payload, timeout=5)
        return resp.status_code, resp.text
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    # generate a few synthetic events and send
    for i in range(5):
        ev = make_synthetic_event()
        token, ts = encrypt_and_store(ev)
        status, text = send_to_server(token, ts)
        print(f"[{datetime.utcnow().isoformat()}] Sent event. Server status: {status}. Reply: {text}")
        time.sleep(1 + random.random()*2)
