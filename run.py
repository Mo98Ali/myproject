from __init__ import app
import ssl
# Mein Pfad ==> C:\Users\ali\Desktop\React\projekt\SW\Verschlusselung\Verschlüsselung\SSL Dateien
ssl_cert = "C:\\Users\\ali\\Desktop\\React\\projekt\\SW\\Verschlusselung\\SSL Dateien\\self-signed-ca-cert.crt"
ssl_key = "C:\\Users\\ali\\Desktop\\React\\projekt\\SW\\Verschlusselung\\SSL Dateien\\private-ca.key"

cryp = ssl.SSLContext(ssl.PROTOCOL_TLS)
cryp.options |= ssl.OP_NO_TLSv1| ssl.OP_NO_TLSv1_1
cryp.load_cert_chain(ssl_cert,ssl_key)

if __name__ == "__main__":
    app.run(debug = True,ssl_context = cryp)

