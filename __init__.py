from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# init app
app = Flask(__name__)

# Init cors
CORS(app)

# Encrypt
@app.route('/encrypt/<int:p>/<int:q>/<int:koprima>', methods=['POST'])
def encrypt(p, q, koprima):
    n = p * q 
    phi = (p-1) * (q-1)

    e = koprima
    d = modinv(e, phi)
   
    s = request.json['msg']
    enc = {
        "message" : encrypt_string(s, e, n)
    }

    print(enc)
    
    return jsonify(enc)
    
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def coprimes(a):
    l = [x for x in range(2, a) 
        if gcd(a, x) == 1 
            and modinv(x, phi) is not None
            and modinv(x, phi) != x]
    return l

def encrypt_block(m, e, n):
    c = modinv(m**e, n)

    return c

def encrypt_string(s, e, n):
    return ''.join([chr(encrypt_block(ord(x), e, n)) for x in list(s)])

# Decrypt
@app.route('/decrypt/<int:p>/<int:q>/<int:koprima>', methods=['POST'])
def decrypt(p, q, koprima):
    n = p * q
    phi=(p-1)*(q-1)
    e = koprima
    d = modinv(e,phi)
    s = request.json['msg']
    dec = {
        "message" : decrypt_string(s, d, n)
    }

    return jsonify(dec)

def decrypt_block(c, d, n):
    m = modinv(c**d, n)

    return m
    
def decrypt_string(s, d, n):
    return ''.join([chr(decrypt_block(ord(x), d, n)) for x in list(s)])

def getApp():
    return app

# Run Server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)